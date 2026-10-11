# Prediction Market Analysis - Does an existing market file prove that all its trades were collected?

**Decision question:** Does an existing market file prove that all its trades were collected?

| Field | Review |
| --- | --- |
| Upstream | [Jon-Becker/prediction-market-analysis](https://github.com/Jon-Becker/prediction-market-analysis) |
| Primary area | Market Data & Ingestion |
| Source commit | [9afe7a1cb8fd5acb207fb01027d6114a414f0cd2](https://github.com/Jon-Becker/prediction-market-analysis/commit/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Indexes prediction-market trades and tests one interrupted backfill path. A Kalshi ticker with partial saved data may be skipped on the next run. |

## What this project does

A prediction-market research repository with Kalshi and Polymarket indexers plus public datasets.

## Mechanism inspected

The Kalshi trade indexer loads persisted trade IDs and market tickers to avoid duplicate rows; a separate Polymarket backfill test checks cursor recovery after interruption.

## Limitation that matters

Kalshi tickers with any saved trade are excluded from subsequent fetching, so a partially collected ticker can be mistaken for complete. The Polymarket resume test does not establish completeness of that Kalshi path.

## Practical check for a trading system

Track completion per market and time interval, not mere presence of rows; separately test retry after a partial ticker download.

## Why this score

3/5. The source illustrates both an explicit cursor recovery test and a precise incomplete-market failure mode.

## Source trail

[README](https://github.com/Jon-Becker/prediction-market-analysis/blob/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2/README.md#L34); [src/indexers/kalshi/trades.py](https://github.com/Jon-Becker/prediction-market-analysis/blob/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2/src/indexers/kalshi/trades.py#L43); [src/indexers/kalshi/trades.py](https://github.com/Jon-Becker/prediction-market-analysis/blob/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2/src/indexers/kalshi/trades.py#L66); [tests/test_backfill_cursor.py](https://github.com/Jon-Becker/prediction-market-analysis/blob/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2/tests/test_backfill_cursor.py#L55); [License text](https://github.com/Jon-Becker/prediction-market-analysis/blob/9afe7a1cb8fd5acb207fb01027d6114a414f0cd2/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
