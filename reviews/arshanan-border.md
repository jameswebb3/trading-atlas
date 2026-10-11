# border - Does a depth stream resync after a sequence gap?

**Decision question:** Does a depth stream resync after a sequence gap?

| Field | Review |
| --- | --- |
| Upstream | [ArshAnan/border](https://github.com/ArshAnan/border) |
| Primary area | Market Data & Ingestion |
| Source commit | [2cb0b8642def80b2600ae78381eafad8b9e73498](https://github.com/ArshAnan/border/commit/2cb0b8642def80b2600ae78381eafad8b9e73498) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | A buffered depth stream is aligned to a REST snapshot and moves to RESYNCING when later update IDs skip the expected successor. The first-event bracket uses the snapshot ID itself, and the inspected path restarts after a gap; venue-specific Binance alignment semantics need an external protocol check. |

## What this project does

A Binance L2 reconstruction and feature-capture library.

## Mechanism inspected

A buffered depth stream is aligned to a REST snapshot and moves to RESYNCING when later update IDs skip the expected successor.

## Limitation that matters

The first-event bracket uses the snapshot ID itself, and the inspected path restarts after a gap; venue-specific Binance alignment semantics need an external protocol check.

## Practical check for a trading system

Use fixture tapes for snapshot boundary, duplicate, gap and reconnect transitions before trusting derived LOB features.

## Why this score

2/5. The state machine is inspectable, but its exact boundary contract must be validated against venue rules.

## Source trail

[README](https://github.com/ArshAnan/border/blob/2cb0b8642def80b2600ae78381eafad8b9e73498/README.md#L1); [orderbook/buffer.py](https://github.com/ArshAnan/border/blob/2cb0b8642def80b2600ae78381eafad8b9e73498/orderbook/buffer.py#L70); [Root license](https://github.com/ArshAnan/border/blob/2cb0b8642def80b2600ae78381eafad8b9e73498/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
