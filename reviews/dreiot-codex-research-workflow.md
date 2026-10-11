# Codex Research Workflow - What should an experiment record say about a dirty working tree?

**Decision question:** What should an experiment record say about a dirty working tree?

| Field | Review |
| --- | --- |
| Upstream | [Dreiot/codex-research-workflow](https://github.com/Dreiot/codex-research-workflow) |
| Primary area | Research & Reproducibility |
| Source commit | [687cab5d2466fbdaaa3e17099fa2ce572d613071](https://github.com/Dreiot/codex-research-workflow/commit/687cab5d2466fbdaaa3e17099fa2ce572d613071) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The workflow records current HEAD, a dirty-worktree flag and an optional source-snapshot path. The snapshot is optional and a dirty flag alone does not identify the changed bytes or data inputs. |

## What this project does

A research-workflow package with evidence metadata.

## Mechanism inspected

The workflow records current HEAD, a dirty-worktree flag and an optional source-snapshot path.

## Limitation that matters

The snapshot is optional and a dirty flag alone does not identify the changed bytes or data inputs.

## Practical check for a trading system

Require a source snapshot or diff digest when the research workspace is dirty.

## Why this score

2/5. The metadata fields help trace a run, but they are not a complete reproducibility receipt.

## Source trail

[README](https://github.com/Dreiot/codex-research-workflow/blob/687cab5d2466fbdaaa3e17099fa2ce572d613071/README.md#L1); [skills/codex-research-workflow/scripts/workflow.py](https://github.com/Dreiot/codex-research-workflow/blob/687cab5d2466fbdaaa3e17099fa2ce572d613071/skills/codex-research-workflow/scripts/workflow.py#L1040); [skills/codex-research-workflow/scripts/workflow.py](https://github.com/Dreiot/codex-research-workflow/blob/687cab5d2466fbdaaa3e17099fa2ce572d613071/skills/codex-research-workflow/scripts/workflow.py#L1062); [Root license](https://github.com/Dreiot/codex-research-workflow/blob/687cab5d2466fbdaaa3e17099fa2ce572d613071/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
