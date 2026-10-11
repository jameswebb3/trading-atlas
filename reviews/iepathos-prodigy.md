# Prodigy - A workflow checkpoint is not side-effect reconciliation

**Decision question:** What does an agent resume skip after an interrupted step?

| Field | Review |
| --- | --- |
| Upstream | [iepathos/prodigy](https://github.com/iepathos/prodigy) |
| Primary area | Research & Reproducibility |
| Source commit | [4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba](https://github.com/iepathos/prodigy/commit/4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Uses checkpoint status and a stored step index to decide whether an agent workflow can resume or force restart. The reviewed skip calculation does not establish what external side effects occurred inside the interrupted step. |

## What this project does

An automated development workflow tool with checkpoint and resume commands. The inspected module contains pure decision helpers for the resume path and inline source tests.

## Mechanism inspected

should_resume blocks completed and running workflows unless forced. calculate_skip_count returns the stored current_step_index for ordinary resume and zero for force restart. Inline tests cover path selection and status decisions.

## Limitation that matters

The inspected helper uses the checkpoint index as the skip count without checking whether the current step produced an external side effect before interruption. The module does not reconcile orders, files or other external state; the broader tool may have separate checks outside this reviewed path. This is a source review, not a runtime or security test.

## Practical check for a trading system

A trading execution restart must query exchange orders and fills before skipping or repeating a step. Persist a durable action ID and make uncertain actions recoverable rather than relying on a workflow index alone.

## Why this score

2/5 because the source provides a clear transferable resume decision boundary and tests, while its indexed checkpoint lacks exchange-state reconciliation.

## Source trail

[README](https://github.com/iepathos/prodigy/blob/4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba/README.md#L712); [Resume helper](https://github.com/iepathos/prodigy/blob/4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba/src/resume_logic.rs#L74); [Inline tests](https://github.com/iepathos/prodigy/blob/4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba/src/resume_logic.rs#L109); [License](https://github.com/iepathos/prodigy/blob/4dc1789bc5a67a9d2b7323ac0f17f9ca046c65ba/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
