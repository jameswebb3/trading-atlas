# openhl - Can position accounting be replayed from the same fill sequence?

**Decision question:** Can position accounting be replayed from the same fill sequence?

| Field | Review |
| --- | --- |
| Upstream | [psyto/openhl](https://github.com/psyto/openhl) |
| Primary area | Portfolio & Risk |
| Source commit | [9f1b82436ccf31bc1778367aeedbe3a900f17233](https://github.com/psyto/openhl/commit/9f1b82436ccf31bc1778367aeedbe3a900f17233) |
| Reviewed | 2026-10-11 |
| Declared license | MIT OR Apache-2.0 (Cargo.toml) |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Separates fill-driven position/PnL transitions from funding and fee cash movements. A pure clearing rule does not by itself recover missing fills or certify venue semantics. |

## What this project does

An educational Hyperliquid-shaped exchange implementation with a pure clearing state machine and separate funding/liquidation components.

## Mechanism inspected

The clearing module applies fills to account positions, combines same-direction lots by weighted average and realizes PnL on reductions. It treats fees and funding as separate cash movements rather than hiding them inside a fill price.

## Limitation that matters

The repository states active development moved elsewhere and explicitly says this clearing crate is not an event-sourced durable account store or fee model. Exchange-shape implementation is not evidence of Hyperliquid production behavior.

## Practical check for a trading system

Use a pure fill-to-position oracle for accounting tests, while sourcing real fills, fees, funding and restart recovery from separate audited records.

## Why this score

3/5 because A direct accounting decomposition is visible, with educational and durability boundaries openly stated.

## Source trail

[README](https://github.com/psyto/openhl/blob/9f1b82436ccf31bc1778367aeedbe3a900f17233/README.md#L1); [docs/architecture.md](https://github.com/psyto/openhl/blob/9f1b82436ccf31bc1778367aeedbe3a900f17233/docs/architecture.md#L1); [crates/clearing/src/lib.rs](https://github.com/psyto/openhl/blob/9f1b82436ccf31bc1778367aeedbe3a900f17233/crates/clearing/src/lib.rs#L1); [crates/clearing/src/lib.rs](https://github.com/psyto/openhl/blob/9f1b82436ccf31bc1778367aeedbe3a900f17233/crates/clearing/src/lib.rs#L34).

[Cargo.toml](https://github.com/psyto/openhl/blob/9f1b82436ccf31bc1778367aeedbe3a900f17233/Cargo.toml#L22).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
