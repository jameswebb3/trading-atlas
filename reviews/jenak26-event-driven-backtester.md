# Event-Driven Backtester - Can a strategy read future bars or fill at the price it just observed?

**Decision question:** Can a strategy read future bars or fill at the price it just observed?

| Field | Review |
| --- | --- |
| Upstream | [Jenak26/event-driven-backtester](https://github.com/Jenak26/event-driven-backtester) |
| Primary area | Backtesting & Simulation |
| Source commit | [a07dbf72608ace5617c7b2a2810ce00094746294](https://github.com/Jenak26/event-driven-backtester/commit/a07dbf72608ace5617c7b2a2810ce00094746294) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Restricts strategy reads to elapsed bars and routes orders to the next bar's open. A next-open rule does not model liquidity, and a vanished symbol can bias the historical universe. |

## What this project does

An equities research engine with a one-bar cursor, event queue and next-bar-open broker.

## Mechanism inspected

The data handler slices historical bars only through its current cursor; the broker requests the next open and refuses to fill when no next bar exists. This makes two common lookahead routes explicit in code.

## Limitation that matters

Next-open execution still assumes the order can trade at that open plus configured costs, with no order-book or queue evidence. The README documents a delisted equity that the data source no longer supplies, so universe survivorship also needs care.

## Practical check for a trading system

Keep decision-time data access and execution-time price lookup as separate interfaces, then test missing next bars and disappearing symbols.

## Why this score

3/5 because The structural timing guard is directly useful, but daily-bar fills and external universe availability limit execution inference.

## Source trail

[README](https://github.com/Jenak26/event-driven-backtester/blob/a07dbf72608ace5617c7b2a2810ce00094746294/README.md#L177); [backtester/data.py](https://github.com/Jenak26/event-driven-backtester/blob/a07dbf72608ace5617c7b2a2810ce00094746294/backtester/data.py#L38); [backtester/execution.py](https://github.com/Jenak26/event-driven-backtester/blob/a07dbf72608ace5617c7b2a2810ce00094746294/backtester/execution.py#L14); [License text](https://github.com/Jenak26/event-driven-backtester/blob/a07dbf72608ace5617c7b2a2810ce00094746294/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
