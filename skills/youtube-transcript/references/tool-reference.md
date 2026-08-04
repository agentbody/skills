# YouTube Transcript Tool Reference

MCP server: `/mcp/youtube-transcript`

Tool ID: `youtube.transcript`

MCP Tool: `youtube_transcript`

REST: `POST /v1/tools/youtube.transcript/call`

## Input

| Field | Type | Required | Rules |
|---|---|---:|---|
| `url` | string (URI) | Yes | Non-empty YouTube video URL |
| `language` | string | No | Requested subtitle language, up to 35 characters |

## Output

Successful calls return:

- `videoId`: normalized video identifier.
- `language`: selected subtitle language.
- `captionType`: `manual` or `auto`.
- `text`: complete normalized transcript text.
- `segments`: ordered objects with `startMs`, `endMs`, and `text`.

`TRANSCRIPT_UNAVAILABLE` means no usable existing subtitle track was found. `LANGUAGE_UNAVAILABLE` means the requested language was not available. Preserve segment ordering and do not manufacture timestamps for plain text.
