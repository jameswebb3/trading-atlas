# Coinversa Pulse MCP Server - Does an agent know when a market-data result was truncated or unavailable?

**Decision question:** Does an agent know when a market-data result was truncated or unavailable?

| Field | Review |
| --- | --- |
| Upstream | [Coinversaa/mcp-server](https://github.com/Coinversaa/mcp-server) |
| Primary area | Agents & Decision Systems |
| Source commit | [5fb2de8b08816cac9b3f32be6169ca4c95512ef3](https://github.com/Coinversaa/mcp-server/commit/5fb2de8b08816cac9b3f32be6169ca4c95512ef3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its capArray helper returns the displayed rows together with totalCount, truncated and an optional note; the data-coverage tool records unknown window starts as null and carries per-dataset notes rather than guessing dates. The MCP layer depends on a hosted API and key tier. Truncation metadata reports omission but does not restore the missing rows; an agent must page or narrow a query before drawing exhaustive conclusions. |

## What this project does

An MCP connector to a hosted Hyperliquid intelligence API, exposing wallet cohorts, trade history, book views and dataset coverage through agent tools.

## Mechanism inspected

Its capArray helper returns the displayed rows together with totalCount, truncated and an optional note; the data-coverage tool records unknown window starts as null and carries per-dataset notes rather than guessing dates.

## Limitation that matters

The MCP layer depends on a hosted API and key tier. Truncation metadata reports omission but does not restore the missing rows; an agent must page or narrow a query before drawing exhaustive conclusions.

## Practical check for a trading system

Return count, truncation, source window and freshness with every large research result, and require the agent to resolve partial coverage before asserting a complete market or wallet universe.

## Why this score

3/5. A concrete, reusable data-contract pattern addresses false completeness in trading research, though the upstream data service is not self-hosted.

## Source trail

[README](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/README.md#L1); [src/coinversaServer.ts](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/src/coinversaServer.ts#L116); [src/coinversaServer.ts](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/src/coinversaServer.ts#L381); [src/coinversaServer.ts](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/src/coinversaServer.ts#L384); [src/index.ts](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/src/index.ts#L9); [Root license](https://github.com/Coinversaa/mcp-server/blob/5fb2de8b08816cac9b3f32be6169ca4c95512ef3/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
