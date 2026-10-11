# Janus - Follow a feature back to its label

**Decision question:** Can a model feature contain its own target through a derived column?

| Field | Review |
| --- | --- |
| Upstream | [Ahmedxsaad/Janus](https://github.com/Ahmedxsaad/Janus) |
| Primary area | Data Quality & Lineage |
| Source commit | [5d428a29b79ceba9161d683ab3838237a65b50f2](https://github.com/Ahmedxsaad/Janus/commit/5d428a29b79ceba9161d683ab3838237a65b50f2) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The leakage detector follows each model feature's source column upstream to declared label columns; a separate detector diffs current input schema against a training-run snapshot Missing feature-source lineage or absent training snapshot makes a case untested, not clean; catalog coverage and time-of-availability still need separate proof |

## What this project does

A DataHub-based deterministic ML supply-chain detector [README](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/README.md).

## Mechanism inspected

The leakage detector follows each model feature's source column upstream to declared label columns; a separate detector diffs current input schema against a training-run snapshot [Implementation](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/janus/detect/leakage.py#L128-L170). [Related path](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/janus/detect/schema_drift.py#L127-L169).

## Limitation that matters

Missing feature-source lineage or absent training snapshot makes a case untested, not clean; catalog coverage and time-of-availability still need separate proof This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

For each trading target and feature, preserve column provenance and training-time schema. Report unknown when any link or baseline is missing

## Why this score

Directly relevant to false-positive research conclusions; the code keeps missing links out of the clean verdict

## Source trail

[README](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/README.md) - [Implementation](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/janus/detect/leakage.py#L128-L170) - [Related path](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/janus/detect/schema_drift.py#L127-L169) - [License](https://github.com/Ahmedxsaad/Janus/blob/5d428a29b79ceba9161d683ab3838237a65b50f2/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
