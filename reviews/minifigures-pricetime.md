# pricetime - Can an optimized matching engine match a simple reference after random order events?

**Decision question:** Can an optimized matching engine match a simple reference after random order events?

| Field | Review |
| --- | --- |
| Upstream | [Minifigures/pricetime](https://github.com/Minifigures/pricetime) |
| Primary area | Testing & Verification |
| Source commit | [4e9254823a729ea9de9270f1a122c0e0347fcd79](https://github.com/Minifigures/pricetime/commit/4e9254823a729ea9de9270f1a122c0e0347fcd79) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The differential fuzz feeds identical submit, cancel and replace events to both books, then compares emitted events and visible state. Generated operations remain within a bounded price band and the reference can share a mistaken venue assumption. |

## What this project does

A C++ price-time matching engine with a reference implementation.

## Mechanism inspected

The differential fuzz feeds identical submit, cancel and replace events to both books, then compares emitted events and visible state.

## Limitation that matters

Generated operations remain within a bounded price band and the reference can share a mistaken venue assumption.

## Practical check for a trading system

Keep a slow independent replay oracle and compare both events and book state over adversarial sequences.

## Why this score

3/5. The source checks more than output fills; it also detects hidden state divergence.

## Source trail

[README](https://github.com/Minifigures/pricetime/blob/4e9254823a729ea9de9270f1a122c0e0347fcd79/README.md#L1); [tests/test_differential.cpp](https://github.com/Minifigures/pricetime/blob/4e9254823a729ea9de9270f1a122c0e0347fcd79/tests/test_differential.cpp#L130); [Root license](https://github.com/Minifigures/pricetime/blob/4e9254823a729ea9de9270f1a122c0e0347fcd79/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
