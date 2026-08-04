---
name: tiktok-transcript
description: Extract existing TikTok captions or explicitly transcribe TikTok video audio into text and timed segments. Use when a user asks for a TikTok transcript, captions, subtitles, quotes, timestamps, or audio transcription.
---

# TikTok Transcript

Use the Agent Body MCP server at `/mcp/tiktok-transcript`.

Read [references/tool-reference.md](references/tool-reference.md) for exact inputs, outputs, and tool-selection rules.

## Workflow

1. Confirm the TikTok video URL and whether the user wants existing captions or audio transcription.
2. Prefer `tiktok_transcript` when the request can be satisfied by an existing caption track. Add `language` only when requested.
3. Use `tiktok_audio_to_transcript` only when the user explicitly asks to transcribe audio or explicitly approves it after captions are unavailable. This Tool is separately metered and limited to 10 minutes.
4. Read the result from `data`. Use `text` for full-text tasks and `segments` for timestamps or quotes.
5. Preserve `language`, `captionType`, segment order, and timing boundaries.

Never silently fall back from caption extraction to audio transcription. Report unavailable captions, unavailable languages, invalid duration, and service failures without inventing text.
