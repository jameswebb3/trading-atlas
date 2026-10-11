# daffy — A generic datetime type can lose resolution

**Decision question:** Is datetime precision part of the schema?

| Field | Review |
| --- | --- |
| Upstream | [daffy](https://github.com/vertti/daffy) |
| Primary area | Data Quality & Lineage |
| Source commit | [971af351754259987ce35ffe330b804cfaa97843](https://github.com/vertti/daffy/commit/971af351754259987ce35ffe330b804cfaa97843) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its dtype matcher strips parameters when the expected type is unparameterized, while explicit parameters constrain precision; it also counts nulls and unexpected columns. An expectation of merely datetime can accept different time units, which is dangerous when event and receipt clocks are compared. |

## What this project does

A decorator-based validator for pandas and Polars frames. [README](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/README.md).

## Mechanism inspected

Its dtype matcher strips parameters when the expected type is unparameterized, while explicit parameters constrain precision; it also counts nulls and unexpected columns. [Implementation](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/daffy/validators/columns.py#L34-L111).

## Limitation that matters

An expectation of merely datetime can accept different time units, which is dangerous when event and receipt clocks are compared. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Specify timestamp units and nullability explicitly for ingestion and feature boundaries.

## Why this score

Transferable engineering pattern: Its dtype matcher strips parameters when the expected type is unparameterized, while explicit parameters constrain precision; it also counts nulls and unexpected columns. An expectation of merely datetime can accept different time units, which is dangerous when event and receipt clocks are compared.

## Source trail

[README](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/README.md) · [Documentation](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/docs/usage.md) · [Implementation](https://github.com/vertti/daffy/blob/971af351754259987ce35ffe330b804cfaa97843/daffy/validators/columns.py#L34-L111).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
