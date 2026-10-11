# Hyperliquid MCP Server — Read and write tools need different authority

**Decision question:** Should an assistant’s market-data channel also expose order placement?

| Field | Review |
| --- | --- |
| Upstream | [caiovicentino/hyperliquid-mcp-server](https://github.com/caiovicentino/hyperliquid-mcp-server) |
| Primary area | Execution & Exchange Integration |
| Source commit | [29c0786b3a4362bc75aed1d3ff5826a879dcaf26](https://github.com/caiovicentino/hyperliquid-mcp-server/commit/29c0786b3a4362bc75aed1d3ff5826a879dcaf26) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Its place_order tool accepts coin, side, size, price, TIF, reduce-only, and optional client ID in the same tool surface used for account reads. An assistant-facing interface with write credentials expands the execution boundary; a success flag from an SDK response is not a complete fill record. |

## What this project does

An MCP server that offers Hyperliquid market, account, and trading tools. [Project README](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/README.md#L47).

## Mechanism inspected

Its place_order tool accepts coin, side, size, price, TIF, reduce-only, and optional client ID in the same tool surface used for account reads. [Implementation](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/tools/trading_tools.py#L43). [Related source 1](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/tools/websocket_tools.py#L68).

## Limitation that matters

An assistant-facing interface with write credentials expands the execution boundary; a success flag from an SDK response is not a complete fill record. This is a source review, not a runtime or security test.

## Practical check for a trading system

Separate read-only research tools from a guarded order actuator with explicit authorization and reconciliation.

## Why this score

A direct interface-boundary case, but not a component to place in an autonomous trading path.

## Source trail

[README](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/README.md#L47); [Implementation](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/tools/trading_tools.py#L43); [Related source 1](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/tools/websocket_tools.py#L68) - [License](https://github.com/caiovicentino/hyperliquid-mcp-server/blob/29c0786b3a4362bc75aed1d3ff5826a879dcaf26/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
