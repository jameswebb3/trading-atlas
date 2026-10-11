# Kalshi Dashboard: Does a fresh fetch timestamp prove every market record is current and complete?

**Decision question:** Does a fresh fetch timestamp prove every market record is current and complete?

| Field | Review |
| --- | --- |
| Upstream | [epunzal2/kalshi_dashboard](https://github.com/epunzal2/kalshi_dashboard) |
| Primary area | Market Data & Ingestion |
| Source commit | [4352904b0b2007f78d78f95f31ac02b254955ae8](https://github.com/epunzal2/kalshi_dashboard/commit/4352904b0b2007f78d78f95f31ac02b254955ae8) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The client follows cursor pages until the API supplies no next cursor. The fetcher adds one fetch_timestamp to each returned market and appends snapshots to per-market JSON. The dashboard scans saved records and uses the latest timestamp anywhere to set a freshness flag. No cycle or duplicate cursor guard appears in this client path. The newest successful fetch can hide stale markets, skipped tickers or incomplete pages. Collection time is not source event time; the code does not establish a historical backfill. |

## What this project does

Paginates Kalshi markets and appends fetched snapshots with a collection timestamp. Its dashboard calls the dataset fresh if any stored record has a recent fetch timestamp; that does not prove per-market freshness or historical coverage.

## Mechanism inspected

The client follows cursor pages until the API supplies no next cursor. The fetcher adds one fetch_timestamp to each returned market and appends snapshots to per-market JSON. The dashboard scans saved records and uses the latest timestamp anywhere to set a freshness flag.

## Limitation that matters

No cycle or duplicate cursor guard appears in this client path. The newest successful fetch can hide stale markets, skipped tickers or incomplete pages. Collection time is not source event time; the code does not establish a historical backfill.

## Practical check for a trading system

For each requested series, record the request window, cursor chain, page count, market IDs, source timestamp and receipt timestamp. Compute freshness and coverage for each entity; flag a missing entity even when another market refreshed.

## Why this score

2/5 transferable: a concrete data-quality counterexample on a relevant venue, but the dashboard design is a small GCP snapshot pipeline and not a robust backfill reference.

## Source trail

[README.md](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/README.md#L1); [src/clients.py](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/src/clients.py#L170); [src/data_fetcher.py](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/src/data_fetcher.py#L172); [src/data_fetcher.py](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/src/data_fetcher.py#L242); [src/app.py](https://github.com/epunzal2/kalshi_dashboard/blob/4352904b0b2007f78d78f95f31ac02b254955ae8/src/app.py#L75)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
