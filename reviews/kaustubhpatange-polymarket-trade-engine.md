# polymarket-trade-engine - Will a restart recover pending orders without a torn state file?

**Decision question:** Will a restart recover pending orders without a torn state file?

| Field | Review |
| --- | --- |
| Upstream | [KaustubhPatange/polymarket-trade-engine](https://github.com/KaustubhPatange/polymarket-trade-engine) |
| Primary area | Execution & Exchange Integration |
| Source commit | [eda6759323b1b4cdb3559ca97876436c8fc231fd](https://github.com/KaustubhPatange/polymarket-trade-engine/commit/eda6759323b1b4cdb3559ca97876436c8fc231fd) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | State is serialized to a temporary file and renamed over the live state path, including pending orders and session P&L. A parse failure returns null and the inspected save path has no fsync or exchange-side reconciliation. |

## What this project does

A prediction-market execution engine with persisted market and order history.

## Mechanism inspected

State is serialized to a temporary file and renamed over the live state path, including pending orders and session P&L.

## Limitation that matters

A parse failure returns null and the inspected save path has no fsync or exchange-side reconciliation.

## Practical check for a trading system

Persist an order journal durably, then rebuild and reconcile before any post-restart submission.

## Why this score

3/5. Atomic rename helps, but it is only one part of order recovery.

## Source trail

[README](https://github.com/KaustubhPatange/polymarket-trade-engine/blob/eda6759323b1b4cdb3559ca97876436c8fc231fd/README.md#L1); [docs/GUIDE.md](https://github.com/KaustubhPatange/polymarket-trade-engine/blob/eda6759323b1b4cdb3559ca97876436c8fc231fd/docs/GUIDE.md#L1); [engine/state.ts](https://github.com/KaustubhPatange/polymarket-trade-engine/blob/eda6759323b1b4cdb3559ca97876436c8fc231fd/engine/state.ts#L44); [Root license](https://github.com/KaustubhPatange/polymarket-trade-engine/blob/eda6759323b1b4cdb3559ca97876436c8fc231fd/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
