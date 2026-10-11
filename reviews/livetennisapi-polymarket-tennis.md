# Polymarket Tennis - Can two live feeds be joined without hiding their separate age?

**Decision question:** Can two live feeds be joined without hiding their separate age?

| Field | Review |
| --- | --- |
| Upstream | [livetennisapi/polymarket-tennis](https://github.com/livetennisapi/polymarket-tennis) |
| Primary area | Market Data & Ingestion |
| Source commit | [c5ceff488a4ef1557164f35e5de5cd6fdb1c209e](https://github.com/livetennisapi/polymarket-tennis/commit/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Keeps market and score timestamps separate and leaves ambiguous tennis settlements unresolved. The paper tape does not prove independent feed latency or executable fills. |

## What this project does

An observe-only toolkit joining Polymarket tennis markets with a live score feed and a small paper replay.

## Mechanism inspected

LiveMarketView keeps market and score as-of timestamps plus fetch timestamps separately. Its replay refuses to force settlement for retired, walkover or abandoned matches when the outcome mapping is uncertain.

## Limitation that matters

The replay builder assigns the tape timestamp to both fetch clocks, so that tape alone cannot establish the true independent latency of the original feeds. Paper marking uses observed prices, not a proven order-arrival fill.

## Practical check for a trading system

Preserve exchange-time and observed-time per source, and leave ambiguous settlement as unknown until venue rules are verified.

## Why this score

3/5. A direct cross-feed timing and settlement distinction is visible, with a clear replay evidence boundary.

## Source trail

[README](https://github.com/livetennisapi/polymarket-tennis/blob/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e/README.md#L63); [src/polymarket_tennis/join.py](https://github.com/livetennisapi/polymarket-tennis/blob/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e/src/polymarket_tennis/join.py#L55); [src/polymarket_tennis/arena/replay.py](https://github.com/livetennisapi/polymarket-tennis/blob/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e/src/polymarket_tennis/arena/replay.py#L88); [src/polymarket_tennis/arena/replay.py](https://github.com/livetennisapi/polymarket-tennis/blob/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e/src/polymarket_tennis/arena/replay.py#L104); [License text](https://github.com/livetennisapi/polymarket-tennis/blob/c5ceff488a4ef1557164f35e5de5cd6fdb1c209e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
