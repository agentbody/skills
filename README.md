<div align="center">
  <h1>Agent Body Skills</h1>
  <p>Agent Body gives agents the ability to interact with the real world.</p>
  <p>Stable, self-developed, continuously operated enterprise capabilities for agent platforms, Skill platforms, and MCP platforms.</p>
  <p>
    <a href="README_zh.md">中文</a> ·
    <a href="#install">Install</a> ·
    <a href="#connect-to-agent-body">Connect</a> ·
    <a href="#available-skills">Skills</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

Agent Body gives agents the ability to interact with the real world.

We provide stable, self-developed, continuously operated enterprise capabilities for agent platforms, Skill platforms, and MCP platforms. Agent platforms should not have to rebuild service infrastructure for every data, research, or document capability.

Agent Body provides standardized Skills and MCP services so enterprise customers can expand agent capabilities through one consistent integration model, while Agent Body operates the capability execution, authentication boundary, usage, and service layer.

> Install the Skills once. Connect your agent to Agent Body MCP. Let each Skill provide the workflow and let Agent Body perform the service call.

## For Platform Teams

When you integrate Agent Body, your platform gets a clear service boundary and a reusable agent-facing contract:

| Platform concern | What Agent Body provides |
|---|---|
| Add capabilities quickly | Ready-to-install Skills and endpoint-specific MCP services instead of one custom adapter per capability |
| Keep agent behavior predictable | Clear triggers, fixed workflows, input checks, result handling, and explicit failure states |
| Operate with control | API-key authentication, tool allowlists, quota and usage visibility, billing boundaries, and scoped results |
| Protect your platform | Service credentials stay server-side; public responses are projected to business data rather than raw upstream payloads |
| Evolve without fragmentation | One standard `skills/` source tree, version-controlled documentation, and CI validation for every Skill |

Agent Body separates the agent-facing contract from service execution. Your platform integrates the contract; Agent Body operates the authenticated service path behind it.

### Responsibility Boundaries

| Layer | Owns |
|---|---|
| Your platform | Agent experience, Skill installation, MCP client configuration, and your product's user permissions |
| Agent Body | Self-developed service execution, MCP tool contracts, authentication boundary, usage and billing records, and service-side credentials |
| The Skill | Trigger conditions, fixed operating procedure, input preparation, result interpretation, and safety rules |

This separation lets a platform add capabilities without copying provider credentials, MCP implementation details, or service-specific workflows into its own product.

### Reliability By Design

- Public MCP endpoints are separated by product capability, so tools and data boundaries stay explicit.
- Input schemas, tool names, Skill metadata, and result projections are validated as part of the repository workflow.
- Account-scoped authentication, allowlists, usage records, and bounded result reads are part of the service path.
- Service failures are returned as controlled error states; upstream credentials and raw provider responses are not exposed to clients.

Availability targets, data residency, retention, and contractual SLAs depend on the Agent Body deployment and service agreement. They should be confirmed for your environment rather than inferred from this catalog.

## At A Glance

| You need to... | Use this Skill |
|---|---|
| Check quota, spend, or request history | [account-usage](skills/account-usage/SKILL.md) |
| Research LinkedIn people or YouTube business contacts | [people-data](skills/people-data/SKILL.md) |
| Find and review potential customer signals | [find-leads](skills/find-leads/SKILL.md) |
| Track competitor updates and market response | [competitor-monitoring](skills/competitor-monitoring/SKILL.md) |
| Research pain points, budgets, alternatives, and buying intent | [demand-research](skills/demand-research/SKILL.md) |
| Convert documents into Markdown and structured content | [document-parsing](skills/document-parsing/SKILL.md) |
| Make writing sound natural without changing facts | [humanize-writing](skills/humanize-writing/SKILL.md) |

## Install

Install the complete Agent Body Skills catalog:

```bash
npx skills add agentbody/skills
```

Install one Skill:

```bash
npx skills add agentbody/skills --skill document-parsing
```

Install for a specific agent and make it global:

```bash
npx skills add agentbody/skills \
  --skill document-parsing \
  --agent codex \
  --global
```

List available Skills:

```bash
npx skills add agentbody/skills --list
```

The Skills CLI places the standard source in the target agent's expected location. This repository intentionally maintains one source tree under `skills/`; it does not duplicate Skills under `.claude/skills/`, `.agents/skills/`, or `.codex/`.

## Quick Start

### 1. Install a Skill

```bash
npx skills add agentbody/skills --skill people-data
```

### 2. Connect Agent Body MCP

Configure your MCP client with an Agent Body API key and the endpoint for the Skill you installed:

```json
{
  "mcpServers": {
    "agentbody-people-data": {
      "type": "http",
      "url": "https://api.agentbody.io/people-data/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    }
  }
}
```

Replace the endpoint path with the one listed in [Available Skills](#available-skills). Keep the API key in your agent or deployment secret store; never commit it to a Skill or repository.

### 3. Ask Your Agent

Examples:

```text
Find people on LinkedIn who are heads of marketing at fintech companies in Singapore.
Create a lead monitor for companies looking for document automation.
Parse this PDF and give me the tables from pages 4 to 6.
Rewrite this announcement to sound natural and professional.
```

## Available Skills

One MCP endpoint maps to one Skill. The tools listed in the last column are capabilities inside that Skill, not separate Skills.

| Skill | MCP endpoint | Tools | Best for |
|---|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | `account_quota`, `usage_summary`, `usage_history` | Quota, billing usage, and request history |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | `linkedin-profile-lookup`, `linkedin-email-lookup`, `linkedin-phone-lookup`, `linkedin-people-search`, `youtube-email-finder` | People research and business contact enrichment |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | `create-monitor`, `get-signals`, `review-signals` | Potential customer and sales-opportunity signals |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | `create-monitor`, `get-signals`, `review-signals` | Competitor updates, feedback, comparisons, and market response |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | `create-monitor`, `get-signals`, `review-signals` | Pain points, budgets, alternatives, and buying intent |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | `document-upload`, `document-parsing`, `document-parsing-result` | Markdown, structured extraction, page ranges, and local files |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | `humanize_text` | Natural rewrites that preserve meaning and facts |

## Local Documents

The `document-parsing` Skill supports files on the user's local machine:

```text
document-upload
  -> receive a short-lived upload URL
  -> upload local bytes with the bundled helper script
  -> document-parsing(uploadId)
  -> document-parsing-result(documentId, range)
```

The client does not need an object-storage API key. The Agent Body API key authorizes the upload session; the temporary upload URL authorizes the single file upload. See [document-parsing](skills/document-parsing/SKILL.md) for the fixed workflow and [upload_document.py](skills/document-parsing/scripts/upload_document.py) for the tested upload bridge.

## How Skills Work

Each Skill has a small, standard entrypoint:

```text
skills/<skill-name>/
├── SKILL.md                 # Triggering metadata and fixed agent workflow
├── references/              # Detailed tool contracts and domain notes
└── scripts/                 # Optional deterministic local helpers
```

`SKILL.md` tells an agent when to use the capability, which MCP tool to select, how to validate inputs, and how to present results. Agent Body MCP services perform the remote work. Authentication and service configuration belong to the client connection, not to the Skill files.

## FAQ

<details>
<summary><strong>Is each MCP tool a separate Skill?</strong></summary>

No. One MCP endpoint is one Skill. For example, `/people-data/mcp` is the `people-data` Skill and contains five related tools.
</details>

<details>
<summary><strong>Do all Skills need a scripts directory?</strong></summary>

No. `scripts/` is optional and should only contain a real, tested local helper. Most Agent Body capabilities run entirely through MCP. `document-parsing` includes a script because a local file must be streamed to the temporary upload URL.
</details>

<details>
<summary><strong>Do I need an object-storage API key?</strong></summary>

No. Clients need an Agent Body API key for MCP access. Object-storage credentials stay on the Agent Body service; local uploads use a short-lived URL returned by `document-upload`.
</details>

<details>
<summary><strong>Where do I find detailed input and output rules?</strong></summary>

Open the Skill's `SKILL.md`. Detailed tool mappings and result rules are in its `references/` directory. The live MCP tool schema remains authoritative for exact fields.
</details>

## Repository Layout

```text
.
├── README.md
├── README_zh.md
├── LICENSE
├── CONTRIBUTING.md
├── SECURITY.md
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── references/
│       └── scripts/
└── .github/
    └── workflows/
        └── validate-skills.yml
```

Every Skill directory uses lowercase letters, digits, and hyphens, and exactly matches the `name` in its `SKILL.md` frontmatter. Optional directories are added only when they support the Skill directly.

## Contributing And Security

- Skill format and pull requests: [CONTRIBUTING.md](CONTRIBUTING.md)
- Vulnerability reporting: [SECURITY.md](SECURITY.md)
- License: [MIT](LICENSE)

The validation workflow checks Skill metadata, directory names, required files, and frontmatter consistency on every push and pull request.
