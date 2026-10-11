# Micrometer — Detect metric-tag cardinality before monitoring collapses

**Decision question:** Can per-order labels overwhelm an observability system?

| Field | Review |
| --- | --- |
| Upstream | [micrometer-metrics/micrometer](https://github.com/micrometer-metrics/micrometer) |
| Primary area | Operations & Observability |
| Source commit | [b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea](https://github.com/micrometer-metrics/micrometer/commit/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The detector periodically searches for the first meter exceeding a configured tag threshold and invokes a warning consumer. The detector warns rather than constrains tags; its threshold is generic and may miss a burst between scans. |

## What this project does

A metrics library with scheduled detection of high-cardinality tag sets. [Project README](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/README.md#L1).

## Mechanism inspected

The detector periodically searches for the first meter exceeding a configured tag threshold and invokes a warning consumer. [Implementation](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/micrometer-core/src/main/java/io/micrometer/core/instrument/HighCardinalityTagsDetector.java#L121).

## Limitation that matters

The detector warns rather than constrains tags; its threshold is generic and may miss a burst between scans. This is a source review, not a runtime or security test.

## Practical check for a trading system

Avoid order IDs and timestamps as metric labels; keep high-cardinality details in logs or traces.

## Why this score

A practical monitoring-cost caution, not a trading-specific telemetry system.

## Source trail

[README](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/README.md#L1); [Implementation](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/micrometer-core/src/main/java/io/micrometer/core/instrument/HighCardinalityTagsDetector.java#L121) - [License](https://github.com/micrometer-metrics/micrometer/blob/b1b0dbffb54e83ba613c8df1ad4d7cc7cf666eea/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
