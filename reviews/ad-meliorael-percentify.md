# Percentify — Profile targets separately from features

**Decision question:** Does a dataset profiler treat the label as an ordinary input column?

| Field | Review |
| --- | --- |
| Upstream | [Ad-meliorael/percentify](https://github.com/Ad-meliorael/percentify) |
| Primary area | Data Quality & Lineage |
| Source commit | [811876ccbf56432f8e2f1a9e5179627966bdba3c](https://github.com/Ad-meliorael/percentify/commit/811876ccbf56432f8e2f1a9e5179627966bdba3c) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The profiler accepts an explicit target and runs target-specific leakage and imbalance checks apart from feature diagnostics. A profiler can flag obvious relationships but cannot prove publication time or eliminate leakage caused by the experiment design. |

## What this project does

A dataframe profiler that ranks quality issues and suggested fixes. [Project README](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/README.md#L1).

## Mechanism inspected

The profiler accepts an explicit target and runs target-specific leakage and imbalance checks apart from feature diagnostics. [Implementation](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/percentify/profiling.py#L684).

## Limitation that matters

A profiler can flag obvious relationships but cannot prove publication time or eliminate leakage caused by the experiment design. This is a source review, not a runtime or security test.

## Practical check for a trading system

Declare target columns before profiling and inspect feature availability at decision time separately.

## Why this score

A useful boundary between label and feature diagnostics, with no claim of causal certification.

## Source trail

[README](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/README.md#L1); [Implementation](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/percentify/profiling.py#L684) - [License](https://github.com/Ad-meliorael/percentify/blob/811876ccbf56432f8e2f1a9e5179627966bdba3c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
