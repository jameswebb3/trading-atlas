# Medicare CCLF Connector - How should revised and cancelled records be selected?

**Decision question:** How should revised and cancelled records be selected?

| Field | Review |
| --- | --- |
| Upstream | [tuva-health/medicare_cclf_connector](https://github.com/tuva-health/medicare_cclf_connector) |
| Primary area | Data Quality & Lineage |
| Source commit | [4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf](https://github.com/tuva-health/medicare_cclf_connector/commit/4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The intermediate model ranks claim versions and removes cancellation records before selecting the latest row. The ordering is healthcare-specific and does not prove that a revised record was known at the historical decision time. |

## What this project does

A dbt connector for versioned Medicare claims.

## Mechanism inspected

The intermediate model ranks claim versions and removes cancellation records before selecting the latest row.

## Limitation that matters

The ordering is healthcare-specific and does not prove that a revised record was known at the historical decision time.

## Practical check for a trading system

Keep revision time and effective time separate when deduplicating exchange or reference events.

## Why this score

2/5. The explicit revision selection is useful; point-in-time availability remains separate.

## Source trail

[README](https://github.com/tuva-health/medicare_cclf_connector/blob/4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf/README.md#L1); [models/intermediate/int_pharmacy_claim_deduped.sql](https://github.com/tuva-health/medicare_cclf_connector/blob/4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf/models/intermediate/int_pharmacy_claim_deduped.sql#L28); [models/intermediate/int_pharmacy_claim_deduped.sql](https://github.com/tuva-health/medicare_cclf_connector/blob/4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf/models/intermediate/int_pharmacy_claim_deduped.sql#L90); [Root license](https://github.com/tuva-health/medicare_cclf_connector/blob/4728d7a65eed512e2c9d2c3ad2dd82f24e1f81cf/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
