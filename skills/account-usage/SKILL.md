---
name: account-usage
description: Check the current Agent Body account balance, API key quota, request totals, spending, and recent usage history. Use when a user asks about credits, balance, limits, billing usage, consumption, request history, or remaining capacity.
---

# Account Usage

Answer account and API-key usage questions through the Agent Body MCP server at `/mcp/account`.

Read [references/tool-reference.md](references/tool-reference.md) for exact inputs, defaults, filters, and result fields.

## Workflow

1. Choose the smallest sufficient tool:
   - Use `account_quota` for current balance and API-key capacity.
   - Use `usage_summary` for totals over a time range.
   - Use `usage_history` for recent itemized records.
2. For `usage_summary`, pass RFC 3339 `from` and `to` only when the user specifies a range. The service otherwise uses the most recent 30 days.
3. For `usage_history`, use only its supported filters. It does not accept a date range. Follow `nextCursor` only when more records are requested.
4. Read the business result from `data`. Distinguish available balance, reserved balance, spend limit, and actual charges.
5. Preserve USD precision and returned timestamps. Never estimate omitted values or merge null and zero.

## Failure handling

- Stop on authentication or permission errors and ask the user to check the MCP connection or API key.
- Treat an unchanged pagination cursor as completion to prevent a loop.
- State when no records match the filters or when only part of the requested history was read.

Never expose the API key, authorization header, opaque cursor contents, or account-private usage data outside the user's requested scope.
