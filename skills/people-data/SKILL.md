---
name: people-data
description: Research professional profiles and public business contact data through LinkedIn and YouTube, including profile details, email, phone, people search, and channel business email lookup. Use when a user asks to identify, enrich, or find people, creators, or business contacts.
---

# People Data

Perform authorized people and public business-contact research through the Agent Body MCP server at `/mcp/people-data`.

Read [references/tool-reference.md](references/tool-reference.md) for exact Tool names and input fields.

## Workflow

1. Select one operation:
   - `linkedin_person_profile` for one professional profile.
   - `linkedin_email_lookup` for one profile's email.
   - `linkedin_phone_lookup` for one profile's phone number.
   - `linkedin_people_search` for filtered people discovery.
   - `youtube_email_finder` for public business emails from one or more channels.
2. Prefer a canonical profile or channel URL. For name-only searches, use explicit role, company, location, or keyword filters.
3. Use only fields exposed by the live schema. Note that profile lookup uses `linkedin_url`, while email and phone lookup use `profileUrl`.
4. Verify that returned identities match the request. Deduplicate search results by canonical profile identity when possible.
5. Present only returned contact data. Never construct or guess an email address or phone number.

## Safety

Use contact information only for an authorized business purpose. Do not infer sensitive traits, bypass access controls, expose credentials, or treat a missing result as evidence that a person has no contact information.
