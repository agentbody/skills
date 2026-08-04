<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>Self-developed Skills and MCP services for platforms and enterprises in the agent era.</p>
  <p>
    <a href="README_zh.md">中文</a> ·
    <a href="#install">Install</a> ·
    <a href="#connect-mcp">Connect</a> ·
    <a href="#call-rest-api">REST API</a> ·
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
| [account-usage](skills/account-usage/SKILL.md) | `/mcp/account` | Check account balance, API key quota, usage summaries, and usage history |
| [people-data](skills/people-data/SKILL.md) | `/mcp/people-data` | Look up professional profiles and public business contact data, search people, and find YouTube channel emails |
| [find-leads](skills/find-leads/SKILL.md) | `/mcp/find-leads` | Discover and review public signals from potential customers |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/mcp/competitor-monitoring` | Research competitor updates, feedback, comparisons, and market response |
| [demand-research](skills/demand-research/SKILL.md) | `/mcp/demand-research` | Research public pain points, budgets, alternatives, and buying intent |
| [document-parsing](skills/document-parsing/SKILL.md) | `/mcp/document-parsing` | Upload and parse documents into Markdown and structured content |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/mcp/humanizer` | Rewrite text naturally while preserving meaning and facts |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | `/mcp/youtube-transcript` | Extract text from an existing YouTube subtitle track |
| [tiktok-transcript](skills/tiktok-transcript/SKILL.md) | `/mcp/tiktok-transcript` | Extract existing TikTok captions or transcribe TikTok audio |

One MCP endpoint is one Skill. Tools are capabilities inside that Skill.

### Install One Skill

Replace `document-parsing` with the Skill you want, then tell your AI agent:

> Install the Agent Body document-parsing Skill. Skill source: [https://github.com/agentbody/skills/tree/main/skills/document-parsing](https://github.com/agentbody/skills/tree/main/skills/document-parsing). Verify it works after installation.

## Connect MCP

Add the required services to a client that supports the standard MCP JSON format. To connect all Agent Body services, use:

Access to Agent Body MCP services is provided through the [Agent Body community on Discord](https://discord.gg/TxuDBzAYJr). Obtain your access credentials there before configuring a client.

```json
{
  "mcpServers": {
    "account": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/account",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "people-data": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/people-data",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "find-leads": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/find-leads",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "competitor-monitoring": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/competitor-monitoring",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "demand-research": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/demand-research",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "document-parsing": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/document-parsing",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "humanizer": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/humanizer",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "youtube-transcript": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/youtube-transcript",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "tiktok-transcript": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp/tiktok-transcript",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    }
  }
}
```

Replace `<AGENT_BODY_API_KEY>` with the credential provided by the community. Keep only the services you need. Store the credential in your platform's secret store and never commit it to a Skill or repository. Legacy paths such as `/mcp`, `/people-data/mcp`, and `/humanizer/mcp` are not supported.

## Call REST API

REST and MCP expose the same Tools through the same authorization, validation, billing, and usage pipeline. List the Tools visible to the current API key:

```bash
curl https://api.agentbody.io/v1/tools \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}"
```

Call any Tool by its dotted Tool ID:

```bash
curl -X POST https://api.agentbody.io/v1/tools/linkedin.email_lookup/call \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: lookup-001" \
  --data '{"profileUrl":"https://www.linkedin.com/in/example"}'
```

Successful calls return `{"data": {...}}`. Errors return `{"error":{"code":"...","message":"..."}}`. `Idempotency-Key` is optional but recommended for retryable calls. Each Skill's Tool Reference maps dotted REST Tool IDs to MCP Tool names and records the exact input contract.

## Contributing

- [Contributing guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [MIT License](LICENSE)
