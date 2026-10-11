# Quant Event-Driven Backtesting Framework - Can a two-leg backtest accidentally fill only one leg?

**Decision question:** Can a two-leg backtest accidentally fill only one leg?

| Field | Review |
| --- | --- |
| Upstream | [ShubhamOzza/quant-event-driven-backtesting-framework](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework) |
| Primary area | Backtesting & Simulation |
| Source commit | [4149266616367b227828e2de4316675f749f10b0](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework/commit/4149266616367b227828e2de4316675f749f10b0) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Groups linked pair orders for simulated all-or-none handling and makes future-data access an error. The README acknowledges that cash-floor sizing may overshoot its nominal gross leverage ceiling. |

## What this project does

A single-file event-driven equities backtester with next-bar fills, accounting checks and linked pair signals.

## Mechanism inspected

Signals and orders carry a link_id; the execution handler groups linked orders and treats the two legs as one fill decision in the simulator. A separate lookahead exception rejects future-bar requests.

## Limitation that matters

Atomicity here is a simulation policy. Two independent exchange orders cannot be made atomic just by sharing an identifier, and the README notes a cash-floor sizing path that can exceed the nominal gross leverage cap.

## Practical check for a trading system

Test pair-leg reservation and accounting jointly while treating live legging, rejection and rollback as separate execution risks.

## Why this score

3/5 because The linked-order path targets a real backtest error, but it does not transfer as a live atomic-execution guarantee.

## Source trail

[README](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework/blob/4149266616367b227828e2de4316675f749f10b0/README.md#L105); [Event_Driven_Backtesting_Framework.py](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework/blob/4149266616367b227828e2de4316675f749f10b0/Event_Driven_Backtesting_Framework.py#L114); [Event_Driven_Backtesting_Framework.py](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework/blob/4149266616367b227828e2de4316675f749f10b0/Event_Driven_Backtesting_Framework.py#L733); [Event_Driven_Backtesting_Framework.py](https://github.com/ShubhamOzza/quant-event-driven-backtesting-framework/blob/4149266616367b227828e2de4316675f749f10b0/Event_Driven_Backtesting_Framework.py#L222).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
