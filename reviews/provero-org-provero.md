# provero — No history is a separate quality state

**Decision question:** Does an anomaly check distinguish insufficient baseline from a clean pass?

| Field | Review |
| --- | --- |
| Upstream | [provero-org/provero](https://github.com/provero-org/provero) |
| Primary area | Data Quality & Lineage |
| Source commit | [fc261752af25fba0e77664bb43fc66794037a136](https://github.com/provero-org/provero/commit/fc261752af25fba0e77664bb43fc66794037a136) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The anomaly check returns SKIP if no historical metric exists, ERROR for non-finite current or historical values, then PASS/FAIL only after a detector runs. Its generic MAD-style detector does not encode trading regime or seasonality; the useful part is status semantics. |

## What this project does

Data observability engine with historical anomaly checks. [README](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/README.md).

## Mechanism inspected

The anomaly check returns SKIP if no historical metric exists, ERROR for non-finite current or historical values, then PASS/FAIL only after a detector runs. [Implementation](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/provero-core/src/provero/anomaly/checks.py#L156-L210).

## Limitation that matters

Its generic MAD-style detector does not encode trading regime or seasonality; the useful part is status semantics. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Make no-baseline, invalid-baseline and anomalous-data separate collector quality outcomes, and prevent SKIP from counting as PASS.

## Why this score

The anomaly check returns SKIP if no historical metric exists, ERROR for non-finite current or historical values, then PASS/FAIL only after a detector runs. Its generic MAD-style detector does not encode trading regime or seasonality; the useful part is status semantics.

## Source trail

[README](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/README.md) · [Implementation](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/provero-core/src/provero/anomaly/checks.py#L156-L210) · [License](https://github.com/provero-org/provero/blob/fc261752af25fba0e77664bb43fc66794037a136/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
