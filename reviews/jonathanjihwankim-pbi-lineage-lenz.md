# pbi-lineage-lenz - Distinguish a reused dependency from a lineage cycle

**Decision question:** Can a lineage graph traverse a shared upstream metric without calling it circular?

| Field | Review |
| --- | --- |
| Upstream | [JonathanJihwanKim/pbi-lineage-lenz](https://github.com/JonathanJihwanKim/pbi-lineage-lenz) |
| Primary area | Data Quality & Lineage |
| Source commit | [b8d6e0fde7c0c23f8edd6dae5372701861089674](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/commit/b8d6e0fde7c0c23f8edd6dae5372701861089674) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The measure tracer carries an ancestors set on the current path to flag real cycles, and a memo of completed subtrees to reuse a measure reached from more than one parent. Source-column rows are deduplicated while retaining every referring measure. This is static analysis of a Power BI model. It does not verify query execution, delayed publication, or the values stored in a source column; parser omissions remain outside this path. |

## What this project does

PBI Lineage Lenz traces Power BI visuals and DAX measures back to their source tables and columns. [README](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/README.md).

## Mechanism inspected

The measure tracer carries an ancestors set on the current path to flag real cycles, and a memo of completed subtrees to reuse a measure reached from more than one parent. Source-column rows are deduplicated while retaining every referring measure. [Implementation](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/packages/core/src/graph/lineageTracer.js#L261-L309). [Related path](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/packages/core/src/graph/lineageTracer.js#L357-L389).

## Limitation that matters

This is static analysis of a Power BI model. It does not verify query execution, delayed publication, or the values stored in a source column; parser omissions remain outside this path. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For a feature or report dependency graph, test a diamond-shaped DAG and a genuine cycle separately. Keep every consumer of a shared source in the impact view.

## Why this score

The cycle-versus-reuse distinction is a common graph correctness trap; the implementation is precise but its domain is BI lineage.

## Source trail

[README](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/README.md) - [Implementation](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/packages/core/src/graph/lineageTracer.js#L261-L309) - [Related path](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/packages/core/src/graph/lineageTracer.js#L357-L389) - [License](https://github.com/JonathanJihwanKim/pbi-lineage-lenz/blob/b8d6e0fde7c0c23f8edd6dae5372701861089674/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
