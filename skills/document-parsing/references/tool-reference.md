# Document Parsing Tool Reference

MCP server: `/mcp/document-parsing`

| Tool ID | MCP Tool |
|---|---|
| `document.upload` | `document_upload` |
| `document.parsing` | `document_parsing` |
| `document.result.get` | `document_result_get` |

REST uses `POST /v1/tools/{tool_id}/call`.

Successful calls return the business result in `data`.

## `document_upload`

Creates a short-lived upload session for a local file.

| Field | Type | Required | Rules |
|---|---|---:|---|
| `fileName` | string | Yes | 1-255 characters |
| `contentType` | string | Yes | 1-128 characters |
| `sizeBytes` | integer | Yes | 1-52,428,800 bytes by default |

The result contains `uploadId`, `uploadUrl`, `method` (`PUT`), `headers`, `expiresAt`, and `maxBytes`. Stream the exact local file as raw bytes with the returned method and headers. The default session lifetime is 30 minutes.

## `document_parsing`

Use exactly one source form:

```json
{"uploadId":"<uuid>"}
```

```json
{"fileUrl":"https://example.com/report.pdf","fileName":"report.pdf"}
```

`fileUrl` must use HTTPS and is limited to 1,024 characters. Optional booleans are `analysisChart`, `mergeTables`, `relevelTitles`, `recognizeSeal`, and `returnSpanBoxes`.

The result contains `documentId`, `pages`, `preview`, and `read`. Documents are limited to 100 pages and normalized stored results to 8 MiB.

## `document_result_get`

Required input: `documentId` (UUID).

Optional ranges:

| Field | Type | Rules |
|---|---|---|
| `pageStart` | integer | Minimum 1 |
| `pageEnd` | integer | 1-100 |
| `markdownStart` | integer | Minimum 0 |
| `markdownEnd` | integer | Minimum 0 |

Results are scoped to the API key that created the parsed document. The result contains `documentId`, returned page coverage, `pages`, `markdown`, `blocks`, and `markdownSpans`.

## Local upload bridge

Pass the values returned by `document_upload` to the bundled script:

```bash
python scripts/upload_document.py \
  --file ./report.pdf \
  --upload-url "<temporary-upload-url>" \
  --method PUT \
  --headers-file ./temporary-upload-headers.json \
  --max-bytes 52428800
```

Do not log or retain the signed URL and headers after the upload completes.
