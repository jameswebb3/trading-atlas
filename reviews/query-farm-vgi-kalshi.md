# vgi-kalshi - Can an empty live query mean an archived market rather than no market?

**Decision question:** Can an empty live query mean an archived market rather than no market?

| Field | Review |
| --- | --- |
| Upstream | [Query-farm/vgi-kalshi](https://github.com/Query-farm/vgi-kalshi) |
| Primary area | Market Data Ingestion |
| Source commit | [a47f9d96ba635133c1ac50f7739158fa9d103658](https://github.com/Query-farm/vgi-kalshi/commit/a47f9d96ba635133c1ac50f7739158fa9d103658) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Exposes historical markets and trades separately from live tables and makes the moving archive cutoff queryable. A live endpoint can return no rows for an older settled market; the archive split must be resolved explicitly, and current order books cannot reconstruct past queue position. |

## What this project does

A read-only DuckDB/VGI worker exposing Kalshi markets, order books, candlesticks, trades, events and the historical archive as tables.

## Mechanism inspected

The historical-market function pages through archived settlements instead of materializing the entire series, exposes a matching table shape plus settlement value, and points callers to a historical_cutoff table. Archive results have a long cache TTL. Time-filter pushdown widens inclusive API bounds then applies pushed predicates again in the output batch, protecting boundary rows from premature exclusion.

## Limitation that matters

The live endpoint returns an empty result for markets moved to the archive rather than a missing-history error. A consumer that only queries live can misclassify settled markets as nonexistent. The separate archive API is a data-discovery remedy, but it does not provide a historical order-book tape or proof of passive fill. The reviewed code is a read-only interface, not an execution system.

## Practical check for a trading system

For market histories, record which side of the live/archive boundary supplied each row and treat empty results as source-status questions. Keep settlement data separate from order-book-at-decision evidence when assessing a maker strategy.

## Why this score

3/5 because the code provides a concrete direct market-data boundary and paging/filter semantics, though the venue and missing historical book limit transfer to execution studies.

## Source trail

[README and archive boundary](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/README.md#L112); [Historical page emission](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/vgi_kalshi/historical.py#L89); [Cutoff caveat](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/vgi_kalshi/historical.py#L118); [Cutoff table](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/vgi_kalshi/historical.py#L472); [Time-bound pushdown](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/vgi_kalshi/pushdown.py#L48); [License](https://github.com/Query-farm/vgi-kalshi/blob/a47f9d96ba635133c1ac50f7739158fa9d103658/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
