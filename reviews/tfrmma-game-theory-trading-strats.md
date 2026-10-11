# Game Theory Trading Strats — Queue state must be explicit

**Decision question:** What must a tick replay track before crediting a maker fill?

| Field | Review |
| --- | --- |
| Upstream | [tfrmma/game-theory-trading-strats](https://github.com/tfrmma/game-theory-trading-strats) |
| Primary area | Execution & Exchange Integration |
| Source commit | [89f8462bd8b539b1b42b518b41aca4fadaf0178f](https://github.com/tfrmma/game-theory-trading-strats/commit/89f8462bd8b539b1b42b518b41aca4fadaf0178f) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The replay keeps quantity ahead of each resting order and drains it before crediting fills; cancellations advance the queue only through an assumed fraction. The cancellation fraction and synthetic order flow are modeling assumptions, not verified Hyperliquid queue truth. |

## What this project does

A collection of market-making strategies and an L2 tick replay. [Project README](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/README.md#L36).

## Mechanism inspected

The replay keeps quantity ahead of each resting order and drains it before crediting fills; cancellations advance the queue only through an assumed fraction. [Implementation](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/backtesting/tick_by_tick_backtester.py#L184). [Related source 1](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/engine/central_risk_manager.py#L103).

## Limitation that matters

The cancellation fraction and synthetic order flow are modeling assumptions, not verified Hyperliquid queue truth. Report sensitivity before using simulated maker PnL. This is a source review, not a runtime or security test.

## Practical check for a trading system

Expose queue-ahead, arrival latency, and cancellation assumptions beside every maker-fill result.

## Why this score

The explicit FIFO state is a useful replay reference, bounded by unverified queue dynamics.

## Source trail

[README](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/README.md#L36); [Implementation](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/backtesting/tick_by_tick_backtester.py#L184); [Related source 1](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/engine/central_risk_manager.py#L103) - [License](https://github.com/tfrmma/game-theory-trading-strats/blob/89f8462bd8b539b1b42b518b41aca4fadaf0178f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
