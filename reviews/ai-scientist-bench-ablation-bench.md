# AblationBench - Does a timestamped evaluation directory reproduce the same benchmark?

**Decision question:** Does a timestamped evaluation directory reproduce the same benchmark?

| Field | Review |
| --- | --- |
| Upstream | [ai-scientist-bench/ablation-bench](https://github.com/ai-scientist-bench/ablation-bench) |
| Primary area | Agents & Decision Systems |
| Source commit | [be61e0403b2ef556704871f2b02d567c123da651](https://github.com/ai-scientist-bench/ablation-bench/commit/be61e0403b2ef556704871f2b02d567c123da651) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The harness configures a dataset split, judge and output directory, then creates a timestamped result path. A timestamp alone does not pin the dataset revision or judge implementation. |

## What this project does

A benchmark harness for automated ablation research.

## Mechanism inspected

The harness configures a dataset split, judge and output directory, then creates a timestamped result path.

## Limitation that matters

A timestamp alone does not pin the dataset revision or judge implementation.

## Practical check for a trading system

Record dataset and judge digests with each ablation run.

## Why this score

2/5. The output organization is useful; stronger input identity is required for repeatability.

## Source trail

[README](https://github.com/ai-scientist-bench/ablation-bench/blob/be61e0403b2ef556704871f2b02d567c123da651/README.md#L1); [ablation_bench/harness/evaluation.py](https://github.com/ai-scientist-bench/ablation-bench/blob/be61e0403b2ef556704871f2b02d567c123da651/ablation_bench/harness/evaluation.py#L21); [ablation_bench/harness/evaluation.py](https://github.com/ai-scientist-bench/ablation-bench/blob/be61e0403b2ef556704871f2b02d567c123da651/ablation_bench/harness/evaluation.py#L100).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
