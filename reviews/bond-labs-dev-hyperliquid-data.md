# hyperliquid-data - Will a partial Hyperliquid archive day be mistaken for complete history?

**Decision question:** Will a partial Hyperliquid archive day be mistaken for complete history?

| Field | Review |
| --- | --- |
| Upstream | [bond-labs-dev/hyperliquid-data](https://github.com/bond-labs-dev/hyperliquid-data) |
| Primary area | Market Data Ingestion |
| Source commit | [84890cb59bb652dd0f8b250a79c12b98a8967605](https://github.com/bond-labs-dev/hyperliquid-data/commit/84890cb59bb652dd0f8b250a79c12b98a8967605) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Requires all 24 hourly archive objects before writing a daily trade or L2 Parquet file and keeps exchange and node timestamps separate. The L2 parser substitutes exchange time when node time is invalid, so that fallback cannot measure capture latency; 24 objects also do not prove every record within them is valid. |

## What this project does

A command-line extractor for Hyperliquid candles, funding, L2 snapshots, trades, fills and liquidations. The inspected paths read the exchange archive and write per-day Parquet; requester-pays cost is surfaced before large pulls.

## Mechanism inspected

The shared S3 iterator counts found and missing hourly objects and raises on non-404 fetch errors. The trades path downloads each all-coin hour once, keeps taker rows and deduplicates by trade ID. Trades and L2 paths refuse to cache a day when fewer than 24 hours were found, so a later run can retry an archive still publishing.

## Limitation that matters

Completeness is measured at the object level. Malformed JSON rows and invalid book levels are skipped, so 24/24 objects does not certify record-level coverage. L2 preserves exchange and node clocks when parseable, but replaces invalid node time with exchange time; that row cannot support a real latency estimate. This is source inspection, not independent validation of archive contents.

## Practical check for a trading system

For historical market-data decisions, record object-hour coverage, row rejects and timestamp-origin status per partition. Do not let a missing or fallback receipt clock enter latency or available-at calculations as an observed arrival.

## Why this score

4/5 because the source implements a directly useful Hyperliquid archive completeness gate and separate clocks, with clear residual limits at row and timestamp level.

## Source trail

[README](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/README.md#L72); [Hourly fetch and fault semantics](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/src/hyperliquid_data/s3io.py#L125); [Trades completeness gate](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/src/hyperliquid_data/sources/trades.py#L129); [L2 timestamp fallback](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/src/hyperliquid_data/sources/l2book.py#L126); [L2 completeness gate](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/src/hyperliquid_data/sources/l2book.py#L274); [License](https://github.com/bond-labs-dev/hyperliquid-data/blob/84890cb59bb652dd0f8b250a79c12b98a8967605/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
