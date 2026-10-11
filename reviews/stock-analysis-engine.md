# A successful cache read can return no market data

**Decision question:** Does a successful data-access status mean a usable observation exists?

| Field | Review |
| --- | --- |
| Upstream | [Stock Analysis Engine](https://github.com/AlgoTraders/stock-analysis-engine) |
| Primary area | Market Data & Ingestion |
| Source commit | [10d296b8352af4e13b92a73757056e50bb79ebb6](https://github.com/AlgoTraders/stock-analysis-engine/commit/10d296b8352af4e13b92a73757056e50bb79ebb6) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/AlgoTraders/stock-analysis-engine/blob/10d296b8352af4e13b92a73757056e50bb79ebb6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The Redis helper returns SUCCESS even when a key contains no data, and its expire parameter is documented as unused. It is a useful caution for market-data adapters: transport success, observation presence, and freshness need separate checks. The wider project targets equity feeds. |

## Mechanism worth inspecting

The [overview](https://github.com/AlgoTraders/stock-analysis-engine/blob/10d296b8352af4e13b92a73757056e50bb79ebb6/README.rst#L4-L19) describes distributed equity datafeeds; the [dataset guide](https://github.com/AlgoTraders/stock-analysis-engine/blob/10d296b8352af4e13b92a73757056e50bb79ebb6/docs/source/load_algo_dataset_from_redis.rst#L1-L5) identifies Redis-backed backtests. In the [cache helper](https://github.com/AlgoTraders/stock-analysis-engine/blob/10d296b8352af4e13b92a73757056e50bb79ebb6/analysis_engine/get_data_from_redis_key.py#L28-L54), expire is not an implemented freshness check. The [missing-key branch](https://github.com/AlgoTraders/stock-analysis-engine/blob/10d296b8352af4e13b92a73757056e50bb79ebb6/analysis_engine/get_data_from_redis_key.py#L141-L152) returns SUCCESS with an empty data field.

## Important limit

This is an observation about the helper's contract, not proof that every caller accepts missing data. We did not inspect the full caller chain. A usable adapter must reject absent or stale values separately.

## Questions to take into your own design

- Does the caller distinguish absent, stale, and available data?
- Is cache age based on receipt time or the underlying observation's publication time?

## Why this score for a trading system

2/5: The success-without-data branch exposes a precise ingestion-contract risk, but this narrow equity-cache path is not a complete crypto feed design.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
