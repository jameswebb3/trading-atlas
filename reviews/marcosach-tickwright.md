# Tickwright - What should a failed venue read do to reconciliation?

**Decision question:** What should a failed venue read do to reconciliation?

| Field | Review |
| --- | --- |
| Upstream | [MarcosACH/tickwright](https://github.com/MarcosACH/tickwright) |
| Primary area | Execution & Exchange Integration |
| Source commit | [44aa9526632c1d8cb652e39f6055f27797ff252f](https://github.com/MarcosACH/tickwright/commit/44aa9526632c1d8cb652e39f6055f27797ff252f) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | A failed send freezes the reconciliation cycle, while an unreadable response body is charged to the affected order and escalated on repeated failure. The code establishes an internal safety policy, not proof that a specific venue reports all delayed fills or terminal states. |

## What this project does

An event-driven trading engine with durable order state and venue reconciliation.

## Mechanism inspected

A failed send freezes the reconciliation cycle, while an unreadable response body is charged to the affected order and escalated on repeated failure.

## Limitation that matters

The code establishes an internal safety policy, not proof that a specific venue reports all delayed fills or terminal states.

## Practical check for a trading system

Test failed-send and malformed-body paths separately, with no ghost deletion on an outage.

## Why this score

4/5. The split failure policy is a concrete model for fail-closed live reconciliation.

## Source trail

[README](https://github.com/MarcosACH/tickwright/blob/44aa9526632c1d8cb652e39f6055f27797ff252f/README.md#L1); [docs/adr/0009-recovery-snapshot-plus-reconcile.md](https://github.com/MarcosACH/tickwright/blob/44aa9526632c1d8cb652e39f6055f27797ff252f/docs/adr/0009-recovery-snapshot-plus-reconcile.md#L1); [src/tickwright/engine/reconcile.py](https://github.com/MarcosACH/tickwright/blob/44aa9526632c1d8cb652e39f6055f27797ff252f/src/tickwright/engine/reconcile.py#L286); [Root license](https://github.com/MarcosACH/tickwright/blob/44aa9526632c1d8cb652e39f6055f27797ff252f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
