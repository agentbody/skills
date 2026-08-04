# Humanize Writing Tool Reference

MCP server: `/mcp/humanizer`

Tool ID: `humanizer.text`

MCP Tool: `humanizer_text`

REST: `POST /v1/tools/humanizer.text/call`

## Input

| Field | Type | Required | Rules |
|---|---|---:|---|
| `text` | string | Yes | 1-20,000 characters |
| `language` | string | No | Up to 35 characters; defaults to automatic detection |
| `mode` | string | No | `light`, `balanced`, or `strong`; defaults to `balanced` |

The schema does not accept `tone`, `audience`, `channel`, `length`, or arbitrary style fields.

## Output

Successful calls return:

```json
{"data":{"text":"<rewritten text>"}}
```

Before returning the text, compare names, numbers, dates, links, citations, negations, qualifications, language, headings, lists, and code blocks with the source.
