# MaverickMCP — Do tool annotations enforce permission to change a portfolio

**Decision question:** Do tool annotations enforce permission to change a portfolio?

| Field | Review |
| --- | --- |
| Upstream | [MaverickMCP](https://github.com/wshobson/maverick-mcp) |
| Primary area | Agents & Decision Systems |
| Source commit | [fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1](https://github.com/wshobson/maverick-mcp/commit/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Provides explicit mutation annotations for agent-facing portfolio tools. Use them for client decisions, with separate authorization before exposing writable tools beyond a local personal workflow. |

## Project overview

A personal-use stock-analysis MCP server with market data, portfolio tools and a trade journal. [Project documentation](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/docs/runbooks/mcp-clients.md).

## Mechanism worth inspecting

The [portfolio tool module](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/maverick/portfolio/tools.py#L20-L43) distinguishes read, add, remove and clear annotations. [Registration](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/maverick/portfolio/tools.py#L386-L432) attaches these hints to individual tools; clearing also [requires a confirmation argument](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/maverick/portfolio/tools.py#L137-L147).

## Important limit

Tool hints and a confirmation boolean are not an authentication boundary. The [client runbook](https://github.com/wshobson/maverick-mcp/blob/fb55c84c9a9c8cc26b1d4aaf337e6fcc83cf7eb1/docs/runbooks/mcp-clients.md#L46-L56) explicitly describes the server as unauthenticated and personal-use.

## Questions to take into your own design

- Do tool annotations enforce permission to change a portfolio?
- Is write authorization checked independently of tool hints and confirmation arguments?

## Why this score for a trading system

2/5: concrete portfolio-tool classification, but hints and a caller-supplied boolean do not replace authorization.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
