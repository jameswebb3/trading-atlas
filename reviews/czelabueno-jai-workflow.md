# Jai Workflow - Does a valid workflow graph guarantee a resumable experiment?

**Decision question:** Does a valid workflow graph guarantee a resumable experiment?

| Field | Review |
| --- | --- |
| Upstream | [czelabueno/jai-workflow](https://github.com/czelabueno/jai-workflow) |
| Primary area | Research & Reproducibility |
| Source commit | [864bef04bf92990295c169feebb908e791a39fe2](https://github.com/czelabueno/jai-workflow/commit/864bef04bf92990295c169feebb908e791a39fe2) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The builder validates graph structure and start/end transitions before constructing a workflow. Graph validity says nothing about durable task receipts, retry idempotence or data snapshot identity. |

## What this project does

A Java state-workflow builder.

## Mechanism inspected

The builder validates graph structure and start/end transitions before constructing a workflow.

## Limitation that matters

Graph validity says nothing about durable task receipts, retry idempotence or data snapshot identity.

## Practical check for a trading system

Validate the DAG and separately persist step inputs, outputs and retries.

## Why this score

2/5. A transferable structural check with a missing execution-evidence layer.

## Source trail

[README](https://github.com/czelabueno/jai-workflow/blob/864bef04bf92990295c169feebb908e791a39fe2/README.md#L1); [jai-workflow-core/src/main/java/io/github/czelabueno/jai/workflow/DefaultStateWorkflow.java](https://github.com/czelabueno/jai-workflow/blob/864bef04bf92990295c169feebb908e791a39fe2/jai-workflow-core/src/main/java/io/github/czelabueno/jai/workflow/DefaultStateWorkflow.java#L231); [Root license](https://github.com/czelabueno/jai-workflow/blob/864bef04bf92990295c169feebb908e791a39fe2/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
