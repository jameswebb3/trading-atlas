# Kalshi Trading System - Does a timed-out order become safe after a cancel request?

**Decision question:** Does a timed-out order become safe after a cancel request?

| Field | Review |
| --- | --- |
| Upstream | [sririthishpalani-max/kalshi-trading-system](https://github.com/sririthishpalani-max/kalshi-trading-system) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ac04d4234c09f07e549a8909ff814b85dd73e609](https://github.com/sririthishpalani-max/kalshi-trading-system/commit/ac04d4234c09f07e549a8909ff814b85dd73e609) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Adds a timeout cancel path and independent risk checks to a Kalshi bot. The timeout path needs account-side reconciliation before it can call an order definitively closed. |

## What this project does

An asynchronous Kalshi short-horizon trading bot with a paper default, order timeout and a separate risk manager.

## Mechanism inspected

The bot checks risk before order submission, polls the resulting order briefly, and attempts cancellation if still resting. The risk manager tracks daily loss and per-market activity.

## Limitation that matters

The inspected timeout path treats a cancellation as closing local risk without showing a subsequent account-side fill and open-order reconciliation. A fill may race cancellation; a cancel request is not terminal evidence. The backtest is bar-based and cannot settle that race.

## Practical check for a trading system

Track submit, ACK, cancel, late fill and account snapshot as separate states; do not release exposure on cancel intent alone.

## Why this score

2/5 because The timing problem is visible and valuable as a caution, but the safety claim is not established by the inspected branch.

## Source trail

[README](https://github.com/sririthishpalani-max/kalshi-trading-system/blob/ac04d4234c09f07e549a8909ff814b85dd73e609/README.md#L95); [bot.py](https://github.com/sririthishpalani-max/kalshi-trading-system/blob/ac04d4234c09f07e549a8909ff814b85dd73e609/bot.py#L102); [bot.py](https://github.com/sririthishpalani-max/kalshi-trading-system/blob/ac04d4234c09f07e549a8909ff814b85dd73e609/bot.py#L107); [risk_manager.py](https://github.com/sririthishpalani-max/kalshi-trading-system/blob/ac04d4234c09f07e549a8909ff814b85dd73e609/risk_manager.py#L74); [License text](https://github.com/sririthishpalani-max/kalshi-trading-system/blob/ac04d4234c09f07e549a8909ff814b85dd73e609/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
