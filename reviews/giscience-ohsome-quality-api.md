# ohsome Quality API - Is freshness measured against source coverage or wall-clock time?

**Decision question:** Is freshness measured against source coverage or wall-clock time?

| Field | Review |
| --- | --- |
| Upstream | [GIScience/ohsome-quality-api](https://github.com/GIScience/ohsome-quality-api) |
| Primary area | Data Quality & Lineage |
| Source commit | [c5e34d53b45e6da41786b1c83c2a34e3108c95fe](https://github.com/GIScience/ohsome-quality-api/commit/c5e34d53b45e6da41786b1c83c2a34e3108c95fe) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The currentness indicator anchors monthly bins to the source metadata temporalExtent.end and queries the latest contributions. Deleted features are excluded by the inspected path, and a source-relative freshness score can look good while the source itself is late. |

## What this project does

An OpenStreetMap quality service that estimates currentness for a region.

## Mechanism inspected

The currentness indicator anchors monthly bins to the source metadata temporalExtent.end and queries the latest contributions.

## Limitation that matters

Deleted features are excluded by the inspected path, and a source-relative freshness score can look good while the source itself is late.

## Practical check for a trading system

Record both source coverage end and the decision-time freshness lag.

## Why this score

2/5. The two-clock distinction transfers to trading data freshness checks.

## Source trail

[README](https://github.com/GIScience/ohsome-quality-api/blob/c5e34d53b45e6da41786b1c83c2a34e3108c95fe/README.md#L1); [ohsome_quality_api/indicators/currentness/indicator.py](https://github.com/GIScience/ohsome-quality-api/blob/c5e34d53b45e6da41786b1c83c2a34e3108c95fe/ohsome_quality_api/indicators/currentness/indicator.py#L73); [ohsome_quality_api/indicators/currentness/indicator.py](https://github.com/GIScience/ohsome-quality-api/blob/c5e34d53b45e6da41786b1c83c2a34e3108c95fe/ohsome_quality_api/indicators/currentness/indicator.py#L80); [ohsome_quality_api/indicators/currentness/indicator.py](https://github.com/GIScience/ohsome-quality-api/blob/c5e34d53b45e6da41786b1c83c2a34e3108c95fe/ohsome_quality_api/indicators/currentness/indicator.py#L83).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
