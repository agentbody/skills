# Humanize Writing Tool Reference

MCP server: `/humanizer/mcp`

Tool: `humanize_text`

The runtime MCP schema is authoritative for exact field names. The stable request contract supplied for this Skill is:

- `text`: source text to rewrite
- `language`: source or requested output language
- `tone`: desired voice

Optional audience, channel, length, or style controls may be used only when the live schema exposes them and the user supplied or approved them.

## Quality checklist

Before returning the result, compare the source and rewrite for:

- names, numbers, dates, links, citations, and product terminology;
- negations, legal qualifications, uncertainty, and scope;
- language and requested tone;
- headings, lists, code, and other intentional formatting.

When a source contains factual or legal claims, preserve them even if they make the prose less smooth. The tool improves expression; it does not fact-check or strengthen claims.
