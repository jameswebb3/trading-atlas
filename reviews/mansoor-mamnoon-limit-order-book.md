# Limit Order Book Engine - How does reconstruction record a gap it cannot repair?

**Decision question:** How does reconstruction record a gap it cannot repair?

| Field | Review |
| --- | --- |
| Upstream | [mansoor-mamnoon/limit-order-book](https://github.com/mansoor-mamnoon/limit-order-book) |
| Primary area | Market Data & Ingestion |
| Source commit | [78e1fb0e0563388456e5030d858ef43d6407bed3](https://github.com/mansoor-mamnoon/limit-order-book/commit/78e1fb0e0563388456e5030d858ef43d6407bed3) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The reconstructor increments a gap counter, advances to a later REST snapshot when present and emits an explicit gap_no_snapshot record otherwise. Resynchronizing to a later snapshot leaves the intervening state unobserved; the book cannot support fill claims for that interval. |

## What this project does

A C++ book engine with Python L2 capture, reconstruction and validation tools.

## Mechanism inspected

The reconstructor increments a gap counter, advances to a later REST snapshot when present and emits an explicit gap_no_snapshot record otherwise.

## Limitation that matters

Resynchronizing to a later snapshot leaves the intervening state unobserved; the book cannot support fill claims for that interval.

## Practical check for a trading system

Mark gap intervals unusable for replay rather than interpolating an apparently continuous book.

## Why this score

3/5. The code exposes both repaired and unrepaired gaps in output records.

## Source trail

[README](https://github.com/mansoor-mamnoon/limit-order-book/blob/78e1fb0e0563388456e5030d858ef43d6407bed3/README.md#L1); [docs/bench.md](https://github.com/mansoor-mamnoon/limit-order-book/blob/78e1fb0e0563388456e5030d858ef43d6407bed3/docs/bench.md#L1); [python/orderbook_tools/reconstruct.py](https://github.com/mansoor-mamnoon/limit-order-book/blob/78e1fb0e0563388456e5030d858ef43d6407bed3/python/orderbook_tools/reconstruct.py#L315).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
