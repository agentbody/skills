<div align="center">
  <h1>Agent Body Skills</h1>
  <p>面向 Agent 平台、Skill 平台和 MCP 平台，提供稳定、自研的企业级能力服务。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#安装">安装</a> ·
    <a href="#连接">连接</a> ·
    <a href="#可用-skills">Skills</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

Agent Body，为 Agent 提供与真实世界交互的能力。

我们提供标准化的 Skills 和 MCP 服务，让平台通过一次接入，快速扩展数据、研究、文档和写作能力。平台负责 Agent 体验，Agent Body 负责能力执行、认证、用量和计费服务。

## 为什么选择 Agent Body

- **稳定接入：** 一个 MCP endpoint 对应一个 Skill，工具和数据边界明确。
- **自研服务：** 每个 Skill 背后的能力由 Agent Body 构建和运营。
- **流程可控：** 每个 Skill 都定义触发条件、输入、固定流程、结果和异常处理。
- **面向平台：** 提供 API Key 认证、工具权限、额度、用量记录和服务端凭证保护。

## 安装

安装全部 Skills：

```bash
npx skills add agentbody/skills
```

安装单个 Skill：

```bash
npx skills add agentbody/skills --skill document-parsing
```

查看可用 Skills：

```bash
npx skills add agentbody/skills --list
```

## 连接

配置已安装 Skill 对应的 MCP endpoint：

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

API Key 应保存在平台的密钥管理系统中，不能提交到 Skill 或 GitHub 仓库。

## 可用 Skills

一个 MCP endpoint 对应一个 Skill，工具是该 Skill 内部的能力。

| Skill | MCP endpoint | 能力 |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | 额度、用量汇总和请求历史 |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | LinkedIn 人员数据和 YouTube 商务联系人 |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | 潜在客户和销售机会信号 |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | 竞品动态和市场反馈 |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | 痛点、预算、替代方案和购买意向 |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | 将文档转换为 Markdown 和结构化内容 |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | 保留原意和事实的自然化改写 |

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
