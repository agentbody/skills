---
name: competitor-monitoring
description: Monitor competitors for product updates, customer feedback, comparisons, and market reactions, then retrieve and review the resulting signals. Use when a user asks to track competitors, competitive intelligence, launches, reviews, or market response over time.
---

# Competitor Monitoring

Track competitive intelligence through the Agent Body MCP server at `/competitor-monitoring/mcp`.

Read [references/tool-reference.md](references/tool-reference.md) for the monitor lifecycle and evidence model.

## Fixed workflow

### 1. Define the monitoring brief

Capture the competitor names and canonical identifiers, products or features, topics, sources, geography, language, cadence, time window, and exclusions. Clarify whether the user wants launches, pricing, customer feedback, comparisons, market response, or all of them.

### 2. Create or reuse a monitor

- Reuse a monitor identifier supplied by the user when it matches the brief.
- Otherwise call `create-monitor` once after the scope is confirmed.
- Record the returned monitor identifier and status.
- Do not report monitor configuration as competitive evidence.

### 3. Retrieve and organize signals

Call `get-signals` for the requested period. Preserve cursors and source metadata. Group results by competitor, topic, and signal type, while keeping each claim linked to its underlying evidence and timestamp.

### 4. Analyze with evidence boundaries

Separate direct observations from interpretation. Label market reaction, customer sentiment, and comparison claims as reported signals rather than universal conclusions. Highlight conflicting or stale signals instead of averaging them away.

### 5. Review confirmed signals

Present a review queue with signal ID, evidence summary, competitor/topic, and proposed disposition. Call `review-signals` only after the user confirms or supplies the disposition. Report reviewed and pending counts.

## Failure handling and safety

- Ask for a competitor or topic when the request is too broad.
- Report empty results and partial pages explicitly.
- Stop on authentication, permission, or rate-limit errors; do not bypass controls.
- Avoid unsupported claims, private customer data, and confidential monitoring criteria.

Use authorized or publicly available information only. Never include credentials in monitor criteria or output.
