# TradingView-Screener — A screener response is not point-in-time evidence

**Decision question:** Can a live or delayed scanner response be replayed causally?

| Field | Review |
| --- | --- |
| Upstream | [shner-elmo/TradingView-Screener](https://github.com/shner-elmo/TradingView-Screener) |
| Primary area | Market Data & Ingestion |
| Source commit | [5422d9012752353c59a31d13f54ceba55c265d9d](https://github.com/shner-elmo/TradingView-Screener/commit/5422d9012752353c59a31d13f54ceba55c265d9d) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The query posts filter JSON with a timeout and parses the returned scanner rows; its documentation distinguishes live access via authentication from delayed data. The shown response path has no per-field publication timestamp or historical snapshot identity, so it cannot establish available_at for a backtest. |

## What this project does

Python query wrapper for TradingView screener endpoints and tabular results. [README](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/README.md).

## Mechanism inspected

The query posts filter JSON with a timeout and parses the returned scanner rows; its documentation distinguishes live access via authentication from delayed data. [Implementation](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/src/tradingview_screener/query.py#L689-L745).

## Limitation that matters

The shown response path has no per-field publication timestamp or historical snapshot identity, so it cannot establish available_at for a backtest. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Do not backfill causal factors from current screener responses without independently timestamped snapshots and survivorship controls.

## Why this score

The query posts filter JSON with a timeout and parses the returned scanner rows; its documentation distinguishes live access via authentication from delayed data. The shown response path has no per-field publication timestamp or historical snapshot identity, so it cannot establish available_at for a backtest.

## Source trail

[README](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/README.md) · [Implementation](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/src/tradingview_screener/query.py#L689-L745) · [License](https://github.com/shner-elmo/TradingView-Screener/blob/5422d9012752353c59a31d13f54ceba55c265d9d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
