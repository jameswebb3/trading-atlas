# Crypto Data Pipeline - Can retrying a crypto price collector still leave data gaps?

**Decision question:** Can retrying a crypto price collector still leave data gaps?

| Field | Review |
| --- | --- |
| Upstream | [godstime-dev/crypto-data-pipeline](https://github.com/godstime-dev/crypto-data-pipeline) |
| Primary area | Market Data & Ingestion |
| Source commit | [51e73cc3ecdf60832b370e171d41a54a907db8f9](https://github.com/godstime-dev/crypto-data-pipeline/commit/51e73cc3ecdf60832b370e171d41a54a907db8f9) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The collector enforces a minimum interval and backs off on HTTP 429; a validator checks coin and USD price before insert. Other fields are warnings, and a unique coin/timestamp conflict is ignored, so missing fields and timestamp collisions can pass quietly. |

## What this project does

A small cryptocurrency market-data collector backed by DuckDB.

## Mechanism inspected

The collector enforces a minimum interval and backs off on HTTP 429; a validator checks coin and USD price before insert.

## Limitation that matters

Other fields are warnings, and a unique coin/timestamp conflict is ignored, so missing fields and timestamp collisions can pass quietly.

## Practical check for a trading system

Make field coverage and duplicate timestamp conflicts explicit in collector receipts.

## Why this score

2/5. The rate-limit loop is practical, while accepted partial rows limit data trust.

## Source trail

[README](https://github.com/godstime-dev/crypto-data-pipeline/blob/51e73cc3ecdf60832b370e171d41a54a907db8f9/README.md#L1); [app/collector.py](https://github.com/godstime-dev/crypto-data-pipeline/blob/51e73cc3ecdf60832b370e171d41a54a907db8f9/app/collector.py#L29); [app/collector.py](https://github.com/godstime-dev/crypto-data-pipeline/blob/51e73cc3ecdf60832b370e171d41a54a907db8f9/app/collector.py#L54); [app/validator.py](https://github.com/godstime-dev/crypto-data-pipeline/blob/51e73cc3ecdf60832b370e171d41a54a907db8f9/app/validator.py#L6); [app/database.py](https://github.com/godstime-dev/crypto-data-pipeline/blob/51e73cc3ecdf60832b370e171d41a54a907db8f9/app/database.py#L30).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
