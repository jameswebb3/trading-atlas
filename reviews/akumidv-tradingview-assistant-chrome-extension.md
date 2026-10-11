# TradingView Assistant - Can a parameter search present an in-sample winner as evidence?

**Decision question:** Can a parameter search present an in-sample winner as evidence?

| Field | Review |
| --- | --- |
| Upstream | [akumidv/tradingview-assistant-chrome-extension](https://github.com/akumidv/tradingview-assistant-chrome-extension) |
| Primary area | Backtesting & Simulation |
| Source commit | [263a9f54c00453f5e41487f23a469006e18ae0f8](https://github.com/akumidv/tradingview-assistant-chrome-extension/commit/263a9f54c00453f5e41487f23a469006e18ae0f8) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The optimizer loads an initial best result and updates a running best value while cycling parameter combinations through TradingView reports. The inspected loop ranks the same tested reports; it does not show a reserved holdout or adjustment for the search count. |

## What this project does

A browser extension that automates TradingView strategy parameter tests.

## Mechanism inspected

The optimizer loads an initial best result and updates a running best value while cycling parameter combinations through TradingView reports.

## Limitation that matters

The inspected loop ranks the same tested reports; it does not show a reserved holdout or adjustment for the search count.

## Practical check for a trading system

Keep the parameter search and final untouched evaluation as separate artifacts.

## Why this score

2/5. It exposes the optimization feedback loop but not independent validation.

## Source trail

[README](https://github.com/akumidv/tradingview-assistant-chrome-extension/blob/263a9f54c00453f5e41487f23a469006e18ae0f8/README.md#L1); [content_scripts/backtest.js](https://github.com/akumidv/tradingview-assistant-chrome-extension/blob/263a9f54c00453f5e41487f23a469006e18ae0f8/content_scripts/backtest.js#L23); [content_scripts/backtest.js](https://github.com/akumidv/tradingview-assistant-chrome-extension/blob/263a9f54c00453f5e41487f23a469006e18ae0f8/content_scripts/backtest.js#L41); [content_scripts/backtest.js](https://github.com/akumidv/tradingview-assistant-chrome-extension/blob/263a9f54c00453f5e41487f23a469006e18ae0f8/content_scripts/backtest.js#L81).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
