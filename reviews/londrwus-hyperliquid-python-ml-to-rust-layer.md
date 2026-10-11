# Axon — Separate fills from order updates

**Decision question:** Can an execution engine recover correct position state from out-of-order events?

| Field | Review |
| --- | --- |
| Upstream | [londrwus/hyperliquid-python-ml-to-rust-layer](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7563e86cf2d9413702885ea1c0728322ca6c94c9](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/commit/7563e86cf2d9413702885ea1c0728322ca6c94c9) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its ADR gives Fill and OrderUpdate distinct types, uses absolute remaining size, and places the venue client behind a GuardedClient risk gate. An ADR and local tests cannot prove recovery from every real venue gap; order updates are not a durable fill snapshot. |

## What this project does

An architecture separating Python research from a Rust Hyperliquid execution layer. [Project README](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/README.md#L7).

## Mechanism inspected

Its ADR gives Fill and OrderUpdate distinct types, uses absolute remaining size, and places the venue client behind a GuardedClient risk gate. [Implementation](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/crates/axon-execution/src/guard.rs#L696). [Related source 1](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/docs/adr/0010-execution-events-and-reconciliation.md#L38). [Related source 2](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/crates/axon-execution/src/inflight.rs#L112).

## Limitation that matters

An ADR and local tests cannot prove recovery from every real venue gap; order updates are not a durable fill snapshot. The additional Rust service adds maintenance. This is a source review, not a runtime or security test.

## Practical check for a trading system

Use trade IDs for fill deduplication, reconcile cumulative quantities against REST after reconnect, and keep the raw venue client inaccessible to strategies.

## Why this score

Directly addresses position drift and bypassable risk gates with concrete source types, but requires venue-specific recovery tests.

## Source trail

[README](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/README.md#L7); [Implementation](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/crates/axon-execution/src/guard.rs#L696); [Related source 1](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/docs/adr/0010-execution-events-and-reconciliation.md#L38); [Related source 2](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/crates/axon-execution/src/inflight.rs#L112) - [License](https://github.com/londrwus/hyperliquid-python-ml-to-rust-layer/blob/7563e86cf2d9413702885ea1c0728322ca6c94c9/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
