# Cube Studio - Is a dataset name and version enough to replay a run?

**Decision question:** Is a dataset name and version enough to replay a run?

| Field | Review |
| --- | --- |
| Upstream | [data-infra/cube-studio](https://github.com/data-infra/cube-studio) |
| Primary area | Research & Reproducibility |
| Source commit | [6774b3e29f272f73025b3d788272558a60c73696](https://github.com/data-infra/cube-studio/commit/6774b3e29f272f73025b3d788272558a60c73696) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The dataset launcher accepts name and version and downloads a selected source. The route does not record a payload hash; some source branches build shell commands from supplied names. |

## What this project does

A platform for datasets and ML workflows.

## Mechanism inspected

The dataset launcher accepts name and version and downloads a selected source.

## Limitation that matters

The route does not record a payload hash; some source branches build shell commands from supplied names.

## Practical check for a trading system

Persist content digests and resolved revision, not just a mutable version label.

## Why this score

2/5. The launcher exposes the gap between version selection and immutable evidence.

## Source trail

[README](https://github.com/data-infra/cube-studio/blob/6774b3e29f272f73025b3d788272558a60c73696/README.md#L1); [job-template/job/dataset/launcher.py](https://github.com/data-infra/cube-studio/blob/6774b3e29f272f73025b3d788272558a60c73696/job-template/job/dataset/launcher.py#L123); [Root license](https://github.com/data-infra/cube-studio/blob/6774b3e29f272f73025b3d788272558a60c73696/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
