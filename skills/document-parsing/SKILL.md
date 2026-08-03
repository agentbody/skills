---
name: document-parsing
description: Upload and parse PDFs, DOC and DOCX files, scans, images, XLSX spreadsheets, and other document formats into high-quality Markdown and structured content, with page-level or Markdown-range retrieval. Use when a user asks to extract, convert, inspect, search, or analyze documents, including multi-page files and long contracts.
---

# Document Parsing

Convert and inspect documents through the Agent Body MCP server at `/document-parsing/mcp`.

Read [references/tool-reference.md](references/tool-reference.md) for the job lifecycle and extraction-quality rules.

## Fixed workflow

### 1. Define the extraction target

Identify the source file, requested output (full Markdown, structured content, selected pages, or a Markdown range), language if relevant, and any tables, headings, fields, or sections that matter. For large files, decide the smallest useful retrieval window. For a local file, resolve its filename, MIME type, and exact byte size before calling MCP.

### 2. Create a temporary upload session

Call `document-upload` with `fileName`, `contentType`, and `sizeBytes`. Read the returned fields from the MCP result's `data` object. The Gateway validates a positive size up to 50 MiB and returns `uploadId`, `uploadUrl`, `method` (`PUT`), `headers`, `expiresAt`, and `maxBytes`. Retain these session details without exposing the URL or signed headers. Upload only the file the user authorized.

### 3. Bridge the local file to the MCP upload URL

Run [scripts/upload_document.py](scripts/upload_document.py) with the local path and the URL/method/headers from the MCP response. The script streams the local file to the Gateway's short-lived object-storage presigned URL and prints only a small JSON success record. Pass `maxBytes` to enforce the server limit. Do not expose the upload URL or signed headers in the final answer.

Example shape; map the actual MCP response fields to these arguments:

```bash
python scripts/upload_document.py \
  --file ./document.pdf \
  --upload-url "<temporary-upload-url>" \
  --method PUT \
  --headers-file ./temporary-upload-headers.json \
  --max-bytes 52428800
```

The current Gateway contract is raw `PUT` bytes, not multipart form data. Do not send the local path as `fileUrl` and do not replace `uploadId` with the R2 URL in the parse call.

### 4. Start parsing

Call `document-parsing` with `uploadId` only. Read `documentId`, `pages`, `preview`, and `read` from the MCP result's `data` object. The Gateway resolves the Key-scoped upload session to a short-lived presigned GET URL for the parser, then retains the result under the API key.

### 5. Retrieve the minimum useful result

Call `document-parsing-result` with the required `documentId` and only the range needed:

- for the complete Markdown when the user asks for a full conversion;
- for selected pages when the question is page-oriented;
- for a Markdown range when the user names a section or text span.

Use `pageStart`/`pageEnd` for pages and `markdownStart`/`markdownEnd` for character ranges. The result is Key-scoped and can include Markdown, pages, blocks, and Markdown span mappings.

Preserve page boundaries, headings, table structure, list order, and parser warnings when supplied.

### 6. Verify before interpretation

Check that the returned result covers the requested pages/range and that identifiers match the upload job. Mark OCR uncertainty, missing pages, malformed tables, and parser warnings. Separate extracted text from any summary or analysis.

## Failure handling and safety

- **Upload failure**: report the failure and do not retry indefinitely.
- **Parsing failure**: preserve the job identifier and service error; do not claim extraction succeeded.
- **Incomplete result**: identify missing pages/ranges and retrieve only the missing portion if supported.
- **Temporary-session expiry**: request a new authorized upload rather than reusing expired credentials.

Treat uploaded documents as private and temporary. The default upload session TTL is 30 minutes and the default size limit is 50 MiB. After a successful parse, the Gateway marks the session consumed and deletes the temporary R2 object. Do not expose session tokens, signed URLs, credentials, or unrelated document content.
