# DennohPeter Hyperliquid — Reconnect needs a recovery source

**Decision question:** Will a WebSocket wrapper restore events missed while offline?

| Field | Review |
| --- | --- |
| Upstream | [dennohpeter/hyperliquid](https://github.com/dennohpeter/hyperliquid) |
| Primary area | Execution & Exchange Integration |
| Source commit | [712600db03693c4e154c7b1573970c012cf759a5](https://github.com/dennohpeter/hyperliquid/commit/712600db03693c4e154c7b1573970c012cf759a5) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The exchange client signs and sends orders with an optional client ID; the WebSocket client stores channel subscriptions. The reviewed connect and next paths do not establish backfill or fill reconciliation after the stream ends. |

## What this project does

A Rust Hyperliquid SDK with exchange and WebSocket clients. [Project README](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/README.md#L8).

## Mechanism inspected

The exchange client signs and sends orders with an optional client ID; the WebSocket client stores channel subscriptions. [Implementation](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/src/exchange.rs#L33). [Related source 1](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/TODO.md#L1). [Related source 2](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/src/websocket.rs#L21).

## Limitation that matters

The reviewed connect and next paths do not establish backfill or fill reconciliation after the stream ends. A subscription list is not a durable event log. This is a source review, not a runtime or security test.

## Practical check for a trading system

After reconnect, fetch venue orders and fills from a known overlap point before marking account state current.

## Why this score

The SDK offers useful method separation, but no demonstrated gap-recovery guarantee.

## Source trail

[README](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/README.md#L8); [Implementation](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/src/exchange.rs#L33); [Related source 1](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/TODO.md#L1); [Related source 2](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/src/websocket.rs#L21) - [License](https://github.com/dennohpeter/hyperliquid/blob/712600db03693c4e154c7b1573970c012cf759a5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
