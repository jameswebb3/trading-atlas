# hyperliquid-tracker - What happens when a Hyperliquid trade-stream callback fails?

**Decision question:** What happens when a Hyperliquid trade-stream callback fails?

| Field | Review |
| --- | --- |
| Upstream | [0xhype/hyperliquid-tracker](https://github.com/0xhype/hyperliquid-tracker) |
| Primary area | Operations & Observability |
| Source commit | [5dda9a1aaa6be32178f041db0baa3a372acec160](https://github.com/0xhype/hyperliquid-tracker/commit/5dda9a1aaa6be32178f041db0baa3a372acec160) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | It filters WS trades by price times size and reconnects with increasing delay after close. Its detached processTrade rejection and WebSocket error handlers throw inside callbacks; no source gap or missed-trade recovery is shown. |

## What this project does

A Hyperliquid trade monitor with a notional threshold and Telegram notifications.

## Mechanism inspected

It filters WS trades by price times size and reconnects with increasing delay after close.

## Limitation that matters

Its detached processTrade rejection and WebSocket error handlers throw inside callbacks; no source gap or missed-trade recovery is shown.

## Practical check for a trading system

Test callback failures and reconnect gaps before treating alerts as complete market evidence.

## Why this score

2/5. The feed is relevant, but failure paths make it a cautionary reference rather than a collector blueprint.

## Source trail

[README](https://github.com/0xhype/hyperliquid-tracker/blob/5dda9a1aaa6be32178f041db0baa3a372acec160/README.md#L1); [src/core/websocket.ts](https://github.com/0xhype/hyperliquid-tracker/blob/5dda9a1aaa6be32178f041db0baa3a372acec160/src/core/websocket.ts#L64).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
