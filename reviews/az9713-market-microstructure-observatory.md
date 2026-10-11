# Market Microstructure Observatory - Can passive fills be constrained by prints ahead of the order?

**Decision question:** Can passive fills be constrained by prints ahead of the order?

| Field | Review |
| --- | --- |
| Upstream | [az9713/market-microstructure-observatory](https://github.com/az9713/market-microstructure-observatory) |
| Primary area | Backtesting & Simulation |
| Source commit | [853994e9c48ec2b1a81d29602011a8195189dc24](https://github.com/az9713/market-microstructure-observatory/commit/853994e9c48ec2b1a81d29602011a8195189dc24) |
| Reviewed | 2026-10-11 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Delays trading actions and advances a passive order only when prints consume queue-ahead volume. L1 queue-ahead is an assumption under unknown cancellations, not a reconstruction of exact order priority. |

## What this project does

A small order-book simulator and real-tape backtest with explicit action latency, maker/taker fees and queue-aware passive orders.

## Mechanism inspected

The backtest delays place, cancel and market actions; a passive order starts behind displayed size and queueAhead decreases as trades print at its price. The separate book core stores price-level order queues with price-time matching for synthetic simulation.

## Limitation that matters

Its real-data backtest uses L1 displayed size and optional queue refinement, so cancellation location and hidden liquidity remain unobserved. The synthetic book core can verify internal mechanics but cannot validate a historical queue estimate against an exchange. No root license file was found.

## Practical check for a trading system

Use trade-through and queue-ahead sensitivity as execution bounds; keep synthetic book validation separate from real-feed fill evidence.

## Why this score

3/5 because Direct action latency and print-gated maker fills are visible, but historical queue uncertainty and licensing limit adoption.

## Source trail

[README fill assumptions](https://github.com/az9713/market-microstructure-observatory/blob/853994e9c48ec2b1a81d29602011a8195189dc24/README.md#L130); [Delayed actions and queue](https://github.com/az9713/market-microstructure-observatory/blob/853994e9c48ec2b1a81d29602011a8195189dc24/src/backtest/engine.js#L46); [Queue updates on prints](https://github.com/az9713/market-microstructure-observatory/blob/853994e9c48ec2b1a81d29602011a8195189dc24/src/backtest/engine.js#L99); [Synthetic book matching](https://github.com/az9713/market-microstructure-observatory/blob/853994e9c48ec2b1a81d29602011a8195189dc24/src/core/book.js#L72).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
