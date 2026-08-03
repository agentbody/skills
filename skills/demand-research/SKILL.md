---
name: demand-research
description: Research customer pain points, budgets, alternatives, and buying intent through monitored demand signals. Use when a user wants to understand market demand, customer needs, purchase readiness, or reasons people choose competing solutions.
---

# Demand Research

Research demand signals through the Agent Body MCP server at `/demand-research/mcp`.

Read [references/tool-reference.md](references/tool-reference.md) for the monitor lifecycle and interpretation rules.

## Fixed workflow

### 1. Turn the question into a research brief

Specify the audience, product/category, problem space, geography, language, sources, time window, and the evidence types needed: pain points, budget clues, alternatives, or buying intent. Define exclusions and the minimum signal quality needed for a decision.

### 2. Create or reuse a monitor

- Reuse a matching monitor identifier when one is provided.
- Otherwise call `create-monitor` once after the brief is confirmed.
- Retain the monitor identifier, status, and requested window.
- Do not interpret monitor creation as evidence of demand.

### 3. Retrieve signals

Call `get-signals` for the monitor and requested period. Preserve source, timestamp, signal ID, pagination, and any confidence or relevance fields. Continue pagination only when the user requested complete coverage.

### 4. Code evidence into themes

For each signal, distinguish:

- **Direct evidence**: an explicit pain point, budget statement, alternative, or intent statement.
- **Interpretation**: a reasoned theme derived from one or more signals.
- **Unknown**: information not present in the evidence.

Group recurring themes, preserve outliers, and state sample or coverage limits. Never convert inferred intent into a confirmed purchase.

### 5. Review and report

Show a concise evidence table followed by themes, counter-signals, and open questions. Ask for dispositions when needed, then call `review-signals` to record confirmed review outcomes. Report reviewed, pending, and incomplete portions.

## Failure handling and safety

- Ask for a narrower audience or problem space when the research brief is too broad.
- Report empty, partial, stale, or conflicting evidence explicitly.
- Stop on permission or rate-limit errors and preserve the incomplete state.
- Respect privacy, source permissions, and applicable research or outreach rules.
