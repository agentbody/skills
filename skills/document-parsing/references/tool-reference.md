# Document Parsing Tool Reference

MCP server: `/document-parsing/mcp`

The Gateway contract below is implemented in `agentbody-gateway/internal/registry/document_parsing.go` and `internal/documentparsing/service.go`. Use the live MCP schema if it differs.

## Tools

| Tool | Purpose | State to retain |
|---|---|---|
| `document-upload` | Create a temporary document upload session | `fileName`, `contentType`, `sizeBytes` |
| `document-parsing` | Parse the uploaded document to Markdown and structured content | Parsing job/document ID, status, warnings |
| `document-parsing-result` | Read complete, page-level, or Markdown-range output | Requested range, returned range, completeness |

## Upload contract

`document-upload` accepts:

```json
{
  "fileName": "report.pdf",
  "contentType": "application/pdf",
  "sizeBytes": 123456
}
```

The response contains:

```json
{
  "uploadId": "<uuid>",
  "uploadUrl": "https://<r2-presigned-url>",
  "method": "PUT",
  "headers": {"Content-Type": "application/pdf"},
  "expiresAt": "<timestamp>",
  "maxBytes": 52428800
}
```

The MCP transport wraps successful business results as `{"data": <result>}`; the object above is the value of `data`.

Upload raw file bytes with the returned `PUT` URL and headers. The object is stored in Agent Body's API-key-scoped temporary object storage; the client does not need to know the internal object key.

The default session lifetime is 30 minutes. The maximum upload is 50 MiB unless the Gateway deployment changes `DOCUMENT_UPLOAD_MAX_BYTES`.

The parser accepts at most 100 pages per document and the normalized stored result is limited to 8 MiB. Large results should be read through `document-parsing-result` ranges instead of requesting the whole document repeatedly.

## Parse and read contract

For a local upload, call `document-parsing` with:

```json
{"uploadId":"<uuid>"}
```

The response returns `documentId`, `pages`, `preview`, and `read` metadata. Then call `document-parsing-result` with `documentId` and optional `pageStart`, `pageEnd`, `markdownStart`, or `markdownEnd`. Results are scoped to the authenticated API key.

## Extraction quality record

For every response retain:

- source file identity;
- parsing job/document identifier;
- requested page or Markdown range;
- returned coverage;
- parser/OCR warnings;
- whether the result is extracted text, structured data, or an interpretation.

Never silently fill gaps in a document. Report missing pages, unreadable text, malformed tables, and expired sessions.

## Local-file bridge

`document-upload` is the boundary between the MCP service and the agent's local filesystem. A local path is not itself a URL. Use `scripts/upload_document.py` to stream the authorized local file to the returned presigned URL, passing the exact headers returned by the service. Do not log or persist the URL or headers after the upload session expires. After successful parsing, the Gateway marks the session consumed and deletes the temporary object.
