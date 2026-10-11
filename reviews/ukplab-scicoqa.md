# SciCoQA: Can paper-versus-code analysis inspect code written after the paper?

**Decision question:** Can paper-versus-code analysis inspect code written after the paper?

| Field | Review |
| --- | --- |
| Upstream | [UKPLab/scicoqa](https://github.com/UKPLab/scicoqa) |
| Primary area | Research & Reproducibility |
| Source commit | [463162906459be508ed4a2294fcaede9fa072036](https://github.com/UKPLab/scicoqa/commit/463162906459be508ed4a2294fcaede9fa072036) |
| Reviewed | 2026-10-11 |
| Declared license | [Apache-2.0](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The discrepancy iterator passes a paper-specific date to CodeLoader. CodeLoader finds the latest branch commit before that date and records its SHA permalink; if none exists, it selects the latest current commit. Time-based commit selection is not proof of the code actually used in a paper. The fallback is temporally invalid. The loader clones repositories when run; this Atlas review read source only and did not invoke it. |

## What this project does

Compares scientific claims with repository code at a target date. If no commit predates that date, its loader falls back to the latest commit, allowing future code into a historical comparison.

## Mechanism inspected

The discrepancy iterator passes a paper-specific date to CodeLoader. CodeLoader finds the latest branch commit before that date and records its SHA permalink; if none exists, it selects the latest current commit.

## Limitation that matters

Time-based commit selection is not proof of the code actually used in a paper. The fallback is temporally invalid. The loader clones repositories when run; this Atlas review read source only and did not invoke it.

## Practical check for a trading system

Record exact code SHA, release/paper date and selection rule. Treat absent earlier code as missing evidence.

## Why this score

2/5 transferable: paper-code alignment is useful, but the fallback creates a clear lookahead trap.

## Source trail

[README.md](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/README.md#L1); [data/README.md](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/data/README.md#L1); [scicoqa/inference/discrepancy_detection.py](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/scicoqa/inference/discrepancy_detection.py#L166); [scicoqa/core/code_loader.py](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/scicoqa/core/code_loader.py#L58); [scicoqa/core/code_loader.py](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/scicoqa/core/code_loader.py#L199); [scicoqa/core/code_loader.py](https://github.com/UKPLab/scicoqa/blob/463162906459be508ed4a2294fcaede9fa072036/scicoqa/core/code_loader.py#L227)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
