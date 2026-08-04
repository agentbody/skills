---
name: demand-research
description: Research public customer pain points, budgets, alternatives, recommendations, workarounds, and buying intent in social content. Use when a user wants to understand market demand, unmet needs, purchase readiness, or reasons people consider competing solutions.
---

# Demand Research

Research demand signals through the Agent Body MCP server at `/mcp/demand-research`.

Read [references/tool-reference.md](references/tool-reference.md) for exact schemas, supported sources, and lifecycle state.

## Workflow

1. Define a focused `objective`, measurable `until` condition, and one supported `source`. Include the audience, category, problem, geography, language, and desired evidence types when relevant.
2. Call `demand_research_create_monitor` once. Retain the returned `monitor_id` and confidential `monitor_token`.
3. Supply explicit `search_queries` to `demand_research_get_signals`. Use supported strategies, time windows, and bounded retrieval controls.
4. Classify returned evidence as direct evidence, interpretation, or unknown. Preserve contradictions, negative evidence, source context, and coverage limits.
5. Call `demand_research_review_signals` only after a verdict is known. Use `next_round_guidance` to refine later queries.

The service does not expose scheduling cadence or an external pagination cursor. Continue through additional bounded retrieval rounds only while the returned progress supports it.

Protect `monitor_token`, respect source permissions and privacy, and never convert inferred interest into confirmed purchase intent.
