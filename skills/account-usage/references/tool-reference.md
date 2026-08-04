# Account Usage Tool Reference

MCP server: `/mcp/account`

Successful calls return the business result in `data`.

REST uses `POST /v1/tools/{tool_id}/call` with the dotted Tool ID shown below.

## `account_quota`

Tool ID: `account.quota`

Input: `{}`

Returns `balanceUsd`, `reservedUsd`, `availableUsd`, `keySpentUsd`, `keySpendLimitUsd`, and `keyRemainingUsd`. Limit and remaining values are null when the API key has no spend limit.

## `usage_summary`

Tool ID: `usage.summary`

Optional inputs:

| Field | Type | Rules |
|---|---|---|
| `from` | RFC 3339 string | Defaults to 30 days before the current time |
| `to` | RFC 3339 string | Defaults to the current time |

`from` must be earlier than `to`; the maximum range is 366 days. The result includes quota fields, the resolved range, request totals, `chargedUsd`, and breakdowns in `byProtocol` and `byService`.

## `usage_history`

Tool ID: `usage.history`

Optional inputs:

| Field | Type | Rules |
|---|---|---|
| `limit` | integer | 1-100; defaults to 20 |
| `cursor` | string | Return the previous `nextCursor` unchanged |
| `status` | string | `reserved`, `success`, `failed`, or `released` |
| `service` | string | Exact public service filter |
| `toolId` | string | Exact dotted Tool ID filter |

This tool does not accept `from` or `to`. Each record contains `requestId`, `protocol`, `service`, `tool`, `status`, `chargedUsd`, `durationMs`, `createdAt`, and `completedAt`. A response includes `nextCursor` only when another page exists.
