---
name: people-data
description: Research people and public business contact data through LinkedIn and YouTube, including profile details, email, phone, people search, and channel business email lookup. Use when a user asks to identify, enrich, or find people, creators, or business contacts.
---

# People Data

Perform authorized people and public business-contact research through the Agent Body MCP server at `/people-data/mcp`.

Read [references/tool-reference.md](references/tool-reference.md) for the tool map, input checklist, and evidence rules.

## Fixed workflow

### 1. Classify the request

Select one operation before calling a tool:

- **LinkedIn profile**: `linkedin-profile-lookup`.
- **LinkedIn email enrichment**: `linkedin-email-lookup`.
- **LinkedIn phone enrichment**: `linkedin-phone-lookup`.
- **LinkedIn people search**: `linkedin-people-search`.
- **YouTube business email**: `youtube-email-finder`.

If the user asks for several fields on one LinkedIn person, retrieve the profile first, then call only the requested enrichment tools.

### 2. Confirm identity and authorization

- Prefer a canonical LinkedIn profile URL, LinkedIn identifier, YouTube channel URL, or channel handle.
- For name-only searches, confirm company, role, geography, or other disambiguating criteria.
- Confirm the intended business purpose when requesting contact data, especially phone numbers.
- Do not infer sensitive characteristics from a profile or search result.

### 3. Build a precise query

Translate the request into explicit filters without adding assumptions. Preserve the user's spelling for names and companies, normalize obvious formatting differences, and record exclusions such as "current employees only" or "exclude agencies." Use the runtime MCP schema for exact field names.

### 4. Call and verify

- For a lookup, verify that the returned identity matches the requested person or channel before presenting contact data.
- For a search, inspect every returned result for relevance and deduplicate by canonical profile or channel identity when available.
- Treat confidence, source, freshness, and verification flags as evidence metadata, not as facts to recreate.
- If no result is returned, report no match; never guess an email or phone number.

### 5. Present a useful result

Use a compact table for multiple people. Include identity, role/company, location, requested contact fields, source context, and confidence/verification when supplied. For one person, summarize the identity first and contact fields second.

## Failure handling and privacy

- **Ambiguous identity**: ask for a URL or one additional discriminator.
- **Rate limit or permission error**: explain the connection issue and stop; do not rotate keys or bypass limits.
- **Partial enrichment**: show fields that were found and explicitly mark missing fields.
- **Stale or conflicting records**: preserve the conflict and cite the service's source/freshness metadata.

Use contact information only for a legitimate, authorized business purpose and in accordance with applicable privacy laws and platform terms. Never expose API keys, authorization headers, or internal service metadata.
