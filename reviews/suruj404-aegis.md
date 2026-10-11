# Aegis - Can a rejected fill transition still mutate quantity?

**Decision question:** Can a rejected fill transition still mutate quantity?

| Field | Review |
| --- | --- |
| Upstream | [SURUJ404/Aegis](https://github.com/SURUJ404/Aegis) |
| Primary area | Execution & Exchange Integration |
| Source commit | [10bda2c593e13b42fd84c1202583f642d1929ccc](https://github.com/SURUJ404/Aegis/commit/10bda2c593e13b42fd84c1202583f642d1929ccc) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | It caps fills at remaining quantity, computes weighted average price and validates status transitions. It increments quantity and average price before validating the transition, so illegal transitions can leave mutated state. |

## What this project does

A Rust trading engine with an explicit order lifecycle state machine.

## Mechanism inspected

It caps fills at remaining quantity, computes weighted average price and validates status transitions.

## Limitation that matters

It increments quantity and average price before validating the transition, so illegal transitions can leave mutated state.

## Practical check for a trading system

Validate before mutation and test fill-before-ACK, duplicates and late terminal fills.

## Why this score

3/5. Useful lifecycle model with a concrete mutation-order risk.

## Source trail

[README](https://github.com/SURUJ404/Aegis/blob/10bda2c593e13b42fd84c1202583f642d1929ccc/README.md#L1); [docs/DATA.md](https://github.com/SURUJ404/Aegis/blob/10bda2c593e13b42fd84c1202583f642d1929ccc/docs/DATA.md#L1); [crates/execution/src/state_machine.rs](https://github.com/SURUJ404/Aegis/blob/10bda2c593e13b42fd84c1202583f642d1929ccc/crates/execution/src/state_machine.rs#L150); [crates/execution/src/state_machine.rs](https://github.com/SURUJ404/Aegis/blob/10bda2c593e13b42fd84c1202583f642d1929ccc/crates/execution/src/state_machine.rs#L130).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
