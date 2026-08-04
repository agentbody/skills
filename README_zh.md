<div align="center">
  <h1>Agent Body</h1>
  <p><strong>Giving AI Agents a Body.</strong></p>
  <p>面向 Agent 时代的平台与企业，提供 Agent 所需的自研 Skills 和 MCP 服务。</p>
  <p>
    <a href="README.md">English</a> ·
    <a href="#安装-skills">Skills</a> ·
    <a href="#安装-mcp">MCP</a> ·
    <a href="#安装-rest-api">REST API</a>
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

可以选择一种或多种接入方式：Skill 用来教 AI Agent 如何使用能力，MCP 用来直接连接 Agent 客户端，REST API 则用于在应用代码中集成相同的 Tools。

### 安装 Skills

#### 安装全部 Skills

告诉你的 AI Agent：

> 安装全部 Agent Body Skills。Skill 源地址：[https://github.com/agentbody/skills](https://github.com/agentbody/skills)。安装后验证是否可用。

#### 安装单个 Skill

使用下表中的 Skill 源地址，例如：

> 安装 Agent Body 的 document-parsing Skill。Skill 源地址：[https://github.com/agentbody/skills/tree/main/skills/document-parsing](https://github.com/agentbody/skills/tree/main/skills/document-parsing)。安装后验证是否可用。

#### Skill 清单与使用示例

安装后的 Skill 通过 HTTPS `443` 端口调用 `api.agentbody.io` 上列出的 MCP endpoint。

| Skill 源 | MCP endpoint | 安装后的调用示例 |
|---|---|---|
| [account-usage](skills/account-usage/SKILL.md) | `/mcp/account` | “查询我的当前余额和 API Key 配额。” |
| [people-data](skills/people-data/SKILL.md) | `/mcp/people-data` | “查找这个 LinkedIn 资料对应的公开商务邮箱。” |
| [find-leads](skills/find-leads/SKILL.md) | `/mcp/find-leads` | “查找最近在 Reddit 寻找 CRM 替代方案的创业者。” |
| [competitor-monitoring](skills/competitor-monitoring/SKILL.md) | `/mcp/competitor-monitoring` | “调研近期客户对这个竞品的评价。” |
| [demand-research](skills/demand-research/SKILL.md) | `/mcp/demand-research` | “调研财务自动化的预算和购买意向信号。” |
| [document-parsing](skills/document-parsing/SKILL.md) | `/mcp/document-parsing` | “解析这个 PDF，并将第 1 到第 5 页输出为 Markdown。” |
| [humanize-writing](skills/humanize-writing/SKILL.md) | `/mcp/humanizer` | “在保留全部事实的前提下自然化改写这段文字。” |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | `/mcp/youtube-transcript` | “提取这个 YouTube 视频的英文字幕。” |
| [tiktok-transcript](skills/tiktok-transcript/SKILL.md) | `/mcp/tiktok-transcript` | “提取这个 TikTok 视频已有的字幕。” |

一个 MCP endpoint 对应一个 Skill。Skill 提供工作流，Tool 执行具体能力。

### 安装 MCP

所有 Agent Body MCP 服务都需要通过 [Agent Body Discord 社区](https://discord.gg/TxuDBzAYJr) 获取 API Key。获取后，将需要的服务添加到支持 Streamable HTTP MCP 的客户端。安装全部服务时使用：

生产主机：`api.agentbody.io`；传输协议：HTTPS；端口：`443`。

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

#### MCP endpoint 与调用示例

MCP 客户端通过 `tools/call` 调用 Tool，协议请求结构如下：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "account_quota",
    "arguments": {}
  }
}
```

| MCP endpoint | 全部可用 Tools | Tool 调用示例 |
|---|---|---|
| `/mcp/account` | `account_quota`, `usage_summary`, `usage_history` | `account_quota {}` |
| `/mcp/people-data` | `linkedin_email_lookup`, `linkedin_phone_lookup`, `linkedin_person_profile`, `linkedin_people_search`, `youtube_email_finder` | `linkedin_email_lookup {"profileUrl":"https://www.linkedin.com/in/example"}` |
| `/mcp/find-leads` | `find_leads_create_monitor`, `find_leads_get_signals`, `find_leads_review_signals` | `find_leads_create_monitor {"objective":"Find founders seeking CRM alternatives","until":"Collect 5 relevant signals","source":"reddit"}` |
| `/mcp/competitor-monitoring` | `competitor_monitoring_create_monitor`, `competitor_monitoring_get_signals`, `competitor_monitoring_review_signals` | `competitor_monitoring_create_monitor {"objective":"Research reactions to Acme CRM","until":"Collect 5 relevant signals","source":"reddit"}` |
| `/mcp/demand-research` | `demand_research_create_monitor`, `demand_research_get_signals`, `demand_research_review_signals` | `demand_research_create_monitor {"objective":"Research demand for accounting automation","until":"Collect 5 budget or intent signals","source":"reddit"}` |
| `/mcp/document-parsing` | `document_upload`, `document_parsing`, `document_result_get` | `document_upload {"fileName":"report.pdf","contentType":"application/pdf","sizeBytes":123456}` |
| `/mcp/humanizer` | `humanizer_text` | `humanizer_text {"text":"This is the text to rewrite.","mode":"balanced"}` |
| `/mcp/youtube-transcript` | `youtube_transcript` | `youtube_transcript {"url":"https://www.youtube.com/watch?v=VIDEO_ID","language":"en"}` |
| `/mcp/tiktok-transcript` | `tiktok_transcript`, `tiktok_audio_to_transcript` | `tiktok_transcript {"url":"https://www.tiktok.com/@example/video/VIDEO_ID","language":"en"}` |

每个 Skill 中的 Tool Reference 提供全部 Tool 的精确输入和输出。MCP 使用 `X-Idempotency-Key` 实现可选的请求幂等。成功调用将业务结果放在 `structuredContent.data`；业务失败设置 `isError: true` 并返回稳定的 `code`。

### 安装 REST API

REST 与 MCP 通过同一套鉴权、校验、计费和用量记录流程暴露相同的 Tools。查询当前 API Key 可见的 Tools：

生产 Base URL：`https://api.agentbody.io`（HTTPS `443` 端口）。

```bash
curl https://api.agentbody.io/v1/tools \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}"
```

使用 dotted Tool ID 调用 Tool：

```bash
curl -X POST https://api.agentbody.io/v1/tools/linkedin.email_lookup/call \
  -H "Authorization: Bearer ${AGENT_BODY_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: lookup-001" \
  --data '{"profileUrl":"https://www.linkedin.com/in/example"}'
```

REST 包含一个发现 endpoint 和 24 个具体 Tool 调用 endpoint。使用下表中的 JSON 请求体，并携带与上例相同的 Bearer 和 `Content-Type` 请求头。

| REST endpoint | JSON 请求体示例 |
|---|---|
| `GET /v1/tools` | 无请求体 |
| `POST /v1/tools/account.quota/call` | `{}` |
| `POST /v1/tools/usage.summary/call` | `{"from":"2026-08-01T00:00:00Z","to":"2026-08-05T00:00:00Z"}` |
| `POST /v1/tools/usage.history/call` | `{"limit":20,"status":"success"}` |
| `POST /v1/tools/linkedin.email_lookup/call` | `{"profileUrl":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.phone_lookup/call` | `{"profileUrl":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.person_profile/call` | `{"linkedin_url":"https://www.linkedin.com/in/example"}` |
| `POST /v1/tools/linkedin.people_search/call` | `{"jobTitle":["Founder"],"location":["Singapore"],"companyFilter":"current"}` |
| `POST /v1/tools/youtube.email_finder/call` | `{"channels":["https://www.youtube.com/@example"],"scrape_fresh_emails":false}` |
| `POST /v1/tools/find_leads.create_monitor/call` | `{"objective":"Find founders seeking CRM alternatives","until":"Collect 5 relevant signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/find_leads.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"CRM alternative for startup","strategy":"recent","time_window":"month"}],"limit":5}` |
| `POST /v1/tools/find_leads.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Explicit buying intent"}]}` |
| `POST /v1/tools/competitor_monitoring.create_monitor/call` | `{"objective":"Research reactions to Acme CRM","until":"Collect 5 relevant signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/competitor_monitoring.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"Acme CRM review","strategy":"recent","time_window":"month"}],"limit":5}` |
| `POST /v1/tools/competitor_monitoring.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Specific product feedback"}]}` |
| `POST /v1/tools/demand_research.create_monitor/call` | `{"objective":"Research demand for accounting automation","until":"Collect 5 budget or intent signals","source":"reddit","limits":{"target":5}}` |
| `POST /v1/tools/demand_research.get_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","search_queries":[{"source":"reddit","query":"accounting automation budget","strategy":"relevance","time_window":"quarter"}],"limit":5}` |
| `POST /v1/tools/demand_research.review_signals/call` | `{"monitor_id":"MONITOR_ID","monitor_token":"MONITOR_TOKEN","reviews":[{"lead_id":"LEAD_ID","verdict":"relevant","reason":"Contains a budget statement"}]}` |
| `POST /v1/tools/document.upload/call` | `{"fileName":"report.pdf","contentType":"application/pdf","sizeBytes":123456}` |
| `POST /v1/tools/document.parsing/call` | `{"uploadId":"550e8400-e29b-41d4-a716-446655440000"}` |
| `POST /v1/tools/document.result.get/call` | `{"documentId":"550e8400-e29b-41d4-a716-446655440000","pageStart":1,"pageEnd":10}` |
| `POST /v1/tools/humanizer.text/call` | `{"text":"This is the text to rewrite.","language":"en","mode":"balanced"}` |
| `POST /v1/tools/youtube.transcript/call` | `{"url":"https://www.youtube.com/watch?v=VIDEO_ID","language":"en"}` |
| `POST /v1/tools/tiktok.transcript/call` | `{"url":"https://www.tiktok.com/@example/video/VIDEO_ID","language":"en"}` |
| `POST /v1/tools/tiktok.audio_to_transcript/call` | `{"url":"https://www.tiktok.com/@example/video/VIDEO_ID"}` |

成功响应为 `{"data": {...}}`，错误响应为 `{"error":{"code":"...","message":"..."}}`。`Idempotency-Key` 是可选请求头，建议用于可能重试的调用。API Key 权限和运行时启用状态共同决定 `GET /v1/tools` 返回哪些 Tools。

## 贡献

- [贡献指南](CONTRIBUTING.md)
- [安全策略](SECURITY.md)
- [MIT License](LICENSE)
