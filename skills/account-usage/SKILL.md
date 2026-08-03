---
name: account-usage
description: Inspect the current Agent Body API key's quota, reserved amount, request counts, success and failure totals, spend summaries, and paginated usage records. Use when a user asks about credits, limits, billing usage, consumption, request history, or remaining capacity.
---

# Account Usage

Answer account and API-key usage questions through the Agent Body MCP server at `/mcp`. Keep the user's account scope, time range, and timezone explicit in every response.

Read [references/tool-reference.md](references/tool-reference.md) when you need the complete tool map or detailed result-handling rules.

## Fixed workflow

### 1. Classify the request

Choose exactly one primary mode:

- **Quota snapshot**: current balance, reserved/pre-authorized amount, or quota. Use `account_quota`.
- **Usage summary**: totals over a period. Use `usage_summary`.
- **Usage history**: itemized consumption records. Use `usage_history`.
- **Combined report**: call `account_quota` plus one historical tool only when the user explicitly asks for both current capacity and past consumption.

Do not call all three tools by default.

### 2. Normalize the request

- For a summary or history request, identify start date, end date, and timezone.
- If the user omits the period, ask a concise clarification instead of silently choosing a range.
- For history, confirm whether the user wants the first page, a bounded number of records, or all pages in the requested range.
- Preserve the service's native currency, unit, precision, and timestamp format.

### 3. Call the MCP tool

Use the runtime MCP schema for exact input keys and pagination fields. Never invent parameter names. Retain the returned account scope, query range, cursor, and totals needed for the final response.

### 4. Validate and present the result

- Distinguish **available balance**, **reserved amount**, **quota**, and **actual consumption**; never merge them into one number.
- For summaries, show the period first, then total requests, successes, failures, and spend.
- For history, present a stable table with timestamp, operation/model if supplied, status, and cost/amount if supplied.
- Label values as unavailable when the service omits them. Do not estimate.

### 5. Handle pagination and completion

For `usage_history`, continue with the returned cursor only while the user requested more records and the service indicates another page. Report how many pages or records were read. Stop on an unchanged cursor to avoid an infinite loop.

## Failure handling

- **Authentication or permission error**: explain that the MCP connection or API key lacks access; do not retry blindly.
- **Invalid date range**: show the accepted range implied by the service error and ask for corrected dates.
- **Empty result**: say that no records matched the requested scope and period.
- **Partial page failure**: preserve successfully retrieved pages, identify the missing portion, and do not present totals as complete.

Never print the full API key, credentials, authorization headers, or internal request IDs unless the user explicitly needs a safe, non-secret support reference. Treat all usage and billing data as account-private.
