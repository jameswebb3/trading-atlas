# LEILA - Could automatic type conversion hide a broken feed?

**Decision question:** Could automatic type conversion hide a broken feed?

| Field | Review |
| --- | --- |
| Upstream | [ucd-dnp/leila](https://github.com/ucd-dnp/leila) |
| Primary area | Data Quality & Lineage |
| Source commit | [79877fe8246ea52450d1b1cd219b59b471c7a19d](https://github.com/ucd-dnp/leila/commit/79877fe8246ea52450d1b1cd219b59b471c7a19d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The input class supports CSV, Excel and DataFrames with optional inferred type conversion and configurable error handling. Its documented defaults include castDatos true and errors ignore; silently coerced market fields would need explicit exceptions and counts. |

## What this project does

A Spanish-language data-quality library for structured datasets.

## Mechanism inspected

The input class supports CSV, Excel and DataFrames with optional inferred type conversion and configurable error handling.

## Limitation that matters

Its documented defaults include castDatos true and errors ignore; silently coerced market fields would need explicit exceptions and counts.

## Practical check for a trading system

Preserve raw values and fail or quarantine on type drift in price, size and timestamp fields.

## Why this score

2/5. The configurable coercion makes a practical caution for ingestion contracts.

## Source trail

[README](https://github.com/ucd-dnp/leila/blob/79877fe8246ea52450d1b1cd219b59b471c7a19d/README.md#L1); [leila/calidad_datos.py](https://github.com/ucd-dnp/leila/blob/79877fe8246ea52450d1b1cd219b59b471c7a19d/leila/calidad_datos.py#L36); [leila/calidad_datos.py](https://github.com/ucd-dnp/leila/blob/79877fe8246ea52450d1b1cd219b59b471c7a19d/leila/calidad_datos.py#L71).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
