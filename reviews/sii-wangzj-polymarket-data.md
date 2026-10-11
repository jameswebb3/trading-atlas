# Polymarket Data - Does a failed chain range remain distinguishable from a range with no trades?

**Decision question:** Does a failed chain range remain distinguishable from a range with no trades?

| Field | Review |
| --- | --- |
| Upstream | [SII-WANGZJ/Polymarket_data](https://github.com/SII-WANGZJ/Polymarket_data) |
| Primary area | Market Data & Ingestion |
| Source commit | [188eee28f09ba83d79c125bfb367f72ac93962c4](https://github.com/SII-WANGZJ/Polymarket_data/commit/188eee28f09ba83d79c125bfb367f72ac93962c4) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Keeps failed block ranges for targeted refetch rather than treating them as empty. Repair outputs still need coverage and duplicate-event reconciliation. |

## What this project does

A Polymarket on-chain dataset and fetch/clean pipeline for exchange events.

## Mechanism inspected

A repair tool reads explicit failed block intervals, refetches each interval, and distinguishes an RPC failure from a successful empty-log response before writing separate repaired Parquet outputs.

## Limitation that matters

This script does not by itself prove final chain coverage or merge safety: repaired parts need block-range and event-ID checks against the original dataset. Polymarket on-chain fills are also later than a live CLOB decision.

## Practical check for a trading system

Keep failed ranges durable and verify repaired block coverage, deduplication and decision-time availability before research joins.

## Why this score

3/5. The failed-versus-empty distinction is a concrete data-integrity pattern; end-to-end completeness remains to be certified.

## Source trail

[README](https://github.com/SII-WANGZJ/Polymarket_data/blob/188eee28f09ba83d79c125bfb367f72ac93962c4/README.md#L44); [polymarket/tools/refetch_failed_blocks.py](https://github.com/SII-WANGZJ/Polymarket_data/blob/188eee28f09ba83d79c125bfb367f72ac93962c4/polymarket/tools/refetch_failed_blocks.py#L38); [polymarket/tools/refetch_failed_blocks.py](https://github.com/SII-WANGZJ/Polymarket_data/blob/188eee28f09ba83d79c125bfb367f72ac93962c4/polymarket/tools/refetch_failed_blocks.py#L97); [License text](https://github.com/SII-WANGZJ/Polymarket_data/blob/188eee28f09ba83d79c125bfb367f72ac93962c4/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
