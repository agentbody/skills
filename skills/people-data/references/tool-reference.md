# People Data Tool Reference

MCP server: `/people-data/mcp`

The runtime MCP schema is authoritative for exact fields. Never invent search filters, confidence fields, or contact-data keys that the service did not return.

## Tools

| Tool | Use it for | Preferred identifier or query |
|---|---|---|
| `linkedin-profile-lookup` | One LinkedIn profile | Canonical profile URL or stable profile identifier |
| `linkedin-email-lookup` | Email enrichment for one LinkedIn person | Canonical LinkedIn profile URL |
| `linkedin-phone-lookup` | Phone enrichment for one LinkedIn person | Canonical LinkedIn profile URL |
| `linkedin-people-search` | Search multiple people | Explicit role, company, location, keyword, and exclusion criteria |
| `youtube-email-finder` | A channel's business email | Channel URL or handle; name-only input requires disambiguation |

## Evidence and deduplication

- Treat canonical URLs, stable IDs, source labels, freshness, and verification flags as evidence metadata.
- Deduplicate search results by stable ID first, canonical URL second, and normalized name/company only as a last resort.
- Do not convert a missing verification flag into a verified claim.
- Do not merge two people merely because their names match.

## Safe response shape

```text
Identity: <name / channel and canonical source>
Role or channel context: <returned fields>
Requested contact data: <email / phone / business email, or Not found>
Evidence: <source, freshness, confidence, or verification returned by service>
```
