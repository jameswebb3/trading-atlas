# vectorbt Backtesting Skills - Can shifted allocation still import future opening prices?

**Decision question:** Can shifted allocation still import future opening prices?

| Field | Review |
| --- | --- |
| Upstream | [marketcalls/vectorbt-backtesting-skills](https://github.com/marketcalls/vectorbt-backtesting-skills) |
| Primary area | Backtesting & Simulation |
| Source commit | [05d9e8b12fa408f1373c6b79620f8a5473fb874c](https://github.com/marketcalls/vectorbt-backtesting-skills/commit/05d9e8b12fa408f1373c6b79620f8a5473fb874c) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The dual-momentum script picks a quarterly winner from closing returns, shifts the winner by one quarter and maps it to the next trading day. This is a visible timing safeguard. The open-price panel is reindexed to surviving close dates and then forward- and backward-filled. Whenever an opening price is missing, backward fill may import a later open into an earlier execution date. The review does not establish that the shipped input actually contains such a gap. |

## What this project does

Quarterly allocation is explicitly shifted, but missing execution opens can be filled backward from later dates.

## Mechanism inspected

The dual-momentum script picks a quarterly winner from closing returns, shifts the winner by one quarter and maps it to the next trading day. This is a visible timing safeguard.

## Limitation that matters

The open-price panel is reindexed to surviving close dates and then forward- and backward-filled. Whenever an opening price is missing, backward fill may import a later open into an earlier execution date. The review does not establish that the shipped input actually contains such a gap.

## Practical check for a trading system

Disallow backward fill of execution prices; record missing opening quotes and fail or skip the affected trade after proving the price was available at decision time.

## Why this score

2/5. It illustrates a specific, source-visible lookahead path, but is an equity-ETF example without a validated execution model.

## Source trail

[README.md](https://github.com/marketcalls/vectorbt-backtesting-skills/blob/05d9e8b12fa408f1373c6b79620f8a5473fb874c/README.md#L1); [backtesting/dual_momentum_backtest.py](https://github.com/marketcalls/vectorbt-backtesting-skills/blob/05d9e8b12fa408f1373c6b79620f8a5473fb874c/backtesting/dual_momentum_backtest.py#L52); [backtesting/dual_momentum_backtest.py](https://github.com/marketcalls/vectorbt-backtesting-skills/blob/05d9e8b12fa408f1373c6b79620f8a5473fb874c/backtesting/dual_momentum_backtest.py#L70); [backtesting/dual_momentum_backtest.py](https://github.com/marketcalls/vectorbt-backtesting-skills/blob/05d9e8b12fa408f1373c6b79620f8a5473fb874c/backtesting/dual_momentum_backtest.py#L79)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
