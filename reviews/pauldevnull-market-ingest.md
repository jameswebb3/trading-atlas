# market-ingest - When should an absent candle become a known gap?

**Decision question:** When should an absent candle become a known gap?

| Field | Review |
| --- | --- |
| Upstream | [pauldevnull/market-ingest](https://github.com/pauldevnull/market-ingest) |
| Primary area | Market Data & Ingestion |
| Source commit | [f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d](https://github.com/pauldevnull/market-ingest/commit/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Refetches missing candle buckets and records unresolved ones so backfill does not loop forever. A successful empty provider response is not evidence of market-wide absence. |

## What this project does

A market-data pipeline with provider adapters, historical backfill and a distinct gap-scan phase.

## Mechanism inspected

The scanner obtains gaps from stored candles, refetches their surrounding range and writes only returned gap buckets. It records still-missing buckets separately as known gaps after the provider iteration ends.

## Limitation that matters

The code reaches the same still-missing branch when a provider successfully yields zero candles; this marks absence as confirmed from that provider call, not as proof that the market never traded. The README also notes a DST edge in time-step gap enumeration.

## Practical check for a trading system

Store source, request window and response status with known gaps so future provider changes can trigger rechecks.

## Why this score

3/5 because A clear reconciliation phase and explicit unresolved bucket state are useful, but provider silence has narrower meaning than market-level absence.

## Source trail

[README](https://github.com/pauldevnull/market-ingest/blob/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d/README.md#L45); [docs/architecture.md](https://github.com/pauldevnull/market-ingest/blob/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d/docs/architecture.md#L36); [src/ingestion/gap-scanner.ts](https://github.com/pauldevnull/market-ingest/blob/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d/src/ingestion/gap-scanner.ts#L64); [src/ingestion/gap-scanner.ts](https://github.com/pauldevnull/market-ingest/blob/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d/src/ingestion/gap-scanner.ts#L86); [License text](https://github.com/pauldevnull/market-ingest/blob/f7acbb0dd8b63cfc8c071d98e20d08f1d88f465d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
