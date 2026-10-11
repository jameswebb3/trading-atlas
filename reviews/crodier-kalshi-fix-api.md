# kalshi-fix-api - Does a typed feed model enforce integrity?

**Decision question:** Does a typed feed model enforce integrity?

| Field | Review |
| --- | --- |
| Upstream | [crodier/kalshi-fix-api](https://github.com/crodier/kalshi-fix-api) |
| Primary area | Market Data & Ingestion |
| Source commit | [4da955733593562e476cf75a78b922ac6c8ad7fd](https://github.com/crodier/kalshi-fix-api/commit/4da955733593562e476cf75a78b922ac6c8ad7fd) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The model distinguishes snapshots, deltas, trades, fills and subscription updates. These data classes do not check sequence, source time or consistency; no root license was verified. |

## What this project does

A Kalshi FIX and WebSocket API exploration with Kotlin market-data types.

## Mechanism inspected

The model distinguishes snapshots, deltas, trades, fills and subscription updates.

## Limitation that matters

These data classes do not check sequence, source time or consistency; no root license was verified.

## Practical check for a trading system

Add temporal and sequence contracts before ingesting data.

## Why this score

1/5. Relevant vocabulary; thin behavior and maintenance evidence.

## Source trail

[README](https://github.com/crodier/kalshi-fix-api/blob/4da955733593562e476cf75a78b922ac6c8ad7fd/README.md#L1); [src/commonMain/kotlin/com/fbg/api/market/MarketData.kt](https://github.com/crodier/kalshi-fix-api/blob/4da955733593562e476cf75a78b922ac6c8ad7fd/src/commonMain/kotlin/com/fbg/api/market/MarketData.kt#L33).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
