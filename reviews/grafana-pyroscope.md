# pyroscope - Count rejected inputs by reason

**Decision question:** Can ingestion report exactly why incoming observations were discarded?

| Field | Review |
| --- | --- |
| Upstream | [grafana/pyroscope](https://github.com/grafana/pyroscope) |
| Primary area | Operations & Observability |
| Source commit | [cbbf2a6053734ae00c640e16cf254808f1e5ef84](https://github.com/grafana/pyroscope/commit/cbbf2a6053734ae00c640e16cf254808f1e5ef84) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0-only ([source](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/LICENSING.md)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Validation assigns typed discard reasons such as invalid labels, out-of-window timestamp and rate limit; the distributor increments discarded-profile and byte counters with reason and tenant labels. Profile ingestion is not market-data ingestion. These counters explain rejected requests inside this service, not missing source events that never arrived. |

## What this project does

Pyroscope collects and queries continuous application profiles with per-tenant ingestion limits. [README](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/README.md).

## Mechanism inspected

Validation assigns typed discard reasons such as invalid labels, out-of-window timestamp and rate limit; the distributor increments discarded-profile and byte counters with reason and tenant labels. [Implementation](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/pkg/validation/validate.go#L26-L70). [Related path](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/pkg/distributor/distributor.go#L713-L717).

## Limitation that matters

Profile ingestion is not market-data ingestion. These counters explain rejected requests inside this service, not missing source events that never arrived. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

At a market-data ingest boundary, count accepted and rejected events by explicit reason, symbol, source and time bucket, and keep never-arrived gaps as a separate measure.

## Why this score

Validation assigns typed discard reasons such as invalid labels, out-of-window timestamp and rate limit; the distributor increments discarded-profile and byte counters with reason and tenant labels. Profile ingestion is not market-data ingestion. These counters explain rejected requests inside this service, not missing source events that never arrived.

## Source trail

[README](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/README.md) - [Implementation](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/pkg/validation/validate.go#L26-L70) - [Related path](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/pkg/distributor/distributor.go#L713-L717) - [License](https://github.com/grafana/pyroscope/blob/cbbf2a6053734ae00c640e16cf254808f1e5ef84/LICENSING.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
