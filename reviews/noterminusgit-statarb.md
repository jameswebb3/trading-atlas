# statarb - Do factor pipelines reject missing and infinite values before simulation?

**Decision question:** Do factor pipelines reject missing and infinite values before simulation?

| Field | Review |
| --- | --- |
| Upstream | [noterminusgit/statarb](https://github.com/noterminusgit/statarb) |
| Primary area | Data Quality & Lineage |
| Source commit | [b5a981ab2658b5eb5cd0a3f610bc9f4db7142655](https://github.com/noterminusgit/statarb/commit/b5a981ab2658b5eb5cd0a3f610bc9f4db7142655) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The validator reports missing columns, NaNs and infinities with counts, and rejects empty input. These schema checks do not prove point-in-time publication, survivorship freedom or venue execution realism. |

## What this project does

A statistical-arbitrage research repository with data-quality helper tests.

## Mechanism inspected

The validator reports missing columns, NaNs and infinities with counts, and rejects empty input.

## Limitation that matters

These schema checks do not prove point-in-time publication, survivorship freedom or venue execution realism.

## Practical check for a trading system

Combine value checks with temporal availability and universe membership checks at every dataset boundary.

## Why this score

3/5. Concrete checks are reusable as a pattern, but not a full causal data contract.

## Source trail

[README](https://github.com/noterminusgit/statarb/blob/b5a981ab2658b5eb5cd0a3f610bc9f4db7142655/README.md#L1); [docs/PHASE4_DATA_REQUIREMENTS.md](https://github.com/noterminusgit/statarb/blob/b5a981ab2658b5eb5cd0a3f610bc9f4db7142655/docs/PHASE4_DATA_REQUIREMENTS.md#L1); [tests/test_data_quality.py](https://github.com/noterminusgit/statarb/blob/b5a981ab2658b5eb5cd0a3f610bc9f4db7142655/tests/test_data_quality.py#L42); [Root license](https://github.com/noterminusgit/statarb/blob/b5a981ab2658b5eb5cd0a3f610bc9f4db7142655/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
