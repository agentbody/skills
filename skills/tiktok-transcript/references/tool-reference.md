# TikTok Transcript Tool Reference

MCP server: `/mcp/tiktok-transcript`

| Tool ID | MCP Tool |
|---|---|
| `tiktok.transcript` | `tiktok_transcript` |
| `tiktok.audio_to_transcript` | `tiktok_audio_to_transcript` |

REST uses `POST /v1/tools/{tool_id}/call`.

## `tiktok_transcript`

Use this Tool to extract an existing TikTok caption track.

| Field | Type | Required | Rules |
|---|---|---:|---|
| `url` | string (URI) | Yes | Non-empty TikTok video URL |
| `language` | string | No | Requested caption language, up to 35 characters |

The result contains `videoId`, `language`, `captionType` (`manual` or `auto`), `text`, and ordered `segments` with `startMs`, `endMs`, and `text`.

## `tiktok_audio_to_transcript`

Use this Tool only for explicit audio transcription.

| Field | Type | Required | Rules |
|---|---|---:|---|
| `url` | string (URI) | Yes | Non-empty TikTok video URL; video duration must not exceed 10 minutes |

This Tool does not accept a language argument. The result contains `videoId`, detected `language`, `captionType` (`transcribed`), `text`, and timed `segments`.

## Selection and failures

- Do not call audio transcription automatically after `TRANSCRIPT_UNAVAILABLE`.
- `LANGUAGE_UNAVAILABLE` applies to requested existing captions.
- A video longer than the audio limit is rejected as `INVALID_ARGUMENTS`.
- Preserve returned timestamps and never infer missing segments.
