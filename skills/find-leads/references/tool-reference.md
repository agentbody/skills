# Find Leads Tool Reference

MCP server: `/find-leads/mcp`

Use the live MCP schema for exact input and output fields. The stable lifecycle is create -> retrieve -> review.

## Tools

| Tool | Purpose | State to retain |
|---|---|---|
| `create-monitor` | Create a potential-customer/sales-opportunity monitoring task | Monitor ID, status, scope, cadence |
| `get-signals` | Retrieve discovered potential-customer signals | Monitor ID, signal IDs, cursor, source/timestamp |
| `review-signals` | Record signal handling or review outcome | Signal IDs, disposition, review timestamp/status |

## Signal evidence

Keep the original signal text or evidence reference, source, timestamp, matched criterion, and confidence/priority when returned. Summaries must not replace the underlying evidence. A fetched signal is pending until a review outcome is recorded.

## Review queue shape

```text
Signal: <stable ID>
Why it matches: <matched criterion and evidence>
Source/time: <returned source metadata>
Suggested disposition: <relevant / irrelevant / duplicate / follow-up>
Review state: <pending until confirmed and recorded>
```
