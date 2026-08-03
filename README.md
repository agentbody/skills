<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>Self-developed Skills and MCP services for platforms and enterprises in the agent era.</p>
  <p>
    <a href="README_zh.md">中文</a> ·
    <a href="#install">Install</a> ·
    <a href="#connect-mcp">Connect</a> ·
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

### Install All Skills

Tell your AI agent:

> Install all Agent Body Skills. Skill source: [https://github.com/agentbody/skills](https://github.com/agentbody/skills). Verify they work after installation.

### Available Skills

| Skill | MCP endpoint | Capability |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | Account and usage management |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | Use AI to quickly find a person's public information and contact details |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | Find target customers across TikTok, YouTube, Reddit, Facebook, and professional websites |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | Research competitor conversations across TikTok, YouTube, Reddit, Facebook, and professional websites |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | Research pain points, budgets, alternatives, and buying intent across TikTok, YouTube, Reddit, Facebook, and professional websites |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | Parse 18 formats including DOC, PDF, scans, images, and XLSX; optimized for multi-page documents, long contracts, and high-quality Markdown output |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | Natural writing that preserves meaning and facts |

One MCP endpoint is one Skill. Tools are capabilities inside that Skill.

### Install One Skill

Replace `document-parsing` with the Skill you want, then tell your AI agent:

> Install the Agent Body document-parsing Skill. Skill source: [https://github.com/agentbody/skills/tree/main/skills/document-parsing](https://github.com/agentbody/skills/tree/main/skills/document-parsing). Verify it works after installation.

## Connect MCP

Add the required services to a client that supports the standard MCP JSON format. To connect all Agent Body services, use:

```json
{
  "mcpServers": {
    "account-usage": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "people-data": {
      "type": "http",
      "url": "https://api.agentbody.io/people-data/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "find-leads": {
      "type": "http",
      "url": "https://api.agentbody.io/find-leads/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "competitor-monitoring": {
      "type": "http",
      "url": "https://api.agentbody.io/competitor-monitoring/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "demand-research": {
      "type": "http",
      "url": "https://api.agentbody.io/demand-research/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "document-parsing": {
      "type": "http",
      "url": "https://api.agentbody.io/document-parsing/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "humanize-writing": {
      "type": "http",
      "url": "https://api.agentbody.io/humanizer/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    }
  }
}
```

Each MCP server name matches its Skill name. Keep only the services you need. Store the API key in your platform's secret store and never commit it to a Skill or repository.

## Contributing

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)
