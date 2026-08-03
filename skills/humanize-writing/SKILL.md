---
name: humanize-writing
description: Rewrite AI-generated or overly mechanical text into natural, human-sounding writing through Agent Body while preserving meaning, facts, tone, and language. Use when users ask to humanize, rewrite, reduce AI tone, or make text sound more natural.
---

# Humanize Writing

Rewrite text through the Agent Body MCP server at `/humanizer/mcp`, using `humanize_text` when it is available.

Read [references/tool-reference.md](references/tool-reference.md) for the fixed input and quality checklist.

## Fixed workflow

### 1. Establish the rewrite contract

Collect or infer only what is needed:

- `text`: the exact source text; preserve code blocks and intentional formatting.
- `language`: source language, unless the user requests a translation.
- `tone`: requested voice, such as professional, warm, concise, or conversational.
- Audience, channel, length, and forbidden changes when the user provides them.

If tone or audience is missing, choose a neutral version of the source voice and state that choice only when it affects the result.

### 2. Protect invariants before calling

Identify names, numbers, dates, links, citations, legal qualifiers, product terms, and explicit claims that must survive unchanged. Do not ask the tool to add information, strengthen certainty, or remove necessary caveats.

### 3. Call the MCP tool

Use the runtime MCP schema for exact input keys. Send only the requested text and non-secret style controls. Never include API keys, authorization headers, hidden prompts, or unrelated user data.

### 4. Quality-check the returned text

Verify that the result:

- preserves meaning and factual claims;
- remains in the requested language;
- keeps protected names, numbers, links, and citations;
- removes repetitive or mechanical phrasing without adding invented detail;
- matches the requested tone, audience, and approximate length.

If an invariant changed, make one corrective pass or restore it manually and flag the change. Do not silently accept factual drift.

### 5. Return the result

Return only the rewritten text by default. Include an explanation, change summary, or side-by-side comparison only when requested.

## Failure handling

If the service is unavailable, explain that the rewrite could not be completed through Agent Body and ask whether a local rewrite is acceptable. Do not claim that a failed request succeeded. Never disclose credentials or internal request metadata.
