# Ralph Loop Optimizer - Can an agent write evidence outside its assigned run directory?

**Decision question:** Can an agent write evidence outside its assigned run directory?

| Field | Review |
| --- | --- |
| Upstream | [haoran-ni/ralph-loop-optimizer](https://github.com/haoran-ni/ralph-loop-optimizer) |
| Primary area | Research & Reproducibility |
| Source commit | [8c66117f824b3362c8b49e04bd34a9866b171c5c](https://github.com/haoran-ni/ralph-loop-optimizer/commit/8c66117f824b3362c8b49e04bd34a9866b171c5c) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Artifact paths validate a simple run identifier and resolve the destination inside the repository. The final write uses direct write_text; an interrupted write can leave a truncated artifact. |

## What this project does

An iterative optimization agent with managed run artifacts.

## Mechanism inspected

Artifact paths validate a simple run identifier and resolve the destination inside the repository.

## Limitation that matters

The final write uses direct write_text; an interrupted write can leave a truncated artifact.

## Practical check for a trading system

Constrain agent output paths and use atomic replacement for evidence files.

## Why this score

2/5. The path guard is practical, with crash-safe evidence writing still absent.

## Source trail

[README](https://github.com/haoran-ni/ralph-loop-optimizer/blob/8c66117f824b3362c8b49e04bd34a9866b171c5c/README.md#L1); [src/ralph_loop_optimizer/artifacts.py](https://github.com/haoran-ni/ralph-loop-optimizer/blob/8c66117f824b3362c8b49e04bd34a9866b171c5c/src/ralph_loop_optimizer/artifacts.py#L94); [src/ralph_loop_optimizer/artifacts.py](https://github.com/haoran-ni/ralph-loop-optimizer/blob/8c66117f824b3362c8b49e04bd34a9866b171c5c/src/ralph_loop_optimizer/artifacts.py#L138).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
