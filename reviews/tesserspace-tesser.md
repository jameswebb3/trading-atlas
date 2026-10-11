# Tesser - Can local and exchange state be compared without immediately mutating either?

**Decision question:** Can local and exchange state be compared without immediately mutating either?

| Field | Review |
| --- | --- |
| Upstream | [tesserspace/tesser](https://github.com/tesserspace/tesser) |
| Primary area | Execution & Exchange Integration |
| Source commit | [6fd5b3b9a7ad286ac0606f7a00d02b9e6fc6df64](https://github.com/tesserspace/tesser/commit/6fd5b3b9a7ad286ac0606f7a00d02b9e6fc6df64) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | A stateless differ compares local and exchange snapshots, separating matched orders from local ghosts and remote-only zombies. A snapshot diff identifies disagreement but does not by itself prove why an order disappeared or recover its missing fills. |

## What this project does

A Rust quantitative-trading framework with reconciliation and a ledger.

## Mechanism inspected

A stateless differ compares local and exchange snapshots, separating matched orders from local ghosts and remote-only zombies.

## Limitation that matters

A snapshot diff identifies disagreement but does not by itself prove why an order disappeared or recover its missing fills.

## Practical check for a trading system

Produce a read-only discrepancy report before any repair and demand fill evidence for terminal conclusions.

## Why this score

3/5. The explicit diff vocabulary is useful, but repair policy must be evidence driven.

## Source trail

[README](https://github.com/tesserspace/tesser/blob/6fd5b3b9a7ad286ac0606f7a00d02b9e6fc6df64/README.md#L1); [docs/README.md](https://github.com/tesserspace/tesser/blob/6fd5b3b9a7ad286ac0606f7a00d02b9e6fc6df64/docs/README.md#L1); [tesser-cli/src/reconcile/diff.rs](https://github.com/tesserspace/tesser/blob/6fd5b3b9a7ad286ac0606f7a00d02b9e6fc6df64/tesser-cli/src/reconcile/diff.rs#L53).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
