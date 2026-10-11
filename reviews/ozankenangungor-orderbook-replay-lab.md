# orderbook-replay-lab - Does a replay reader reject truncated binary market records?

**Decision question:** Does a replay reader reject truncated binary market records?

| Field | Review |
| --- | --- |
| Upstream | [ozankenangungor/orderbook-replay-lab](https://github.com/ozankenangungor/orderbook-replay-lab) |
| Primary area | Backtesting & Simulation |
| Source commit | [96d0aded54149a76e31d363e090a4ed1800540fc](https://github.com/ozankenangungor/orderbook-replay-lab/commit/96d0aded54149a76e31d363e090a4ed1800540fc) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The reader checks record headers and payload lengths, raising UnexpectedEof on a truncated prefix, header or payload. Binary integrity does not itself prove that all venue events were captured before the file was written. |

## What this project does

A Rust order-book replay laboratory with JSON and binary event readers.

## Mechanism inspected

The reader checks record headers and payload lengths, raising UnexpectedEof on a truncated prefix, header or payload.

## Limitation that matters

Binary integrity does not itself prove that all venue events were captured before the file was written.

## Practical check for a trading system

Fail replay on damaged framing and carry an independent source sequence or coverage manifest.

## Why this score

4/5. It provides a concrete fail-closed file boundary for deterministic replay.

## Source trail

[README](https://github.com/ozankenangungor/orderbook-replay-lab/blob/96d0aded54149a76e31d363e090a4ed1800540fc/README.md#L1); [replay/src/lib.rs](https://github.com/ozankenangungor/orderbook-replay-lab/blob/96d0aded54149a76e31d363e090a4ed1800540fc/replay/src/lib.rs#L154); [Root license](https://github.com/ozankenangungor/orderbook-replay-lab/blob/96d0aded54149a76e31d363e090a4ed1800540fc/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
