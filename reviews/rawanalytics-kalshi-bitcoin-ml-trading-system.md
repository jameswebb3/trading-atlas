# Kalshi Bitcoin ML Trading System - Can a paper fill advantage survive prices that could actually have been quoted?

**Decision question:** Can a paper fill advantage survive prices that could actually have been quoted?

| Field | Review |
| --- | --- |
| Upstream | [Rawanalytics/kalshi-bitcoin-ml-trading-system](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system) |
| Primary area | Backtesting Simulation |
| Source commit | [bcd886a3af22aa0a31ce003e38bd9890331a16df](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/commit/bcd886a3af22aa0a31ce003e38bd9890331a16df) |
| Reviewed | 2026-10-10 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Reprices recorded paper and live fills against bid/ask candles, counts missing and empty quote states, then evaluates forward folds at quote-side prices and fees. The harness uses a minute candle that may end after the signal; its conservative open/close boundary is not an observed intra-minute executable quote, and raw data are not published for independent replication. |

## What this project does

A documented end-to-end Kalshi BTC prediction-market research system with paper and live execution paths. Its public history centers on an apparent paper edge that failed after fill-price scrutiny.

## Mechanism inspected

The acceptance harness joins recorded fills by ticker and timestamp to the first minute candle whose end is at or after the fill time, rejects distant or empty quote states, uses bid/ask and a small adverse haircut, and compares repriced outcomes to recorded fills. It counts missing candles, empty books and unsettled markets separately. The forward experiment retrains on earlier market-close times with an embargo and compares model AUC with the market price before grading first-trigger trades at quote-side prices and fees.

## Limitation that matters

Minute OHLC quotes do not reconstruct the exact book at an intra-minute decision. In particular, a selected candle can end after the signal, and the conservative open/close choice does not prove the whole price path was executable. The README reports a negative live result and fill-bias figures, but source data are excluded, so this review does not independently reproduce those numbers. Its contracts and fees are Kalshi-specific.

## Practical check for a trading system

Use real execution receipts to calibrate any fill model. Keep no-quote, empty-book and unsettled rows visible; place a strict clock on the quote selected for a signal and compare model forecasts with the market-implied baseline before translating a backtest into order policy.

## Why this score

4/5 because the source addresses a costly trading failure with explicit replay and forward-evaluation code, while the candle-resolution and missing raw tape limit what can be verified.

## Source trail

[README and reported audit](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/blob/bcd886a3af22aa0a31ce003e38bd9890331a16df/README.md#L49); [Quote selection](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/blob/bcd886a3af22aa0a31ce003e38bd9890331a16df/scripts/harness.py#L44); [Paper/live repricing](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/blob/bcd886a3af22aa0a31ce003e38bd9890331a16df/scripts/harness.py#L113); [Forward fold and market baseline](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/blob/bcd886a3af22aa0a31ce003e38bd9890331a16df/scripts/gate_experiment.py#L128); [Market rules](https://github.com/Rawanalytics/kalshi-bitcoin-ml-trading-system/blob/bcd886a3af22aa0a31ce003e38bd9890331a16df/MARKET_RULES.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
