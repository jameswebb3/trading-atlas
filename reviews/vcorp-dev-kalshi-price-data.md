# Kalshi Price Data - Does this client establish the completeness of historical Kalshi order books?

**Decision question:** Does this client establish the completeness of historical Kalshi order books?

| Field | Review |
| --- | --- |
| Upstream | [vcorp-dev/kalshi-price-data](https://github.com/vcorp-dev/kalshi-price-data) |
| Primary area | Market Data & Ingestion |
| Source commit | [b77bd3b9e07d844fb993063f5532f86a596e17d0](https://github.com/vcorp-dev/kalshi-price-data/commit/b77bd3b9e07d844fb993063f5532f86a596e17d0) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The client forwards market and snapshot queries to DepthFeed, filters null parameters, and unwraps the response data field. The repository contains no collector, gap detection, archive audit, or independent evidence for the coverage numbers advertised in its README; historical depth is gated behind an external paid service. |

## What this project does

A thin Python client for a separate hosted Kalshi and cross-venue data aggregator.

## Mechanism inspected

The client forwards market and snapshot queries to DepthFeed, filters null parameters, and unwraps the response data field.

## Limitation that matters

The repository contains no collector, gap detection, archive audit, or independent evidence for the coverage numbers advertised in its README; historical depth is gated behind an external paid service.

## Practical check for a trading system

Treat a data API wrapper as an access path, then verify source lineage, sequence gaps and archive coverage separately.

## Why this score

1/5. Useful as a cautionary example of the difference between an API client and a verified market-data archive.

## Source trail

[README](https://github.com/vcorp-dev/kalshi-price-data/blob/b77bd3b9e07d844fb993063f5532f86a596e17d0/README.md#L1); [kalshi_price_data/client.py](https://github.com/vcorp-dev/kalshi-price-data/blob/b77bd3b9e07d844fb993063f5532f86a596e17d0/kalshi_price_data/client.py#L90); [Root license](https://github.com/vcorp-dev/kalshi-price-data/blob/b77bd3b9e07d844fb993063f5532f86a596e17d0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
