---
name: document-parsing
description: Upload and parse documents into Markdown and structured content, then retrieve complete, page-level, or Markdown-range results. Use when a user asks to extract, convert, inspect, search, or analyze a local document or an HTTPS document URL.
---

# Document Parsing

Parse and inspect documents through the Agent Body MCP server at `/mcp/document-parsing`.

Read [references/tool-reference.md](references/tool-reference.md) for exact schemas, limits, and result fields.

## Workflow

1. Identify the source and smallest useful output range. For a local file, determine its filename, MIME type, and exact byte size.
2. Choose one input path:
   - Local file: call `document_upload`, upload the authorized bytes with [scripts/upload_document.py](scripts/upload_document.py), then call `document_parsing` with `uploadId`.
   - Public or signed HTTPS file: call `document_parsing` with `fileUrl` and `fileName`.
3. Read `documentId`, page count, preview, and read metadata from `data`.
4. Call `document_result_get` with `documentId` and only the required page or Markdown range.
5. Verify returned coverage before summarizing. Preserve page boundaries, headings, table structure, and parser warnings when available.

The local upload is a raw `PUT`, not multipart form data. Never pass a local path as `fileUrl`, expose signed upload URLs or headers, or reuse an expired upload session.

Treat document content as private. Separate extracted content from interpretation and report unreadable text, missing pages, malformed tables, or incomplete ranges instead of filling gaps.
