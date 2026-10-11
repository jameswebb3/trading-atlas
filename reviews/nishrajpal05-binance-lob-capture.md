# Binance LOB Capture - Does a detected sequence gap invalidate the local book before writing a snapshot?

**Decision question:** Does a detected sequence gap invalidate the local book before writing a snapshot?

| Field | Review |
| --- | --- |
| Upstream | [nishrajpal05/binance-lob-capture](https://github.com/nishrajpal05/binance-lob-capture) |
| Primary area | Market Data & Ingestion |
| Source commit | [b5418b3d1ca2373f53c52fab864156117637d593](https://github.com/nishrajpal05/binance-lob-capture/commit/b5418b3d1ca2373f53c52fab864156117637d593) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The book identifies a mismatch between the previous update ID and the incoming delta predecessor. It still applies that delta, marks the book synced and writes a top-five snapshot; replay only increments a gap counter. The snapshot may therefore contain an invalid continuation. |

## What this project does

A C++ Binance depth capture and replay tool.

## Mechanism inspected

The book identifies a mismatch between the previous update ID and the incoming delta predecessor.

## Limitation that matters

It still applies that delta, marks the book synced and writes a top-five snapshot; replay only increments a gap counter. The snapshot may therefore contain an invalid continuation.

## Practical check for a trading system

Invalidate the book on a gap and require a new snapshot before publishing levels.

## Why this score

2/5. The code illustrates why detecting a gap is insufficient if invalid state still escapes.

## Source trail

[README](https://github.com/nishrajpal05/binance-lob-capture/blob/b5418b3d1ca2373f53c52fab864156117637d593/README.md#L1); [src/order_book.cpp](https://github.com/nishrajpal05/binance-lob-capture/blob/b5418b3d1ca2373f53c52fab864156117637d593/src/order_book.cpp#L3); [src/order_book.cpp](https://github.com/nishrajpal05/binance-lob-capture/blob/b5418b3d1ca2373f53c52fab864156117637d593/src/order_book.cpp#L36); [src/replay.cpp](https://github.com/nishrajpal05/binance-lob-capture/blob/b5418b3d1ca2373f53c52fab864156117637d593/src/replay.cpp#L162); [src/replay.cpp](https://github.com/nishrajpal05/binance-lob-capture/blob/b5418b3d1ca2373f53c52fab864156117637d593/src/replay.cpp#L166).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
