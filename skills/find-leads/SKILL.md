---
name: find-leads
description: Find potential customers, prospects, and buying signals in public social content through scoped research monitors. Use when a user wants to discover leads, collect sales opportunities, retrieve prospect signals, or review lead evidence.
---

# Find Leads

Discover and review potential-customer signals through the Agent Body MCP server at `/mcp/find-leads`.

Read [references/tool-reference.md](references/tool-reference.md) for exact schemas, supported sources, and lifecycle state.

## Workflow

1. Define a concrete research `objective`, measurable `until` condition, and one supported `source`.
2. Call `find_leads_create_monitor` once. Retain the returned `monitor_id` and `monitor_token`; both are required for later calls.
3. Build explicit `search_queries` for the monitor's source, then call `find_leads_get_signals`. Adjust query strategy, time window, discussion depth, page budget, or limit only through supported fields.
4. Preserve each returned lead's evidence and source context. Separate observed content from interpretation and deduplicate by stable lead identity.
5. Call `find_leads_review_signals` only after a verdict is known. Use `next_round_guidance` to improve the next retrieval round when appropriate.

The service does not expose a scheduling cadence or external pagination cursor. Continue by making another bounded `get_signals` call with revised or repeated search queries while the returned progress indicates more work is useful.

Never fabricate leads or contact details. Treat `monitor_token` as confidential, respect source permissions and privacy requirements, and stop on authentication or permission errors.
