# HeurekaBench — A completed evaluation batch can still omit answers

**Decision question:** Is an agent benchmark score divided by all questions submitted?

| Field | Review |
| --- | --- |
| Upstream | [mlbio-epfl/HeurekaBench](https://github.com/mlbio-epfl/HeurekaBench) |
| Primary area | Agents & Decision Systems |
| Source commit | [c2a2b2fcdc5244220ff60f65483bc084c72a8cf1](https://github.com/mlbio-epfl/HeurekaBench/commit/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its evaluator waits for batch completion, maps returned custom IDs to questions and averages scores from returned lines. The shown path does not assert that every submitted custom ID returned exactly once; a partial output can change the score denominator. |

## What this project does

Benchmark framework for open-ended AI co-scientist questions grounded in studies. [README](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/README.md).

## Mechanism inspected

Its evaluator waits for batch completion, maps returned custom IDs to questions and averages scores from returned lines. [Implementation](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/scheurekabench/evaluate_agent_answer.py#L239-L272).

## Limitation that matters

The shown path does not assert that every submitted custom ID returned exactly once; a partial output can change the score denominator. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Reconcile submitted, returned, failed and duplicate IDs before accepting an agent-evaluation mean.

## Why this score

Its evaluator waits for batch completion, maps returned custom IDs to questions and averages scores from returned lines. The shown path does not assert that every submitted custom ID returned exactly once; a partial output can change the score denominator.

## Source trail

[README](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/README.md) · [Implementation](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/scheurekabench/evaluate_agent_answer.py#L239-L272) · [License](https://github.com/mlbio-epfl/HeurekaBench/blob/c2a2b2fcdc5244220ff60f65483bc084c72a8cf1/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
