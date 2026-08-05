---
name: document-parsing
description: Parse a document at an HTTPS URL into Markdown and structured content, then retrieve complete, page-level, or Markdown-range results. Use when a user asks to extract, convert, inspect, search, or analyze a document available at an HTTPS URL.
---

# Document Parsing

Parse and inspect documents through the Agent Body MCP server at `/mcp/document-parsing`.

Read [references/tool-reference.md](references/tool-reference.md) for exact schemas, limits, and result fields.

## Workflow

1. Confirm the document is reachable at an HTTPS URL and determine the smallest useful output range.
2. Call `document_parsing` with `fileUrl` and `fileName`. Both are required.
3. Read `documentId`, page count, preview, and read metadata from `data`.
4. Call `document_result_get` with `documentId` and only the required page or Markdown range.
5. Verify returned coverage before summarizing. Preserve page boundaries, headings, table structure, and parser warnings when available.

This service accepts URL input only. Local paths, `file://` URLs, Base64 payloads, and multipart uploads are not supported, and there is no upload Tool. When a user supplies a local file, ask them to publish it to an HTTPS URL the service can reach, such as a signed object-storage link.

Never pass a local path as `fileUrl` or embed credentials in the URL; a URL containing userinfo is rejected.

Treat document content as private. Separate extracted content from interpretation and report unreadable text, missing pages, malformed tables, or incomplete ranges instead of filling gaps.
