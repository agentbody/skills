# Competitor Monitoring Tool Reference

MCP server: `/mcp/competitor-monitoring`

| Tool ID | MCP Tool |
|---|---|
| `competitor_monitoring.create_monitor` | `competitor_monitoring_create_monitor` |
| `competitor_monitoring.get_signals` | `competitor_monitoring_get_signals` |
| `competitor_monitoring.review_signals` | `competitor_monitoring_review_signals` |

REST uses `POST /v1/tools/{tool_id}/call`.

The stable lifecycle is create -> retrieve -> review. Successful calls return the business result in `data`.

## Create monitor

`competitor_monitoring_create_monitor` requires `objective`, `until`, and one `source`. Supported sources are `twitter`, `reddit`, `youtube`, `tiktok`, `douyin`, and `xiaohongshu`.

Optional `limits` fields are `max_rounds` (1-10), `max_candidates` (1-500), and `target` (1-50). Retain the returned `monitor_id` and confidential `monitor_token`.

## Get signals

`competitor_monitoring_get_signals` requires `monitor_id`, `monitor_token`, and 1-50 `search_queries`. Every query requires `source` and `query`; it may also contain `query_id`, `strategy`, `time_window`, and `content_kind`.

Strategies: `relevance`, `recent`, `popular`, `most_discussed`.

Time windows: `all`, `hour`, `day`, `week`, `month`, `quarter`, `half_year`, `year`.

Optional call controls are `discussion_depth` (`content`, `comments`, `threads`), `page_budget` (1-10), and `limit` (1-20). Preserve evidence, `progress`, `next_action`, and any `source_errors`.

## Review signals

`competitor_monitoring_review_signals` requires `monitor_id`, `monitor_token`, and `reviews`. Each review contains `lead_id`, `verdict` (`relevant`, `irrelevant`, `uncertain`), and optional `reason`. Optional `next_round_guidance` can refine later searches.
