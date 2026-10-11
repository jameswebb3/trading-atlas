# NBA Finals Trading Lab - Does an external score feed lead a prediction-market quote by enough to trade?

**Decision question:** Does an external score feed lead a prediction-market quote by enough to trade?

| Field | Review |
| --- | --- |
| Upstream | [ivancor1/nba-finals-trading](https://github.com/ivancor1/nba-finals-trading) |
| Primary area | Market Data & Ingestion |
| Source commit | [3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1](https://github.com/ivancor1/nba-finals-trading/commit/3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Measures score-feed lead against book repricing and keeps the latency verdict separate from trading edge. A positive feed lead still needs order arrival, depth and fee evidence. |

## What this project does

A sports-market research lab with independent score/book capture, receive-time comparison and fee-aware backtests.

## Mechanism inspected

The latency report compares receive timestamps around isolated score changes, counts events where the feed leads and refuses a taker conclusion below a minimum event count. A separate fee lab charges both entry and exit at a price-dependent schedule.

## Limitation that matters

One event feed and one market family do not prove transferable timing advantage; the script's positive latency verdict explicitly calls for further research. Fee-aware backtest outputs were not reproduced.

## Practical check for a trading system

Measure decision-relevant lead with both feeds' receipt clocks and separate observed lead from executable edge after fees.

## Why this score

3/5 because Concrete timing and fee checks are present, but sample selection and venue specifics constrain inference.

## Source trail

[README](https://github.com/ivancor1/nba-finals-trading/blob/3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1/README.md#L202); [latency_report.py](https://github.com/ivancor1/nba-finals-trading/blob/3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1/latency_report.py#L104); [latency_report.py](https://github.com/ivancor1/nba-finals-trading/blob/3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1/latency_report.py#L153); [fee_backtest.py](https://github.com/ivancor1/nba-finals-trading/blob/3748b05f4e4e16a9d6d357fd2a99aa02dcb2a5e1/fee_backtest.py#L58).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
