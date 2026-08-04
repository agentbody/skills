<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>面向 Agent 时代的平台与企业，提供 Agent 所需的自研 Skills 和 MCP 服务。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#安装">安装</a> ·
    <a href="#连接-mcp">连接</a> ·
    <a href="#调用-rest-api">REST API</a> ·
    <a href="#可用-skills">Skills</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

所有能力均由 Agent Body 团队自主开发、严格测试并持续运营。平台无需自行筛选和维护质量不一的社区服务。

## 为什么选择 Agent Body

- **自主研发：** Skill 与后端服务均由我们自主开发。
- **稳定可靠：** 严格测试，持续维护。
- **统一接入：** 一次接入，快速扩展多种能力。
- **专属支持：** 为企业客户提供一对一接入服务。

## 安装

### 安装全部 Skills

告诉你的 AI Agent：

> 安装全部 Agent Body Skills。Skill 源地址：[https://github.com/agentbody/skills](https://github.com/agentbody/skills)。安装后验证是否可用。

### 可用 Skills

| Skill | MCP endpoint | 能力 |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp/account` | 查询账户余额、API Key 配额、用量汇总和用量记录 |
| [people-data](skills/people-data/SKILL.md) | `/mcp/people-data` | 查询职业资料和公开商务联系方式、搜索人员、查找 YouTube 频道邮箱 |
| [find-leads](skills/find-leads/SKILL.md) | `/mcp/find-leads` | 发现并审核潜在客户的公开信号 |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/mcp/competitor-monitoring` | 调研竞品动态、反馈、对比和市场反应 |
| [demand-research](skills/demand-research/SKILL.md) | `/mcp/demand-research` | 调研公开的痛点、预算、替代方案和购买意向 |
| [document-parsing](skills/document-parsing/SKILL.md) | `/mcp/document-parsing` | 上传并解析文档，输出 Markdown 和结构化内容 |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/mcp/humanizer` | 在保留原意和事实的前提下自然化改写文本 |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | `/mcp/youtube-transcript` | 提取 YouTube 已有字幕轨道中的文本 |
| [tiktok-transcript](skills/tiktok-transcript/SKILL.md) | `/mcp/tiktok-transcript` | 提取 TikTok 已有字幕或转写 TikTok 音频 |

一个 MCP endpoint 对应一个 Skill，工具是该 Skill 内部的能力。

### 安装单个 Skill

将 `document-parsing` 替换为需要安装的 Skill 名称，然后告诉你的 AI Agent：

> 安装 Agent Body 的 document-parsing Skill。Skill 源地址：[https://github.com/agentbody/skills/tree/main/skills/document-parsing](https://github.com/agentbody/skills/tree/main/skills/document-parsing)。安装后验证是否可用。

## 连接 MCP

将需要的服务添加到支持标准 MCP JSON 格式的客户端。接入全部 Agent Body 服务时使用：

所有 Agent Body MCP 服务都需要通过 [Agent Body Discord 社区](https://discord.gg/TxuDBzAYJr) 获取接入权限和凭证，请先加入社区。

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

将 `<AGENT_BODY_API_KEY>` 替换为社区提供的凭证，只保留需要接入的服务。凭证应保存在平台的密钥管理系统中，不能提交到 Skill 或 GitHub 仓库。`/mcp`、`/people-data/mcp`、`/humanizer/mcp` 等旧路径不再支持。

## 调用 REST API

REST 与 MCP 通过同一套鉴权、校验、计费和用量记录流程暴露相同的 Tools。查询当前 API Key 可见的 Tools：

```bash
curl https://api.agentbody.io/v1/tools \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}"
```

使用 dotted Tool ID 调用任意 Tool：

```bash
curl -X POST https://api.agentbody.io/v1/tools/linkedin.email_lookup/call \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: lookup-001" \
  --data '{"profileUrl":"https://www.linkedin.com/in/example"}'
```

成功响应为 `{"data": {...}}`，错误响应为 `{"error":{"code":"...","message":"..."}}`。`Idempotency-Key` 是可选请求头，建议用于可能重试的调用。每个 Skill 的 Tool Reference 都提供 REST dotted Tool ID、MCP Tool 名和精确输入合同之间的映射。

## 贡献

- [贡献指南](CONTRIBUTING.md)
- [安全策略](SECURITY.md)
- [MIT License](LICENSE)
