# kalshi-stack — Treat print-replay maker returns as an upper bound

**Decision question:** Can print-based passive-fill replay overstate a maker strategy's executable edge?

| Field | Review |
| --- | --- |
| Upstream | [agiprolabs/kalshi-stack](https://github.com/agiprolabs/kalshi-stack) |
| Primary area | Backtesting & Simulation |
| Source commit | [01c9f767a576ff2d0fc38df2f074594fc23a4eb5](https://github.com/agiprolabs/kalshi-stack/commit/01c9f767a576ff2d0fc38df2f074594fc23a4eb5) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant source and relevant test source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its print-replay module explicitly labels passive-fill EV an upper bound; the paper exchange adds queue-ahead depletion, trade-ID deduplication and one-time print-volume spending. The source reports a failed live probe, but that outcome is author-reported and cannot be generalized; queue-ahead from L2 is still an approximation. |

## What this project does

kalshi-stack is a Kalshi infrastructure reference with a market mirror, paper exchange, authenticated client and print-based research replay. [Project README](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/README.md#L1).

## Mechanism inspected

The research replay marks a ladder rung filled on the first qualifying print and warns that this is an upper bound. The paper book initializes queue_ahead from displayed depth, deduplicates trade IDs and spends each print's volume at most once. Its regression suite includes a queue-ahead depletion case. [Print replay](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/backtest/replay.py#L1).

## Limitation that matters

Neither a touch print nor an L2 queue estimate proves that a specific live order would have filled. The README and source describe an adverse live probe, but this review has not independently reproduced those results. This is a source review, not a runtime or security test.

## Practical check for a trading system

Show both a permissive touch bound and a queue-aware estimate for passive strategies, then require order-level live receipts before treating either as executable alpha.

## Why this score

4/5 because the gap between print-touch backtests and queue-aware, live-observed fills is a direct trading-decision risk, with relevant regression tests inspected.

## Source trail

[README](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/README.md#L1); [Print replay](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/backtest/replay.py#L1); [Queue model](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/crates/market-mirror/src/orderbook.rs#L4); [Fill tests](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/crates/market-mirror/tests/fill_realism.rs#L97); [License](https://github.com/agiprolabs/kalshi-stack/blob/01c9f767a576ff2d0fc38df2f074594fc23a4eb5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
