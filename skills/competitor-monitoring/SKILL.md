---
name: competitor-monitoring
description: Research competitor updates, feedback, comparisons, migrations, alternatives, and market response in public social content. Use when a user asks to gather competitive intelligence, study launches or reviews, retrieve competitor signals, or assess market reactions.
---

# Competitor Monitoring

Research competitor signals through the Agent Body MCP server at `/mcp/competitor-monitoring`.

Read [references/tool-reference.md](references/tool-reference.md) for exact schemas, supported sources, and lifecycle state.

## Workflow

1. Define a focused `objective`, measurable `until` condition, and one supported `source`. Include competitors, products, topics, exclusions, geography, or language in the objective when relevant.
2. Call `competitor_monitoring_create_monitor` once. Retain the returned `monitor_id` and confidential `monitor_token`.
3. Supply explicit `search_queries` to `competitor_monitoring_get_signals`. Use supported query strategies and bounded discussion/page controls.
4. Group results by competitor and topic while keeping every observation linked to returned evidence. Separate direct claims from interpretation and highlight conflicting or stale signals.
5. Call `competitor_monitoring_review_signals` only after a verdict is known. Provide `next_round_guidance` when the next research round needs a narrower or different query.

The service does not expose scheduling cadence or an external pagination cursor. Continue through additional bounded retrieval rounds only while the returned progress supports it.

Use authorized public information, protect `monitor_token`, and never present one signal as a universal market conclusion.
