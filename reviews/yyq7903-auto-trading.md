# Polymarket BTC 5M Auto-Trading - Does a large strategy sweep preserve a genuinely held-out validation set?

**Decision question:** Does a large strategy sweep preserve a genuinely held-out validation set?

| Field | Review |
| --- | --- |
| Upstream | [yyq7903/auto-trading](https://github.com/yyq7903/auto-trading) |
| Primary area | Research & Reproducibility |
| Source commit | [728682a15de08844429f5cf632110a6924bc53be](https://github.com/yyq7903/auto-trading/commit/728682a15de08844429f5cf632110a6924bc53be) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Reports coverage reasons while sweeping entry and freshness filters. Sorting many configurations by validation PnL spends that holdout. |

## What this project does

A Polymarket BTC five-minute trading project with market-integrity records and exploratory strategy sweeps.

## Mechanism inspected

Its research script counts exclusion reasons, price seconds and book seconds, then evaluates many probability, timing and freshness configurations on chronological train and validation slices.

## Limitation that matters

The same validation slice is used to rank and choose configurations, including a robustness score that reads validation drawdown. That turns the validation slice into selection data rather than a final independent check. Its data scan counts rows without proving economic fillability.

## Practical check for a trading system

Keep trial counts and exclusion reasons, then reserve another untouched period after any validation-based selection.

## Why this score

2/5. The source exposes useful integrity dimensions and a concrete reuse-of-validation trap.

## Source trail

[README](https://github.com/yyq7903/auto-trading/blob/728682a15de08844429f5cf632110a6924bc53be/README.md#L12); [btc5m-trader/backtest/pragmatic_research.py](https://github.com/yyq7903/auto-trading/blob/728682a15de08844429f5cf632110a6924bc53be/btc5m-trader/backtest/pragmatic_research.py#L253); [btc5m-trader/backtest/pragmatic_research.py](https://github.com/yyq7903/auto-trading/blob/728682a15de08844429f5cf632110a6924bc53be/btc5m-trader/backtest/pragmatic_research.py#L411); [btc5m-trader/backtest/pragmatic_research.py](https://github.com/yyq7903/auto-trading/blob/728682a15de08844429f5cf632110a6924bc53be/btc5m-trader/backtest/pragmatic_research.py#L458); [License text](https://github.com/yyq7903/auto-trading/blob/728682a15de08844429f5cf632110a6924bc53be/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
