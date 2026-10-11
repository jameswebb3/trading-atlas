# Point-in-Time Feature Store - Does a historical join require both event time and availability time?

**Decision question:** Does a historical join require both event time and availability time?

| Field | Review |
| --- | --- |
| Upstream | [datawizard1394/point-in-time-feature-store](https://github.com/datawizard1394/point-in-time-feature-store) |
| Primary area | Data Quality & Lineage |
| Source commit | [cedb6b1a0da70bc43cc9982be8b16701055ebf17](https://github.com/datawizard1394/point-in-time-feature-store/commit/cedb6b1a0da70bc43cc9982be8b16701055ebf17) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The eligibility filter includes a transaction only if its event_time and available_at are both no later than the as-of time. The fixture is synthetic and does not model corrected source revisions or uncertainty in the recorded availability clock. |

## What this project does

A synthetic reference implementation of historical feature generation and parity checks.

## Mechanism inspected

The eligibility filter includes a transaction only if its event_time and available_at are both no later than the as-of time.

## Limitation that matters

The fixture is synthetic and does not model corrected source revisions or uncertainty in the recorded availability clock.

## Practical check for a trading system

Require both clocks and versioned corrections in each source-to-feature lineage record.

## Why this score

4/5. The dual-clock gate directly addresses silent historical leakage.

## Source trail

[README](https://github.com/datawizard1394/point-in-time-feature-store/blob/cedb6b1a0da70bc43cc9982be8b16701055ebf17/README.md#L1); [docs/adr-001-bitemporal-pit-join.md](https://github.com/datawizard1394/point-in-time-feature-store/blob/cedb6b1a0da70bc43cc9982be8b16701055ebf17/docs/adr-001-bitemporal-pit-join.md#L1); [src/feature_store/engine.py](https://github.com/datawizard1394/point-in-time-feature-store/blob/cedb6b1a0da70bc43cc9982be8b16701055ebf17/src/feature_store/engine.py#L44); [Root license](https://github.com/datawizard1394/point-in-time-feature-store/blob/cedb6b1a0da70bc43cc9982be8b16701055ebf17/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
