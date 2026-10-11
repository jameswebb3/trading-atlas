# loongcollector - Keep the last working collector when a new config is invalid

**Decision question:** Should a failed config replacement stop the currently running pipeline?

| Field | Review |
| --- | --- |
| Upstream | [alibaba/loongcollector](https://github.com/alibaba/loongcollector) |
| Primary area | Market Data & Ingestion |
| Source commit | [d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b](https://github.com/alibaba/loongcollector/commit/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | For a modified pipeline, it builds the candidate first. If construction fails, it keeps the existing task running, emits an alarm and marks the new config failed. Only after a successful build does it stop the old task and start the replacement. Keeping a process alive does not certify that its feed is complete or its schema still matches the source. The replacement path shown is not an atomic handover of market-event positions. |

## What this project does

LoongCollector builds task pipelines from collector configuration and reports application status. [README](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/README.md).

## Mechanism inspected

For a modified pipeline, it builds the candidate first. If construction fails, it keeps the existing task running, emits an alarm and marks the new config failed. Only after a successful build does it stop the old task and start the replacement. [Implementation](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/core/task_pipeline/TaskPipelineManager.cpp#L27-L92). [Related path](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/core/task_pipeline/TaskPipeline.cpp#L26-L64).

## Limitation that matters

Keeping a process alive does not certify that its feed is complete or its schema still matches the source. The replacement path shown is not an atomic handover of market-event positions. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Test a malformed collector config update and verify the old version remains active with an explicit failed-update status; reconcile event continuity across a successful handover.

## Why this score

It is a precise deployment safeguard for data collection, with separate semantic-health checks still required.

## Source trail

[README](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/README.md) - [Implementation](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/core/task_pipeline/TaskPipelineManager.cpp#L27-L92) - [Related path](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/core/task_pipeline/TaskPipeline.cpp#L26-L64) - [License](https://github.com/alibaba/loongcollector/blob/d9e8f4df6cf58d4c4be59a6ba3efc67bb37dc46b/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
