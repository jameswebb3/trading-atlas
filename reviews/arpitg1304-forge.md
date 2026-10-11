# Forge Robotics Data Toolkit - What happens when invalid numeric samples enter quality metrics?

**Decision question:** What happens when invalid numeric samples enter quality metrics?

| Field | Review |
| --- | --- |
| Upstream | [arpitg1304/forge](https://github.com/arpitg1304/forge) |
| Primary area | Data Quality & Lineage |
| Source commit | [29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be](https://github.com/arpitg1304/forge/commit/29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The analyzer flags non-finite action values and then replaces NaN and infinity with zero before computing action metrics. The flag survives, but the reported metrics are based on repaired samples; a downstream consumer must not silently accept them as raw-data quality. |

## What this project does

A robotics dataset toolkit with episode-level quality analysis.

## Mechanism inspected

The analyzer flags non-finite action values and then replaces NaN and infinity with zero before computing action metrics.

## Limitation that matters

The flag survives, but the reported metrics are based on repaired samples; a downstream consumer must not silently accept them as raw-data quality.

## Practical check for a trading system

Carry invalid counts and the imputation policy beside every derived metric.

## Why this score

2/5. A concrete data-quality pattern transfers to market feeds, with a significant imputation caveat.

## Source trail

[README](https://github.com/arpitg1304/forge/blob/29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be/README.md#L1); [forge/quality/analyzer.py](https://github.com/arpitg1304/forge/blob/29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be/forge/quality/analyzer.py#L98); [forge/quality/analyzer.py](https://github.com/arpitg1304/forge/blob/29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be/forge/quality/analyzer.py#L101); [forge/quality/analyzer.py](https://github.com/arpitg1304/forge/blob/29e1df0bf0ff4dbd21f39cf7b59d6cd97620f2be/forge/quality/analyzer.py#L103).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
