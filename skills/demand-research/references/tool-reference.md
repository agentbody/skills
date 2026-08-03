# Demand Research Tool Reference

MCP server: `/demand-research/mcp`

Use the live MCP schema for exact fields. The stable lifecycle is create -> retrieve -> code evidence -> review.

## Tools

| Tool | Purpose | State to retain |
|---|---|---|
| `create-monitor` | Create a demand and purchase-intent research task | Monitor ID, audience, problem space, sources, window |
| `get-signals` | Retrieve pain-point, budget, alternative, and intent signals | Signal IDs, evidence, source, timestamp, cursor |
| `review-signals` | Record how demand signals were assessed or handled | Signal IDs, dispositions, review status |

## Coding rules

- Mark explicit statements as direct evidence.
- Mark themes inferred across multiple signals as interpretation.
- Mark absent information as unknown.
- Preserve contradictory and negative signals.
- Never label a person or company as ready to buy solely because a signal mentions a problem.
