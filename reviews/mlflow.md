# MLflow: Attach a dataset identity to each reported metric

**Decision question:** Which dataset produced the metric shown in a run?

| Field | Review |
| --- | --- |
| Upstream | [mlflow/mlflow](https://github.com/mlflow/mlflow) |
| Primary area | Research & Reproducibility |
| Source commit | [f1ec2021589730642dffb2c5e481078428b419b9](https://github.com/mlflow/mlflow/commit/f1ec2021589730642dffb2c5e481078428b419b9) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/mlflow/mlflow/blob/f1ec2021589730642dffb2c5e481078428b419b9/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Stores dataset name and digest alongside a metric and associates the dataset with the run. A digest field is only useful when its construction and the referenced bytes are trustworthy and retained. |

## Project overview

Experiment tracking platform for recording parameters, metrics, datasets, and model artifacts. Organizes runs and their supporting evidence so research results can be compared and investigated.

[Project documentation](https://github.com/mlflow/mlflow/blob/f1ec2021589730642dffb2c5e481078428b419b9/README.md#L144-L154).

## Mechanism worth inspecting

MLflow’s tracking API accepts a dataset for metric logging. The inspected path records dataset name and digest in the metric and logs the corresponding run input when needed. This prevents a metric row from floating free of the sample it summarizes.

**Source trail:** [project overview](https://github.com/mlflow/mlflow/blob/f1ec2021589730642dffb2c5e481078428b419b9/README.md) · [documentation](https://github.com/mlflow/mlflow/blob/f1ec2021589730642dffb2c5e481078428b419b9/README.md#L5-L19) · [implementation](https://github.com/mlflow/mlflow/blob/f1ec2021589730642dffb2c5e481078428b419b9/mlflow/tracking/fluent.py#L1200-L1217).

## Important limit

The API accepts the dataset identity supplied by the caller; this branch does not independently freeze or verify raw bytes. Async logging is also supported, so a completed call and durable result are separate questions.

## Questions to take into your own design

- Can each metric be traced to a content-stable dataset snapshot?
- Does the run receipt distinguish queued logging from durable logging?

## Why this score for a trading system

Metric-to-dataset digests are useful for strategy research receipts, but the inspected path trusts the supplied dataset identity.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
