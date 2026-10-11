# hyperliquid-data-pipeline — Capture raw frames before a lossy processing queue

**Decision question:** Can a low-latency consumer shed frames without silently corrupting the research archive?

| Field | Review |
| --- | --- |
| Upstream | [Giri-Aayush/hyperliquid-data-pipeline](https://github.com/Giri-Aayush/hyperliquid-data-pipeline) |
| Primary area | Market Data & Ingestion |
| Source commit | [a35b42d4144f9ccf48de3b5bafc37cf8d6183714](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/commit/a35b42d4144f9ccf48de3b5bafc37cf8d6183714) |
| Reviewed | 2026-10-10 |
| Declared license | MIT with additional disclaimer |
| Review depth | 3/3: README, relevant source and relevant test source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its raw-frame spool receives websocket frames before parsing and independently of a drop-oldest processing queue, preserving a separate archive path with receive timestamps and overflow counts. The spool itself is bounded and can drop when its writer starves; trade-gap backfill may return zero because the inspected archive path does not currently supply trades. |

## What this project does

A Hyperliquid data pipeline combining live WebSocket collection, historical files, order-book reconstruction, feature processing and execution simulation. [Project README](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/README.md#L1).

## Mechanism inspected

RawSpool appends each frame with wall and monotonic receive stamps before parser interpretation. Enqueue returns false and increments a drop counter on overflow. A test sends 50 frames through a three-slot lossy processing queue and checks that all 50 reached the spool. [Raw spool](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/src/hyperliquid_pipeline/collectors/spool.py#L1).

## Limitation that matters

The spool's writer queue is also finite, so the name lossless is conditional on disk throughput and alarm handling. The reconnect backfill path treats empty trade archive results as retryable, while the README says that archive does not provide the needed trade stream. This is a source review, not a runtime or security test.

## Practical check for a trading system

Separate a durable raw-feed capture contract from a freshest-wins signal queue. Gate studies when the raw spool drops or when reconnect trade gaps remain unrecovered.

## Why this score

4/5 because raw-before-parse capture and explicit overflow accounting address a direct Hyperliquid data-quality risk, with targeted source tests read but no runtime verification here.

## Source trail

[README](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/README.md#L1); [Raw spool](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/src/hyperliquid_pipeline/collectors/spool.py#L1); [Spool tests](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/tests/test_spool.py#L34); [Backfill](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/src/hyperliquid_pipeline/collectors/backfill.py#L50); [L4 gap flag](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/src/hyperliquid_pipeline/book/l4_book.py#L119); [License](https://github.com/Giri-Aayush/hyperliquid-data-pipeline/blob/a35b42d4144f9ccf48de3b5bafc37cf8d6183714/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
