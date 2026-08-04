# Find Leads Tool Reference

MCP server: `/mcp/find-leads`

| Tool ID | MCP Tool |
|---|---|
| `find_leads.create_monitor` | `find_leads_create_monitor` |
| `find_leads.get_signals` | `find_leads_get_signals` |
| `find_leads.review_signals` | `find_leads_review_signals` |

REST uses `POST /v1/tools/{tool_id}/call`.

The stable lifecycle is create -> retrieve -> review. Successful calls return the business result in `data`.

## Create monitor

`find_leads_create_monitor` requires `objective`, `until`, and one `source`. Supported sources are `twitter`, `reddit`, `youtube`, `tiktok`, `douyin`, and `xiaohongshu`.

Optional `limits` fields are `max_rounds` (1-10), `max_candidates` (1-500), and `target` (1-50). Retain the returned `monitor_id` and confidential `monitor_token`.

## Get signals

`find_leads_get_signals` requires:

- `monitor_id` and `monitor_token`.
- `search_queries`, an array of 1-50 objects containing required `source` and `query`.

Each query may include `query_id`, `strategy` (`relevance`, `recent`, `popular`, `most_discussed`), `time_window` (`all`, `hour`, `day`, `week`, `month`, `quarter`, `half_year`, `year`), and `content_kind`. The query source must match the source enabled for the monitor.

Optional call controls are `discussion_depth` (`content`, `comments`, `threads`), `page_budget` (1-10), and `limit` (1-20). Preserve `leads`, `progress`, `next_action`, and any returned `source_errors`.

## Review signals

`find_leads_review_signals` requires `monitor_id`, `monitor_token`, and `reviews`. Each review contains `lead_id`, `verdict` (`relevant`, `irrelevant`, `uncertain`), and optional `reason`. Optional `next_round_guidance` can refine later searches.
