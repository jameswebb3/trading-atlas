# deliverator - Can reconciliation succeed from a partial Hyperliquid read?

**Decision question:** Can reconciliation succeed from a partial Hyperliquid read?

| Field | Review |
| --- | --- |
| Upstream | [erickuhn19/deliverator](https://github.com/erickuhn19/deliverator) |
| Primary area | Execution & Exchange Integration |
| Source commit | [511f7516d1a470d897339b653d2eae7daa81eb98](https://github.com/erickuhn19/deliverator/commit/511f7516d1a470d897339b653d2eae7daa81eb98) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and fail-closed tests inspected; no runtime test |
| Trading-system value | 5/5 |
| Trading-system fit | Direct |
| Executive assessment | It refuses an authoritative diff if sub-dex open orders or position snapshots are degraded, then compares account and audit state. A clean diff still depends on complete fills and audit retention; the live path was not run here. |

## What this project does

A Hyperliquid CLI and core with an audit trail and reconciliation view.

## Mechanism inspected

It refuses an authoritative diff if sub-dex open orders or position snapshots are degraded, then compares account and audit state.

Pinned tests inject a failed sub-dex order read and a degraded sub-dex position snapshot; both assert that reconciliation returns an error instead of a clean verdict. These tests were read, not run.

## Limitation that matters

A clean diff still depends on complete fills and audit retention; the live path was not run here.

## Practical check for a trading system

Fail closed on incomplete reads and preserve unknown CLOIDs until exchange evidence resolves them.

## Why this score

5/5: Pinned source tests reject degraded sub-dex order and position responses before reconciliation can report a clean account; live behavior remains unverified.

## Source trail

[README](https://github.com/erickuhn19/deliverator/blob/511f7516d1a470d897339b653d2eae7daa81eb98/README.md#L1); [internal/core/reconcile.go](https://github.com/erickuhn19/deliverator/blob/511f7516d1a470d897339b653d2eae7daa81eb98/internal/core/reconcile.go#L103); [internal/core/reconcile.go](https://github.com/erickuhn19/deliverator/blob/511f7516d1a470d897339b653d2eae7daa81eb98/internal/core/reconcile.go#L199); [fail-closed tests](https://github.com/erickuhn19/deliverator/blob/511f7516d1a470d897339b653d2eae7daa81eb98/internal/core/reconcile_test.go#L67-L100); [Root license](https://github.com/erickuhn19/deliverator/blob/511f7516d1a470d897339b653d2eae7daa81eb98/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
