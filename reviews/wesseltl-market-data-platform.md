# Market Data Platform - Should a historical REST candle invent trade-derived fields?

**Decision question:** Should a historical REST candle invent trade-derived fields?

| Field | Review |
| --- | --- |
| Upstream | [wesseltl/market-data-platform](https://github.com/wesseltl/market-data-platform) |
| Primary area | Data Quality & Lineage |
| Source commit | [49fe76a981efef50b6273e2695b5ea51a35e2086](https://github.com/wesseltl/market-data-platform/commit/49fe76a981efef50b6273e2695b5ea51a35e2086) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation, and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Leaves trade-derived VWAP absent on REST backfill and checks candle-bucket coverage explicitly. A complete candle grid does not prove that every trade or volume field is complete. |

## What this project does

A small crypto pipeline with live trade aggregation, REST backfill, quality reports and descriptive analytics.

## Mechanism inspected

Trade aggregation computes buckets and VWAP from prints; the quality function enumerates missing expected time buckets and reports coverage. Tests cover bucket boundaries and simple gaps.

## Limitation that matters

The README states that backfilled REST candles leave VWAP null because the underlying trades were not observed. The gap checker reasons from uniform intervals, so exchange outages or venue calendar rules require explicit treatment.

## Practical check for a trading system

Preserve field-level provenance: null for an unobservable metric, and a separate coverage report for missing buckets.

## Why this score

3/5 because The source makes completeness and non-fabrication explicit; it remains a small single-venue example.

## Source trail

[README](https://github.com/wesseltl/market-data-platform/blob/49fe76a981efef50b6273e2695b5ea51a35e2086/README.md#L86); [marketdata/aggregator.py](https://github.com/wesseltl/market-data-platform/blob/49fe76a981efef50b6273e2695b5ea51a35e2086/marketdata/aggregator.py#L18); [marketdata/quality.py](https://github.com/wesseltl/market-data-platform/blob/49fe76a981efef50b6273e2695b5ea51a35e2086/marketdata/quality.py#L17); [tests/test_core.py](https://github.com/wesseltl/market-data-platform/blob/49fe76a981efef50b6273e2695b5ea51a35e2086/tests/test_core.py#L83); [License text](https://github.com/wesseltl/market-data-platform/blob/49fe76a981efef50b6273e2695b5ea51a35e2086/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
