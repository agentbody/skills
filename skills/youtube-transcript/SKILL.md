---
name: youtube-transcript
description: Extract text and timed segments from an existing YouTube manual or automatic subtitle track. Use when a user asks for a YouTube transcript, captions, subtitles, quotes, or timestamped text without audio transcription.
---

# YouTube Transcript

Extract an existing subtitle track through the Agent Body MCP server at `/mcp/youtube-transcript` using `youtube_transcript`.

Read [references/tool-reference.md](references/tool-reference.md) for the exact input and output contract.

## Workflow

1. Confirm the YouTube video URL and optional requested language.
2. Call `youtube_transcript` with `url` and add `language` only when the user requests one.
3. Read `videoId`, `language`, `captionType`, `text`, and `segments` from `data`.
4. Use `text` for full-text tasks and `segments` for timestamps or quotes. Preserve the returned language and caption type.

This Tool reads an existing manual or automatic subtitle track. It does not transcribe audio or create missing captions. On `TRANSCRIPT_UNAVAILABLE` or `LANGUAGE_UNAVAILABLE`, report the limitation and do not invent text or silently switch to another service.
