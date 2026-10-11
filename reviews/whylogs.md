# whylogs: Missing metrics must not silently pass a constraint

**Decision question:** What does a data-quality rule do when its column is absent?

| Field | Review |
| --- | --- |
| Upstream | [whylabs/whylogs](https://github.com/whylabs/whylogs) |
| Primary area | Operations & Observability |
| Source commit | [976bc4c15ca1d4a0199360b8d7708b63e4adaa6d](https://github.com/whylabs/whylogs/commit/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/whylabs/whylogs/blob/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Evaluates constraints against compact dataset profiles and reports pass/fail summaries. Setting require_column_existence false can return true when a column or metric is missing. |

## Mechanism worth inspecting

MetricConstraint selects a metric from a profile and evaluates a predicate. The inspected validation branch raises or returns false on missing inputs by default, but can return true when column existence is not required. That option is a direct example of how absence can become green.

**Source trail:** [project overview](https://github.com/whylabs/whylogs/blob/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d/README.md) · [documentation](https://github.com/whylabs/whylogs/blob/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d/python/docs/features/data_validation.md#L39-L54) · [implementation](https://github.com/whylabs/whylogs/blob/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d/python/whylogs/core/constraints/metric_constraints.py#L90-L130) · [additional source](https://github.com/whylabs/whylogs/blob/976bc4c15ca1d4a0199360b8d7708b63e4adaa6d/python/whylogs/core/constraints/metric_constraints.py#L132-L165).

## Important limit

Profile summaries are lossy and cannot reconstruct all failing rows or source events. A critical missing field should be its own fail-closed state rather than an optional constraint.

## Questions to take into your own design

- Does a missing critical column produce an explicit failure?
- Can an aggregate profile be traced back to its input partition?

## Why this score for a trading system

Profile constraints may catch feed changes, but optional missing-column success is dangerous and profiles lose row-level evidence.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
