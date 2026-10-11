# Hyperliquid Real-Time Data Collector - Does a collector preserve its CSV evidence across restart?

**Decision question:** Does a collector preserve its CSV evidence across restart?

| Field | Review |
| --- | --- |
| Upstream | [bwroniszewski/hyperliquid-realtime-data](https://github.com/bwroniszewski/hyperliquid-realtime-data) |
| Primary area | Market Data & Ingestion |
| Source commit | [0bc00f7a804607eae9469a9541edcb02221ca720](https://github.com/bwroniszewski/hyperliquid-realtime-data/commit/0bc00f7a804607eae9469a9541edcb02221ca720) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Initialization creates per-coin SQLite tables and opens each CSV in write mode before later event handlers append rows. The CSV path is truncated on every start, so the files cannot serve as durable history without an external archival step. |

## What this project does

A Hyperliquid WebSocket collector for L2, trades, candles and asset context.

## Mechanism inspected

Initialization creates per-coin SQLite tables and opens each CSV in write mode before later event handlers append rows.

## Limitation that matters

The CSV path is truncated on every start, so the files cannot serve as durable history without an external archival step.

## Practical check for a trading system

Test restart persistence and keep append-only raw frames with receive time before deriving tables.

## Why this score

1/5. A direct negative example of a collector that can silently erase the prior session.

## Source trail

[README](https://github.com/bwroniszewski/hyperliquid-realtime-data/blob/0bc00f7a804607eae9469a9541edcb02221ca720/README.md#L1); [realtime_data_HL.py](https://github.com/bwroniszewski/hyperliquid-realtime-data/blob/0bc00f7a804607eae9469a9541edcb02221ca720/realtime_data_HL.py#L47); [Root license](https://github.com/bwroniszewski/hyperliquid-realtime-data/blob/0bc00f7a804607eae9469a9541edcb02221ca720/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
