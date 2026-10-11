# order_book_server - What can order-level book diffs reveal that L2 snapshots cannot?

**Decision question:** What can order-level book diffs reveal that L2 snapshots cannot?

| Field | Review |
| --- | --- |
| Upstream | [hyperliquid-dex/order_book_server](https://github.com/hyperliquid-dex/order_book_server) |
| Primary area | Backtesting & Simulation |
| Source commit | [8b4f237904f683aca2dba21a07d87e831ead2a97](https://github.com/hyperliquid-dex/order_book_server/commit/8b4f237904f683aca2dba21a07d87e831ead2a97) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | It stores per-price ordered order IDs and refuses insertion when the referenced resting order is absent, detecting divergence from a diff. This local reconstruction is not proof of exchange matching priority or a fill model for a user account. |

## What this project does

A local order-book server implementing order-level book state from Hyperliquid-related data.

## Mechanism inspected

It stores per-price ordered order IDs and refuses insertion when the referenced resting order is absent, detecting divergence from a diff.

## Limitation that matters

This local reconstruction is not proof of exchange matching priority or a fill model for a user account.

## Practical check for a trading system

Use the divergence condition as a replay integrity test and label any inferred queue position separately from fills.

## Why this score

4/5. The explicit order-level invariant is valuable for book replay, with a clear evidence boundary.

## Source trail

[README](https://github.com/hyperliquid-dex/order_book_server/blob/8b4f237904f683aca2dba21a07d87e831ead2a97/README.md#L1); [server/src/order_book/mod.rs](https://github.com/hyperliquid-dex/order_book_server/blob/8b4f237904f683aca2dba21a07d87e831ead2a97/server/src/order_book/mod.rs#L70).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
