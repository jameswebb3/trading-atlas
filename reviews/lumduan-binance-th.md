# binance-th - What does an order tracker do after the private stream reconnects?

**Decision question:** What does an order tracker do after the private stream reconnects?

| Field | Review |
| --- | --- |
| Upstream | [lumduan/binance-th](https://github.com/lumduan/binance-th) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3282061ef486263fd47dae91483182e3d7a53f91](https://github.com/lumduan/binance-th/commit/3282061ef486263fd47dae91483182e3d7a53f91) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The order tracker replaces its active-order view from REST after reconnect and rejects older execution reports by update time. The REST open-orders snapshot contains active orders only; terminal fills and prices require a separate historical ledger before declaring full account reconciliation. |

## What this project does

A typed Binance Thailand client with order and book trackers.

## Mechanism inspected

The order tracker replaces its active-order view from REST after reconnect and rejects older execution reports by update time.

## Limitation that matters

The REST open-orders snapshot contains active orders only; terminal fills and prices require a separate historical ledger before declaring full account reconciliation.

## Practical check for a trading system

Seed active state on reconnect and separately reconcile fills, cancellations and positions.

## Why this score

3/5. A useful stream-to-snapshot recovery pattern with a clear terminal-history gap.

## Source trail

[README](https://github.com/lumduan/binance-th/blob/3282061ef486263fd47dae91483182e3d7a53f91/README.md#L1); [docs/concepts/errors-and-reconciliation.md](https://github.com/lumduan/binance-th/blob/3282061ef486263fd47dae91483182e3d7a53f91/docs/concepts/errors-and-reconciliation.md#L1); [binance_th/ordertracker.py](https://github.com/lumduan/binance-th/blob/3282061ef486263fd47dae91483182e3d7a53f91/binance_th/ordertracker.py#L77); [Root license](https://github.com/lumduan/binance-th/blob/3282061ef486263fd47dae91483182e3d7a53f91/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
