# hft-market-replay - Can a fast parser still create a false complete book?

**Decision question:** Can a fast parser still create a false complete book?

| Field | Review |
| --- | --- |
| Upstream | [NITIN9181/hft-market-replay](https://github.com/NITIN9181/hft-market-replay) |
| Primary area | Market Data & Ingestion |
| Source commit | [2598dc363d27b0ec69e682348a64331ae1e6d633](https://github.com/NITIN9181/hft-market-replay/commit/2598dc363d27b0ec69e682348a64331ae1e6d633) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | It converts bid and ask updates to fixed-point deltas and carries the first update ID. This parser drops JSON errors and does not check snapshot bridging or the final update ID here. |

## What this project does

A C++ ingestion and replay prototype for Binance depth messages.

## Mechanism inspected

It converts bid and ask updates to fixed-point deltas and carries the first update ID.

## Limitation that matters

This parser drops JSON errors and does not check snapshot bridging or the final update ID here.

## Practical check for a trading system

Validate snapshot-to-delta continuity and count discarded frames.

## Why this score

1/5. Relevant speed prototype, without an integrity contract at this path.

## Source trail

[README](https://github.com/NITIN9181/hft-market-replay/blob/2598dc363d27b0ec69e682348a64331ae1e6d633/README.md#L1); [src/ingestor/binance_parser.cpp](https://github.com/NITIN9181/hft-market-replay/blob/2598dc363d27b0ec69e682348a64331ae1e6d633/src/ingestor/binance_parser.cpp#L77).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
