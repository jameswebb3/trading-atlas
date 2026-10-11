# kalshi-rs - Does a sequence gap actually stop a local Kalshi book from being trusted?

**Decision question:** Does a sequence gap actually stop a local Kalshi book from being trusted?

| Field | Review |
| --- | --- |
| Upstream | [rmadev01/kalshi-rs](https://github.com/rmadev01/kalshi-rs) |
| Primary area | Market Data & Ingestion |
| Source commit | [11527fc39305abeabd7b3038ee5a74921b72447b](https://github.com/rmadev01/kalshi-rs/commit/11527fc39305abeabd7b3038ee5a74921b72447b) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Marks a Kalshi book stale on sequence gaps and skips further deltas until a new snapshot restores synchronization. In an unsynchronized state, a skipped delta returns Ok(true); callers must still check book state and arrange resync. |

## What this project does

A Rust Kalshi API and WebSocket client with an order-book manager that tracks initial snapshots, deltas and resync state.

## Mechanism inspected

A market starts WaitingForSnapshot. A snapshot replaces book state and marks it synchronized; a delta with a missing sequence marks NeedsResync and returns a typed SequenceGap error. Later deltas are skipped while the book remains unsynchronized.

## Limitation that matters

The manager marks recovery needed but the inspected path does not itself fetch and apply the replacement snapshot. Its apply_delta helper returns Ok(true) when skipping a delta in an unsynchronized state, so a caller must inspect the state rather than interpret that boolean as evidence of application.

## Practical check for a trading system

Expose the book state to every consumer; after a gap, block decisions until a fresh snapshot is applied and confirm that skipped deltas cannot look like an updated book.

## Why this score

3/5 because Direct sequence-gap invalidation is implemented with tests, but the success-like skip return and separate resnapshot responsibility deserve attention.

## Source trail

[README order-book feature](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/README.md#L265); [State and gap semantics](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/src/orderbook/manager.rs#L11); [Snapshot sync](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/src/orderbook/manager.rs#L228); [Skipped delta and gap](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/src/orderbook/manager.rs#L273); [Gap test](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/src/orderbook/manager.rs#L433); [License](https://github.com/rmadev01/kalshi-rs/blob/11527fc39305abeabd7b3038ee5a74921b72447b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
