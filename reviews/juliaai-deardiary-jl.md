# DearDiary.jl — Experiment iterations close with an explicit terminal state

**Decision question:** Will a failed research run remain visibly failed after an exception?

| Field | Review |
| --- | --- |
| Upstream | [JuliaAI/DearDiary.jl](https://github.com/JuliaAI/DearDiary.jl) |
| Primary area | Research & Reproducibility |
| Source commit | [3fd20fc5893c9274c4428763ca20bf33fd78981d](https://github.com/JuliaAI/DearDiary.jl/commit/3fd20fc5893c9274c4428763ca20bf33fd78981d) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | with_iteration snapshots the environment, marks normal completion SUCCEEDED, records exception text on FAILED and rethrows the original error. A failure while recording the terminal state is swallowed to preserve the original exception; the ledger can still miss the final status. |

## What this project does

Julia experiment tracker for projects, iterations, parameters, metrics and environment snapshots. [README](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/README.md).

## Mechanism inspected

with_iteration snapshots the environment, marks normal completion SUCCEEDED, records exception text on FAILED and rethrows the original error. [Implementation](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/src/services/iteration.jl#L286-L319). [Test source](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/test/services/iteration.jl#L208-L245).

## Limitation that matters

A failure while recording the terminal state is swallowed to preserve the original exception; the ledger can still miss the final status. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Reconcile started versus terminal trial IDs and alert on stranded runs, while preserving the original research error.

## Why this score

with_iteration snapshots the environment, marks normal completion SUCCEEDED, records exception text on FAILED and rethrows the original error. A failure while recording the terminal state is swallowed to preserve the original exception; the ledger can still miss the final status.

## Source trail

[README](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/README.md) · [Implementation](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/src/services/iteration.jl#L286-L319) · [Test source](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/test/services/iteration.jl#L208-L245) · [License](https://github.com/JuliaAI/DearDiary.jl/blob/3fd20fc5893c9274c4428763ca20bf33fd78981d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
