# Prediction Market Trading Bot - Are heuristic probabilities enough to size a binary market trade?

**Decision question:** Are heuristic probabilities enough to size a binary market trade?

| Field | Review |
| --- | --- |
| Upstream | [suislanchez/polymarket-kalshi-weather-bot](https://github.com/suislanchez/polymarket-kalshi-weather-bot) |
| Primary area | Signals & Models |
| Source commit | [e406394d59c208cc035c4fdf37ebb26636e15a47](https://github.com/suislanchez/polymarket-kalshi-weather-bot/commit/e406394d59c208cc035c4fdf37ebb26636e15a47) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Combines BTC indicators with market price and capped fractional Kelly sizing. Heuristic directional scores are not calibrated outcome probabilities. |

## What this project does

A multi-market bot combining BTC five-minute price indicators and weather forecasts for Kalshi and Polymarket.

## Mechanism inspected

For BTC markets it blends RSI, momentum, VWAP, SMA and market-skew inputs, requires indicator agreement, compares a model probability with a market price, then caps fractional Kelly sizing.

## Limitation that matters

The inspected BTC probability is a weighted indicator heuristic, not a demonstrated calibrated event probability. The source uses Binance candle inputs and ignores whether a cross-market quote is still executable at order arrival. No root license file was verified.

## Practical check for a trading system

Calibrate probabilities and require as-of exchange quotes, fees and latency before using any Kelly fraction or claiming edge.

## Why this score

2/5. The code makes the decision pipeline inspectable but not economically validated.

## Source trail

[README](https://github.com/suislanchez/polymarket-kalshi-weather-bot/blob/e406394d59c208cc035c4fdf37ebb26636e15a47/README.md#L11); [backend/core/signals.py](https://github.com/suislanchez/polymarket-kalshi-weather-bot/blob/e406394d59c208cc035c4fdf37ebb26636e15a47/backend/core/signals.py#L48); [backend/core/signals.py](https://github.com/suislanchez/polymarket-kalshi-weather-bot/blob/e406394d59c208cc035c4fdf37ebb26636e15a47/backend/core/signals.py#L74); [backend/core/signals.py](https://github.com/suislanchez/polymarket-kalshi-weather-bot/blob/e406394d59c208cc035c4fdf37ebb26636e15a47/backend/core/signals.py#L123); [backend/core/signals.py](https://github.com/suislanchez/polymarket-kalshi-weather-bot/blob/e406394d59c208cc035c4fdf37ebb26636e15a47/backend/core/signals.py#L196).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
