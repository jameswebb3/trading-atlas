# LEAN: a shared engine still has different transaction clocks

**Decision question:** Which order-event timing changes between backtest and live execution?

| Field | Review |
| --- | --- |
| Upstream | [QuantConnect/Lean](https://github.com/QuantConnect/Lean) |
| Primary area | Backtesting & Simulation |
| Source commit | [f49bb9623a3e8782bf22bbd2cb51f691058cfdc3](https://github.com/QuantConnect/Lean/commit/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/QuantConnect/Lean/blob/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Documents separate transaction processing for backtest and live, and processes pending backtest requests synchronously with the algorithm loop. Synchronous backtest submission differs from concurrent live brokerage events; parity of interfaces does not imply event-order equivalence. |

## Project overview

Algorithmic trading engine with pluggable data feeds, transaction handling, and event timing. A reference for structuring backtesting and live execution around a shared system architecture.

[Project documentation](https://github.com/QuantConnect/Lean/blob/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3/Documentation/readme.md#L7-L22).

## Mechanism worth inspecting

LEAN's [system overview](https://github.com/QuantConnect/Lean/blob/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3/Documentation/readme.md#L7-L19) distinguishes datafeed, transaction, and realtime event plugins for backtest and live. Its [backtesting transaction handler](https://github.com/QuantConnect/Lean/blob/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3/Engine/TransactionHandlers/BacktestingTransactionHandler.cs#L61-L87) says requests are processed synchronously on the algorithm thread unless concurrency-enabled live mode applies; it processes pending requests before the next algorithm time loop and scans the brokerage. The [submission wait path](https://github.com/QuantConnect/Lean/blob/f49bb9623a3e8782bf22bbd2cb51f691058cfdc3/Engine/TransactionHandlers/BacktestingTransactionHandler.cs#L100-L123) makes that special case explicit.

## Important limit

This review does not establish how every fill model behaves. It identifies a specific ordering difference that a replay must acknowledge: a live venue can acknowledge, fill, or reject on a different clock from a synchronous backtest handler.

## Questions to take into your own design

- Are decision, submit, ACK, fill, and cancel times recorded separately?
- Does a backtest process a request before the next strategy event while live does not?
- Which equivalence claims exclude concurrency and exchange latency?

## Why this score for a trading system

Its explicit backtest/live transaction split is directly useful when assessing trading replay parity, with concurrency still venue dependent.

**Scope of this review:** We read the pinned README, system overview, and transaction handler. We did not run a backtest, inspect every fill model, or verify a live brokerage trace.
