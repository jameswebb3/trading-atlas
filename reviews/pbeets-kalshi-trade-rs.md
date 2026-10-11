# kalshi-trade-rs - What if a book delta has an invalid numeric field?

**Decision question:** What if a book delta has an invalid numeric field?

| Field | Review |
| --- | --- |
| Upstream | [pbeets/kalshi-trade-rs](https://github.com/pbeets/kalshi-trade-rs) |
| Primary area | Market Data & Ingestion |
| Source commit | [bfa3b47dacefad4ffa2022dc025770870985176a](https://github.com/pbeets/kalshi-trade-rs/commit/bfa3b47dacefad4ffa2022dc025770870985176a) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It builds YES and NO levels from snapshots and applies delta quantity by price. Parse failures become 0.0 through unwrap_or, possibly turning bad input into valid-looking zero. |

## What this project does

A Rust Kalshi client with snapshot and delta book state.

## Mechanism inspected

It builds YES and NO levels from snapshots and applies delta quantity by price.

## Limitation that matters

Parse failures become 0.0 through unwrap_or, possibly turning bad input into valid-looking zero.

## Practical check for a trading system

Reject malformed values and invalidate the book instead of substituting zero.

## Why this score

2/5. Concrete reconstruction, but weak parse integrity.

## Source trail

[README](https://github.com/pbeets/kalshi-trade-rs/blob/bfa3b47dacefad4ffa2022dc025770870985176a/README.md#L1); [src/orderbook/state.rs](https://github.com/pbeets/kalshi-trade-rs/blob/bfa3b47dacefad4ffa2022dc025770870985176a/src/orderbook/state.rs#L62); [src/orderbook/state.rs](https://github.com/pbeets/kalshi-trade-rs/blob/bfa3b47dacefad4ffa2022dc025770870985176a/src/orderbook/state.rs#L77); [Root license](https://github.com/pbeets/kalshi-trade-rs/blob/bfa3b47dacefad4ffa2022dc025770870985176a/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
