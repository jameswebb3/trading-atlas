# Microsoft MLOps Example - Can a reported test error survive parameter search on the same test set?

**Decision question:** Can a reported test error survive parameter search on the same test set?

| Field | Review |
| --- | --- |
| Upstream | [microsoft/MLOps](https://github.com/microsoft/MLOps) |
| Primary area | Research & Reproducibility |
| Source commit | [c29628b917b42a910d2ae232556b706b8f1bc0c5](https://github.com/microsoft/MLOps/commit/c29628b917b42a910d2ae232556b706b8f1bc0c5) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Transferable |
| Executive assessment | The example logs metrics for candidate alpha values after one random train/test split. Repeatedly selecting by the same test error consumes that test set; a random split is also unsuitable for dependent trading observations. |

## What this project does

An Azure ML training example using Ridge regression.

## Mechanism inspected

The example logs metrics for candidate alpha values after one random train/test split.

## Limitation that matters

Repeatedly selecting by the same test error consumes that test set; a random split is also unsuitable for dependent trading observations.

## Practical check for a trading system

Keep a reserved holdout and time-aware split separate from tuning.

## Why this score

1/5. A useful negative example of experiment bookkeeping without valid evaluation design.

## Source trail

[README](https://github.com/microsoft/MLOps/blob/c29628b917b42a910d2ae232556b706b8f1bc0c5/README.md#L1); [model-training/train-sklearn.py](https://github.com/microsoft/MLOps/blob/c29628b917b42a910d2ae232556b706b8f1bc0c5/model-training/train-sklearn.py#L7); [Root license](https://github.com/microsoft/MLOps/blob/c29628b917b42a910d2ae232556b706b8f1bc0c5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
