<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>Self-developed Skills and MCP services for platforms and enterprises in the agent era.</p>
  <p>
    <a href="README_zh.md">中文</a> ·
    <a href="#install">Install</a> ·
    <a href="#connect">Connect</a> ·
    <a href="#available-skills">Skills</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

All capabilities are built, tested, and operated by Agent Body, so platforms do not have to evaluate and maintain inconsistent community services.

## Why Agent Body

- **Built in-house:** We develop every Skill and its backend service.
- **Reliable:** Thoroughly tested and continuously maintained.
- **One integration:** Add multiple capabilities through one connection.
- **Dedicated support:** One-on-one integration support for enterprise customers.

## Install

Install all Skills:

```bash
npx skills add agentbody/skills
```

Install one Skill:

```bash
npx skills add agentbody/skills --skill document-parsing
```

List available Skills:

```bash
npx skills add agentbody/skills --list
```

## Connect

Configure the MCP endpoint for the Skill you installed:

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

Keep API keys in your platform's secret store. Never commit them to a Skill or repository.

## Available Skills

One MCP endpoint is one Skill. Tools are capabilities inside that Skill.

| Skill | MCP endpoint | Capability |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | Quota, usage summaries, and request history |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | LinkedIn people data and YouTube business contacts |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | Potential customer and sales signals |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | Competitor updates and market response |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | Pain points, budgets, alternatives, and buying intent |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | Documents to Markdown and structured content |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | Natural writing that preserves meaning and facts |

## Local Documents

The `document-parsing` Skill can process files from the user's machine:

```text
document-upload -> upload local file -> document-parsing -> document-parsing-result
```

The client does not need an object-storage API key. The bundled [upload script](skills/document-parsing/scripts/upload_document.py) uses the short-lived URL returned by Agent Body.

## Skill Structure

```text
skills/<skill-name>/
├── SKILL.md          # Trigger and fixed workflow
├── references/       # Tool contracts
└── scripts/          # Optional local helpers
```

Only `SKILL.md` is required. Scripts and references are added when the Skill needs them.

## Contributing

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)
