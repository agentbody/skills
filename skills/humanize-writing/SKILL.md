---
name: humanize-writing
description: Rewrite AI-generated or mechanical text into more natural writing through Agent Body while preserving meaning, facts, language, and intent. Use when users ask to humanize, rewrite, reduce AI tone, or make text sound more natural.
---

# Humanize Writing

Rewrite text through the Agent Body MCP server at `/mcp/humanizer` using `humanizer_text`.

Read [references/tool-reference.md](references/tool-reference.md) for the exact input contract and rewrite modes.

## Workflow

1. Identify names, numbers, dates, links, citations, legal qualifiers, product terms, formatting, and claims that must remain unchanged.
2. Send the source in `text`. Add `language` only when needed and choose `mode` according to the requested rewrite strength.
3. Read the rewritten string from `data.text`.
4. Compare the result with the source. Preserve facts, negations, qualifications, language, and intentional formatting.
5. Return only the rewritten text unless the user asks for an explanation or comparison.

Do not send unsupported controls such as `tone`, `audience`, or `style`. Do not use the tool to fact-check, translate without instruction, add information, or strengthen uncertain claims.

If the service fails, state that the Agent Body rewrite did not complete. Never present a local fallback as a successful tool result or expose credentials and internal request metadata.
