---
name: find-leads
description: Find target customers, sales leads, prospects, and buying signals across TikTok, YouTube, Reddit, Facebook, social media, and professional websites through monitoring tasks. Use when a user wants to discover leads, monitor a market for prospects, collect sales opportunities, or review lead alerts over time.
---

# Find Leads

Discover and review potential customer signals through the Agent Body MCP server at `/find-leads/mcp`.

Read [references/tool-reference.md](references/tool-reference.md) for the monitor lifecycle, signal fields, and review rules.

## Fixed workflow

### 1. Write a monitor brief

Before calling a tool, turn the request into a short brief containing:

- target customer or buyer profile;
- industry, geography, language, and company-size boundaries;
- lead intent or event to detect;
- keywords, sources, timing/cadence, and exclusions;
- desired signal freshness and review cadence.

Ask for the missing boundary that would materially change the result. Do not create an open-ended monitor by default.

### 2. Create or select the monitor

- If the user provides an existing monitor identifier, use it and do not create a duplicate.
- Otherwise call `create-monitor` once with the approved brief.
- Store the returned monitor identifier, status, and creation details for all later calls.
- Never treat a monitor creation response as proof that a lead already exists.

### 3. Retrieve signals

Call `get-signals` for the monitor and requested time window. Preserve the service's pagination or cursor exactly. For each signal, capture the evidence, timestamp, source, matched criteria, and any confidence or priority returned.

### 4. Triage without inventing evidence

Classify each signal as relevant, irrelevant, duplicate, needs-review, or ready-for-action only when the returned evidence supports it. Separate observed text from the agent's interpretation. Deduplicate by the service's stable signal ID when available.

### 5. Review and close the loop

Ask for the user's disposition when it is not already specified. Call `review-signals` with the runtime schema to record confirmed outcomes. Do not mark a signal reviewed merely because it was fetched. Report the number of reviewed, pending, and skipped signals.

## Failure handling and safety

- **Missing scope**: ask for target market or signal criteria before creating a monitor.
- **Duplicate monitor**: reuse the existing identifier when the brief matches; do not silently create another.
- **Empty results**: report that no matching signals were found for the period.
- **Partial retrieval**: state which pages or time range were not completed.
- **Permission/rate limit**: stop and explain the service error; never bypass it.

Do not fabricate leads, contact details, or evidence. Respect source permissions, privacy requirements, and applicable outreach laws.
