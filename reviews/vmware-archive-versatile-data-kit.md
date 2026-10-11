# versatile-data-kit — A job result should name its failing step

**Decision question:** Can a pipeline finish with a specific reason rather than a generic red status?

| Field | Review |
| --- | --- |
| Upstream | [versatile-data-kit](https://github.com/vmware-archive/versatile-data-kit) |
| Primary area | Research & Reproducibility |
| Source commit | [a9a4c3d6ffff1064cf60f505ffc7d8c747d59201](https://github.com/vmware-archive/versatile-data-kit/commit/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/vmware-archive/versatile-data-kit/blob/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The job runner collects per-step results and emits an execution status when a step fails. The repository announces future archival; installing the framework would add a large dependency, and a successful job does not itself certify data completeness. |

## What this project does

A data job framework with ordered steps and structured execution results. [README](https://github.com/vmware-archive/versatile-data-kit/blob/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201/README.md).

## Mechanism inspected

The job runner collects per-step results and emits an execution status when a step fails. [Implementation](https://github.com/vmware-archive/versatile-data-kit/blob/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201/projects/vdk-core/src/vdk/internal/builtin_plugins/run/data_job.py#L109-L165).

## Limitation that matters

The repository announces future archival; installing the framework would add a large dependency, and a successful job does not itself certify data completeness. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep step-level failure reason in local trial receipts; avoid adopting the framework.

## Why this score

Transferable engineering pattern: The job runner collects per-step results and emits an execution status when a step fails. The repository announces future archival; installing the framework would add a large dependency, and a successful job does not itself certify data completeness.

## Source trail

[README](https://github.com/vmware-archive/versatile-data-kit/blob/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201/README.md) · [Implementation](https://github.com/vmware-archive/versatile-data-kit/blob/a9a4c3d6ffff1064cf60f505ffc7d8c747d59201/projects/vdk-core/src/vdk/internal/builtin_plugins/run/data_job.py#L109-L165).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
