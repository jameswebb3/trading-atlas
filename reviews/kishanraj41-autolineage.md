# autolineage — Locate the first pipeline step that changed a dataset

**Decision question:** Where did a missing or newly retained feature first appear?

| Field | Review |
| --- | --- |
| Upstream | [kishanraj41/autolineage](https://github.com/kishanraj41/autolineage) |
| Primary area | Data Quality & Lineage |
| Source commit | [3b0e303b217f2e3ff7ca821dae06501dc155bb90](https://github.com/kishanraj41/autolineage/commit/3b0e303b217f2e3ff7ca821dae06501dc155bb90) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A fingerprint records row deltas, column sets, shapes, duration and metrics per operation occurrence; comparison attributes introduced, retained and missing columns to the first relevant step. Operation-name and occurrence matching is sensitive to pipeline refactors; its baseline comparison does not by itself prove causality or a safe historical cutoff. |

## What this project does

Automatic lineage tracker with run fingerprints and anomaly localization. [README](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/README.md).

## Mechanism inspected

A fingerprint records row deltas, column sets, shapes, duration and metrics per operation occurrence; comparison attributes introduced, retained and missing columns to the first relevant step. [Implementation](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/autolineage/core/analyzer.py#L145-L190). [Related implementation](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/autolineage/core/analyzer.py#L263-L289).

## Limitation that matters

Operation-name and occurrence matching is sensitive to pipeline refactors; its baseline comparison does not by itself prove causality or a safe historical cutoff. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Compare feature-build fingerprints between approved and candidate runs, tracing a changed target/availability column to its first transformation before any backtest.

## Why this score

A fingerprint records row deltas, column sets, shapes, duration and metrics per operation occurrence; comparison attributes introduced, retained and missing columns to the first relevant step. Operation-name and occurrence matching is sensitive to pipeline refactors; its baseline comparison does not by itself prove causality or a safe historical cutoff.

## Source trail

[README](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/README.md) · [Implementation](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/autolineage/core/analyzer.py#L145-L190) · [Related implementation](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/autolineage/core/analyzer.py#L263-L289) · [License](https://github.com/kishanraj41/autolineage/blob/3b0e303b217f2e3ff7ca821dae06501dc155bb90/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
