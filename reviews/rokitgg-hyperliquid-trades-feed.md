# Hyperliquid Trades Feed Bot - Does a large-trade alert feed survive reconnects without silent gaps?

**Decision question:** Does a large-trade alert feed survive reconnects without silent gaps?

| Field | Review |
| --- | --- |
| Upstream | [rokitgg/hyperliquid-trades-feed](https://github.com/rokitgg/hyperliquid-trades-feed) |
| Primary area | Market Data & Ingestion |
| Source commit | [4c336e5d393296f37707d4e4fd2dbb40a5d17252](https://github.com/rokitgg/hyperliquid-trades-feed/commit/4c336e5d393296f37707d4e4fd2dbb40a5d17252) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | It subscribes to trades for each configured coin, multiplies price by size, and dispatches trades above a fixed threshold to an asynchronous notification path. The reconnect path creates a new socket and resubscribes but has no source-visible replay cursor, gap marker or deduplication key. Errors thrown inside asynchronous catch and WebSocket callbacks are not a reliable completeness record. |

## What this project does

A Hyperliquid trades WebSocket listener that filters configured coins by trade notional and sends selected events to Telegram.

## Mechanism inspected

It subscribes to trades for each configured coin, multiplies price by size, and dispatches trades above a fixed threshold to an asynchronous notification path.

## Limitation that matters

The reconnect path creates a new socket and resubscribes but has no source-visible replay cursor, gap marker or deduplication key. Errors thrown inside asynchronous catch and WebSocket callbacks are not a reliable completeness record.

## Practical check for a trading system

Treat a reconnect as a data-quality event: record the gap interval, backfill from a durable source, and deduplicate trades by stable event identity before using counts as research data.

## Why this score

2/5. The feed gives a concrete ingestion example and an equally concrete reason alerts alone are insufficient evidence of complete market data.

## Source trail

[README](https://github.com/rokitgg/hyperliquid-trades-feed/blob/4c336e5d393296f37707d4e4fd2dbb40a5d17252/README.md#L1); [src/core/websocket.ts](https://github.com/rokitgg/hyperliquid-trades-feed/blob/4c336e5d393296f37707d4e4fd2dbb40a5d17252/src/core/websocket.ts#L52); [src/core/websocket.ts](https://github.com/rokitgg/hyperliquid-trades-feed/blob/4c336e5d393296f37707d4e4fd2dbb40a5d17252/src/core/websocket.ts#L89); [src/core/websocket.ts](https://github.com/rokitgg/hyperliquid-trades-feed/blob/4c336e5d393296f37707d4e4fd2dbb40a5d17252/src/core/websocket.ts#L64).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
