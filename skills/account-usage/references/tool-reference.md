# Account Usage Tool Reference

MCP server: `/mcp`

The service runtime is the source of truth for exact input and output schemas. Use the tool schema exposed by the MCP connection; this document records the stable intent and handling rules only.

## Tools

| Tool | Use it for | Required context to collect |
|---|---|---|
| `account_quota` | Current balance, pre-authorized/reserved amount, and quota | Account/API-key scope if the client exposes more than one |
| `usage_summary` | Request totals, success/failure totals, and consumption for a period | Start, end, timezone, and any service-supported filters |
| `usage_history` | Itemized consumption records | Start, end, timezone, page/cursor intent, and any service-supported filters |

## Interpretation rules

- A quota snapshot is current-state data; do not describe it as historical spend.
- A reserved amount is not the same as consumed amount.
- A summary total is complete only when the service reports a complete result for the requested period.
- A history response may be paginated. Keep the cursor opaque and pass it back unchanged.
- Preserve null, unavailable, and zero as different states when the service distinguishes them.

## Safe response shape

```text
Scope: <account scope returned by the service>
Period: <period and timezone, or current snapshot>

Current capacity: <balance / reserved amount / quota, as available>
Usage: <requests / successes / failures / spend, as available>
Records: <count and page completeness>
Notes: <empty, partial, or unavailable fields>
```
