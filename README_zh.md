<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>面向 Agent 时代的平台与企业，提供 Agent 所需的自研 Skills 和 MCP 服务。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#安装">安装</a> ·
    <a href="#连接-mcp">连接</a> ·
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

> 安装全部 Agent Body Skills。Skill 源地址：https://github.com/agentbody/skills。安装后验证是否可用。

### 可用 Skills

| Skill | MCP endpoint | 能力 |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | 账户与用量管理 |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | 用 AI 快速查找目标人物的公开信息与联系方式 |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | 从 TikTok、YouTube、Reddit、Facebook 等社交媒体和专业网站中发现目标客户 |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | 从 TikTok、YouTube、Reddit、Facebook 等社交媒体和专业网站中调研竞品声音 |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | 从 TikTok、YouTube、Reddit、Facebook 等社交媒体和专业网站中调研痛点、预算、替代方案和购买意向 |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | 支持 DOC、PDF、扫描件、图片、XLSX 等 18 种格式，适用于多页文档和长篇合同，针对大模型优化并输出高质量 Markdown |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | 保留原意和事实的自然化改写 |

一个 MCP endpoint 对应一个 Skill，工具是该 Skill 内部的能力。

### 安装单个 Skill

将 `document-parsing` 替换为需要安装的 Skill 名称，然后告诉你的 AI Agent：

> 安装 Agent Body 的 document-parsing Skill。Skill 源地址：https://github.com/agentbody/skills/tree/main/skills/document-parsing。安装后验证是否可用。

## 连接 MCP

将需要的服务添加到支持标准 MCP JSON 格式的客户端。接入全部 Agent Body 服务时使用：

```json
{
  "mcpServers": {
    "agentbody-account-usage": {
      "type": "http",
      "url": "https://api.agentbody.io/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-people-data": {
      "type": "http",
      "url": "https://api.agentbody.io/people-data/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-find-leads": {
      "type": "http",
      "url": "https://api.agentbody.io/find-leads/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-competitor-monitoring": {
      "type": "http",
      "url": "https://api.agentbody.io/competitor-monitoring/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-demand-research": {
      "type": "http",
      "url": "https://api.agentbody.io/demand-research/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-document-parsing": {
      "type": "http",
      "url": "https://api.agentbody.io/document-parsing/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    },
    "agentbody-humanize-writing": {
      "type": "http",
      "url": "https://api.agentbody.io/humanizer/mcp",
      "headers": {
        "Authorization": "Bearer <AGENT_BODY_API_KEY>"
      }
    }
  }
}
```

只保留需要接入的服务。API Key 应保存在平台的密钥管理系统中，不能提交到 Skill 或 GitHub 仓库。

## 本地文档

`document-parsing` 可以处理用户 Agent 本地的文件：

```text
document-upload -> 上传本地文件 -> document-parsing -> document-parsing-result
```

客户端不需要对象存储 API Key。Skill 自带的[上传脚本](skills/document-parsing/scripts/upload_document.py)使用 Agent Body 返回的短期上传 URL。

## Skill 结构

```text
skills/<skill-name>/
├── SKILL.md          # 触发条件和固定流程
├── references/       # 工具契约
└── scripts/          # 可选本地辅助脚本
```

只有 `SKILL.md` 是必需文件，只有确有需要时才添加 references 和 scripts。

## 贡献

- [贡献指南](CONTRIBUTING.md)
- [安全策略](SECURITY.md)
- [MIT License](LICENSE)
