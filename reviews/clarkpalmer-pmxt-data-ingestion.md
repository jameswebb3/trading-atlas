# pmxt-data-ingestion - When should a historical market be marked complete in a checkpoint?

**Decision question:** When should a historical market be marked complete in a checkpoint?

| Field | Review |
| --- | --- |
| Upstream | [clarkpalmer/pmxt-data-ingestion](https://github.com/clarkpalmer/pmxt-data-ingestion) |
| Primary area | Market Data & Ingestion |
| Source commit | [46e226096681837752a03f961cea3f913a31dea4](https://github.com/clarkpalmer/pmxt-data-ingestion/commit/46e226096681837752a03f961cea3f913a31dea4) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Shows trade and full-book coverage while enriching archived markets. Its completion checkpoint can advance before the corresponding Parquet rows are durable. |

## What this project does

Scripts for downloading PMXT archive snapshots and enriching Polymarket crypto markets with trades and outcomes.

## Mechanism inspected

A market snapshot exposes separate trade and full-book coverage intervals. Trade enrichment tracks completed condition IDs and writes rows to a Parquet file after each batch.

## Limitation that matters

The checkpoint saves the condition IDs before the batch rows are written to Parquet. A crash between those steps can make an unwritten market look complete on restart. Per-market fetch exceptions are skipped without a failure ledger.

## Practical check for a trading system

Publish data parts atomically before advancing a durable completion cursor, then compare persisted row coverage to checkpoint state.

## Why this score

2/5. A practical archive-coverage view is present, but checkpoint ordering creates a concrete silent-loss risk.

## Source trail

[README](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/README.md#L3); [snapshot.py](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/snapshot.py#L105); [enrich.py](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/enrich.py#L79); [enrich.py](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/enrich.py#L129); [enrich.py](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/enrich.py#L136); [License text](https://github.com/clarkpalmer/pmxt-data-ingestion/blob/46e226096681837752a03f961cea3f913a31dea4/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
