# Crypto Market Data Pipeline - Can a WebSocket loop stay alive while its recorder silently loses ticks?

**Decision question:** Can a WebSocket loop stay alive while its recorder silently loses ticks?

| Field | Review |
| --- | --- |
| Upstream | [juitindev/crypto-market-data-pipeline](https://github.com/juitindev/crypto-market-data-pipeline) |
| Primary area | Market Data & Ingestion |
| Source commit | [1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb](https://github.com/juitindev/crypto-market-data-pipeline/commit/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The WS loop isolates per-message dispatch errors and reconnects after transport failure; the recorder appends ticks to rotating JSONL files. Recorder write exceptions are logged and swallowed, so the producer can continue without durable evidence or a lost-tick count. |

## What this project does

A typed Binance futures ingestion pipeline with an event bus and JSONL recorder.

## Mechanism inspected

The WS loop isolates per-message dispatch errors and reconnects after transport failure; the recorder appends ticks to rotating JSONL files.

## Limitation that matters

Recorder write exceptions are logged and swallowed, so the producer can continue without durable evidence or a lost-tick count.

## Practical check for a trading system

Make archival write acknowledgements and loss counters part of feed health.

## Why this score

2/5. Good modular ingestion structure, but this write path is not fail-closed.

## Source trail

[README](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/README.md#L1); [src/market_pipeline/adapters/binance_ws.py](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/src/market_pipeline/adapters/binance_ws.py#L64); [src/market_pipeline/adapters/binance_ws.py](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/src/market_pipeline/adapters/binance_ws.py#L89); [src/market_pipeline/ingestion/recorder.py](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/src/market_pipeline/ingestion/recorder.py#L36); [src/market_pipeline/ingestion/recorder.py](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/src/market_pipeline/ingestion/recorder.py#L46); [Root license](https://github.com/juitindev/crypto-market-data-pipeline/blob/1d8ef8489d52ded122380d7d10d53a6c5dfcdaeb/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
