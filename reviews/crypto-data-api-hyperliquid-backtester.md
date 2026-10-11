# Hyperliquid Backtester - Does a bar backtest apply the same causal timing to entries and exits?

**Decision question:** Does a bar backtest apply the same causal timing to entries and exits?

| Field | Review |
| --- | --- |
| Upstream | [Crypto-Data-API/hyperliquid-backtester](https://github.com/Crypto-Data-API/hyperliquid-backtester) |
| Primary area | Backtesting & Simulation |
| Source commit | [a9dd95dafe0ce3cfae087449a51c683eda725bee](https://github.com/Crypto-Data-API/hyperliquid-backtester/commit/a9dd95dafe0ce3cfae087449a51c683eda725bee) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | It queues entries from a completed bar and fills them at the next bar open while passing only history through the current bar to the strategy. A strategy-directed exit closes at the same bar close after that bar is visible; this needs an executable-close assumption. Funding before the first sample is set to zero. |

## What this project does

A Hyperliquid perpetual bar backtester with fees, funding and account simulation.

## Mechanism inspected

It queues entries from a completed bar and fills them at the next bar open while passing only history through the current bar to the strategy.

## Limitation that matters

A strategy-directed exit closes at the same bar close after that bar is visible; this needs an executable-close assumption. Funding before the first sample is set to zero.

## Practical check for a trading system

Declare entry and exit decision clocks separately and reject missing funding where it matters.

## Why this score

3/5. The delayed entry model is useful, with material timing and funding assumptions to test.

## Source trail

[README](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/README.md#L1); [src/hlbt/backtester.py](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/src/hlbt/backtester.py#L140); [src/hlbt/backtester.py](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/src/hlbt/backtester.py#L191); [src/hlbt/sync.py](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/src/hlbt/sync.py#L196); [src/hlbt/sync.py](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/src/hlbt/sync.py#L202); [Root license](https://github.com/Crypto-Data-API/hyperliquid-backtester/blob/a9dd95dafe0ce3cfae087449a51c683eda725bee/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
