# HyperLiquidAlgoBot - Does a candle strategy enter only after its signal becomes available?

**Decision question:** Does a candle strategy enter only after its signal becomes available?

| Field | Review |
| --- | --- |
| Upstream | [SimSimButDifferent/HyperLiquidAlgoBot](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot) |
| Primary area | Backtesting & Simulation |
| Source commit | [448d1ef3a8b3d8211c62ebe7afd8a4be556be678](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot/commit/448d1ef3a8b3d8211c62ebe7afd8a4be556be678) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Backtests a Hyperliquid indicator strategy at candle closes. Current-candle signals can trade at their own close; liquidation is approximate. |

## What this project does

A Hyperliquid strategy bot with a candle-driven backtest and separate live order helpers.

## Mechanism inspected

The backtester includes the current candle in the strategy input and can open or close a position at that same candle close. It applies a simplified leverage-based liquidation threshold and round-trip fees.

## Limitation that matters

If the current candle is known only at its close, filling a signal at that same close assumes an unavailable execution opportunity. The liquidation threshold is a generic maintenance-margin approximation rather than venue account-margin replay.

## Practical check for a trading system

Move decisions to the next executable event and test funding, fees, intrabar liquidations and marketable depth before interpreting backtest returns.

## Why this score

1/5. This is chiefly a concrete same-bar execution and margin-model caution.

## Source trail

[README](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot/blob/448d1ef3a8b3d8211c62ebe7afd8a4be556be678/README.md#L1); [src/backtesting/Backtester.js](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot/blob/448d1ef3a8b3d8211c62ebe7afd8a4be556be678/src/backtesting/Backtester.js#L100); [src/backtesting/Backtester.js](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot/blob/448d1ef3a8b3d8211c62ebe7afd8a4be556be678/src/backtesting/Backtester.js#L144); [src/backtesting/Backtester.js](https://github.com/SimSimButDifferent/HyperLiquidAlgoBot/blob/448d1ef3a8b3d8211c62ebe7afd8a4be556be678/src/backtesting/Backtester.js#L221).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
