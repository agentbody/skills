# Competitor Monitoring Tool Reference

MCP server: `/competitor-monitoring/mcp`

Use the live MCP schema for exact fields. Keep monitor configuration, retrieved evidence, and human review as separate states.

## Tools

| Tool | Purpose | State to retain |
|---|---|---|
| `create-monitor` | Create a competitor monitoring task | Monitor ID, competitor set, topics, sources, cadence |
| `get-signals` | Retrieve competitor updates, feedback, comparisons, and market response | Signal IDs, source, timestamp, cursor |
| `review-signals` | Record review of a competitive signal | Signal IDs, disposition, reviewer outcome/status |

## Evidence model

For each signal preserve the observed claim, source context, timestamp, competitor/topic, and any freshness or confidence metadata. Keep interpretations in a separate field or paragraph. Do not present a signal as a general market fact without describing its scope.
