<div align="center">
  <h1>Agent Body Skills</h1>
  <p>Agent Body，为 Agent 提供与真实世界交互的能力。</p>
  <p>面向 Agent 平台、Skill 平台和 MCP 平台，提供稳定、自研、可持续运营的企业级能力服务。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#安装">安装</a> ·
    <a href="#连接-agent-body">连接</a> ·
    <a href="#可用-skills">Skills</a>
  </p>
  <p>
    <a href="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml"><img src="https://github.com/agentbody/skills/actions/workflows/validate-skills.yml/badge.svg" alt="Validate Skills"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  </p>
</div>

Agent Body，为 Agent 提供与真实世界交互的能力。

我们面向 Agent 平台、Skill 平台和 MCP 平台，提供稳定、自研、可持续运营的企业级能力服务。Agent 平台不应该为每一种数据、研究和文档能力重复建设底层服务基础设施。

Agent Body 提供标准化的 Skills 和 MCP 服务，让企业客户通过统一的接入方式，快速扩展 Agent 能力，并将能力执行、认证边界、用量和服务运营交给 Agent Body。

> 安装 Skill，连接 Agent Body MCP，然后让 Skill 提供固定流程，让 Agent Body 执行具体服务。

## 面向平台团队

接入 Agent Body 后，平台可以获得清晰的服务边界和可复用的 Agent 能力契约：

| 平台关心的问题 | Agent Body 提供什么 |
|---|---|
| 快速增加能力 | 可直接安装的 Skill 和按 endpoint 划分的 MCP 服务，不需要为每项能力单独开发适配器 |
| 保持 Agent 行为稳定 | 清晰触发条件、固定流程、输入校验、结果处理和明确的失败状态 |
| 可控地运营 | API Key 认证、工具 allowlist、额度和用量可见性、计费边界以及 Key 范围的数据结果 |
| 降低平台风险 | 服务凭证留在服务端；公开响应只暴露业务结果，不透传上游原始响应 |
| 持续演进而不碎片化 | 统一的 `skills/` 源目录、版本化文档，以及每个 Skill 的 CI 校验 |

Agent Body 将面向 Agent 的契约与服务执行层分离：平台接入标准契约，Agent Body 负责其后的认证服务链路和服务运营。

### 责任边界

| 层级 | 负责内容 |
|---|---|
| 你的平台 | Agent 体验、Skill 安装、MCP 客户端配置，以及产品自己的用户权限 |
| Agent Body | 自研服务执行、MCP 工具契约、认证边界、用量与计费记录，以及服务端凭证 |
| Skill | 触发条件、固定操作流程、输入准备、结果解释和安全规则 |

这种边界让平台可以增加能力，而不需要复制供应商凭证、MCP 实现细节或服务专属流程。

### 稳定性设计

- 按产品能力隔离 MCP endpoint，让工具和数据边界保持明确。
- 输入 Schema、工具名称、Skill 元数据和结果投影都会进入仓库校验流程。
- 服务链路包含账户范围认证、工具 allowlist、用量记录和受控的结果范围读取。
- 服务失败以受控错误状态返回；客户端不会接触上游凭证和原始服务商响应。

可用性目标、数据驻留、保留周期和合同 SLA 取决于具体 Agent Body 部署和服务协议，应针对你的环境确认，不能仅从本目录推断。

## 快速了解

| 你需要做什么 | 使用这个 Skill |
|---|---|
| 查询额度、消费和请求历史 | [account-usage](skills/account-usage/SKILL.md) |
| 研究 LinkedIn 人员或 YouTube 商务联系人 | [people-data](skills/people-data/SKILL.md) |
| 发现并审核潜在客户信号 | [find-leads](skills/find-leads/SKILL.md) |
| 追踪竞品动态和市场反馈 | [competitor-monitoring](skills/competitor-monitoring/SKILL.md) |
| 研究痛点、预算、替代方案和购买意向 | [demand-research](skills/demand-research/SKILL.md) |
| 将文档转换为 Markdown 和结构化内容 | [document-parsing](skills/document-parsing/SKILL.md) |
| 在不改变事实的前提下让文字更自然 | [humanize-writing](skills/humanize-writing/SKILL.md) |

## 安装

安装完整的 Agent Body Skills 目录：

```bash
npx skills add agentbody/skills
```

只安装一个 Skill：

```bash
npx skills add agentbody/skills --skill document-parsing
```

安装到指定 Agent，并启用全局范围：

```bash
npx skills add agentbody/skills \
  --skill document-parsing \
  --agent codex \
  --global
```

查看可用 Skills：

```bash
npx skills add agentbody/skills --list
```

Skills CLI 会把标准源目录安装到目标 Agent 的约定位置。本仓库只维护 `skills/` 这一份源代码，不重复维护 `.claude/skills/`、`.agents/skills/` 或 `.codex/`。

## 快速开始

### 1. 安装 Skill

```bash
npx skills add agentbody/skills --skill people-data
```

### 2. 连接 Agent Body

在 MCP 客户端中配置 Agent Body API Key，以及你安装的 Skill 对应的 MCP endpoint：

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

请根据[可用 Skills](#可用-skills)替换 endpoint 路径。API Key 应保存在 Agent 或部署环境的密钥管理系统中，不能提交到 Skill 或 GitHub 仓库。

### 3. 直接向 Agent 提出任务

```text
搜索新加坡金融科技公司的市场负责人，并返回 LinkedIn 资料。
创建一个监控，寻找正在寻找文档自动化方案的公司。
解析这个 PDF，并返回第 4 到第 6 页的表格。
把这段公告改写得更自然、更专业。
```

## 可用 Skills

一个 MCP endpoint 对应一个 Skill。下表中的工具是 Skill 内部的能力，不是独立 Skill。

| Skill | MCP endpoint | 工具 | 适用场景 |
|---|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp` | `account_quota`、`usage_summary`、`usage_history` | 额度、消费和请求历史 |
| [people-data](skills/people-data/SKILL.md) | `/people-data/mcp` | `linkedin-profile-lookup`、`linkedin-email-lookup`、`linkedin-phone-lookup`、`linkedin-people-search`、`youtube-email-finder` | 人员研究和商务联系人补充 |
| [find-leads](skills/find-leads/SKILL.md) | `/find-leads/mcp` | `create-monitor`、`get-signals`、`review-signals` | 潜在客户和销售机会信号 |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/competitor-monitoring/mcp` | `create-monitor`、`get-signals`、`review-signals` | 竞品动态、反馈、对比和市场反应 |
| [demand-research](skills/demand-research/SKILL.md) | `/demand-research/mcp` | `create-monitor`、`get-signals`、`review-signals` | 痛点、预算、替代方案和购买意向 |
| [document-parsing](skills/document-parsing/SKILL.md) | `/document-parsing/mcp` | `document-upload`、`document-parsing`、`document-parsing-result` | Markdown、结构化抽取、页面范围和本地文件 |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/humanizer/mcp` | `humanize_text` | 保留事实和原意的自然化改写 |

## 本地文档

`document-parsing` 支持用户 Agent 本地的文件：

```text
document-upload
  -> 获取短期有效的上传 URL
  -> 使用 Skill 自带脚本上传本地文件字节
  -> document-parsing(uploadId)
  -> document-parsing-result(documentId, range)
```

客户端不需要对象存储 API Key。Agent Body API Key 用于创建上传会话，临时上传 URL 只授权本次文件上传。详见 [document-parsing](skills/document-parsing/SKILL.md) 和经过测试的 [upload_document.py](skills/document-parsing/scripts/upload_document.py)。

## Skill 如何工作

每个 Skill 都有一个标准入口：

```text
skills/<skill-name>/
├── SKILL.md                 # 触发元数据和固定 Agent 流程
├── references/              # 详细工具契约和领域说明
└── scripts/                 # 可选的确定性本地辅助脚本
```

`SKILL.md` 说明什么时候使用能力、选择哪个 MCP 工具、如何校验输入和组织结果。Agent Body MCP 服务负责远程执行；认证和服务配置属于客户端连接，不写入 Skill 文件。

## 常见问题

<details>
<summary><strong>每个 MCP 工具都是一个独立 Skill 吗？</strong></summary>

不是。一个 MCP endpoint 对应一个 Skill。例如 `/people-data/mcp` 是 `people-data` Skill，内部包含 5 个相关工具。
</details>

<details>
<summary><strong>每个 Skill 都需要 scripts 目录吗？</strong></summary>

不需要。`scripts/` 是可选的，只有存在真实且经过测试的本地辅助逻辑时才添加。大多数 Agent Body 能力完全通过 MCP 运行；`document-parsing` 需要脚本，是因为本地文件必须被上传到临时 URL。
</details>

<details>
<summary><strong>需要对象存储 API Key 吗？</strong></summary>

不需要。客户端只需要 Agent Body API Key。对象存储凭证保留在 Agent Body 服务端，本地上传使用 `document-upload` 返回的短期 URL。
</details>

<details>
<summary><strong>详细的输入和输出规则在哪里？</strong></summary>

打开对应 Skill 的 `SKILL.md`。更详细的工具映射和结果规则位于该 Skill 的 `references/` 目录。具体字段以运行时 MCP Schema 为准。
</details>

## 仓库结构

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

每个 Skill 目录使用小写字母、数字和连字符，并且必须与 `SKILL.md` frontmatter 中的 `name` 完全一致。只有直接支持 Skill 的可选目录才应被添加。

## 贡献与安全

- Skill 格式和 Pull Request： [CONTRIBUTING.md](CONTRIBUTING.md)
- 漏洞报告： [SECURITY.md](SECURITY.md)
- 许可证： [MIT](LICENSE)

校验 workflow 会在每次 push 和 pull request 时检查 Skill 元数据、目录名、必需文件和 frontmatter 一致性。
