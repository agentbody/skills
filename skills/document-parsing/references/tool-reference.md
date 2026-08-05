# Document Parsing Tool Reference

MCP server: `/mcp/document-parsing`

| Tool ID | MCP Tool |
|---|---|
| `document.parsing` | `document_parsing` |
| `document.result.get` | `document_result_get` |

REST uses `POST /v1/tools/{tool_id}/call`.

Successful calls return the business result in `data`.

## `document_parsing`

This Tool accepts URL input only:

```json
{"fileUrl":"https://files.example.com/report.pdf","fileName":"report.pdf"}
```

| Field | Type | Required | Rules |
|---|---|---:|---|
| `fileUrl` | string | Yes | HTTPS only, up to 1,024 characters, must include a host, must not contain userinfo |
| `fileName` | string | Yes | 1-255 characters |
| `analysisChart` | boolean | No | Optional parsing option |
| `mergeTables` | boolean | No | Optional parsing option |
| `relevelTitles` | boolean | No | Optional parsing option |
| `recognizeSeal` | boolean | No | Optional parsing option |
| `returnSpanBoxes` | boolean | No | Optional parsing option |

No other fields are accepted. `uploadId`, local paths, `file://` URLs, HTTP URLs, credential-bearing URLs, Base64 payloads, and multipart uploads are rejected as `INVALID_ARGUMENTS` without charge.

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

This Tool cannot be granted on its own. An API key reaches it only by holding `document.parsing` access, and it returns `DOCUMENT_RESULT_NOT_FOUND` for a document created by a different key.
