# TensorZero: Run an evaluation against a frozen configuration

**Decision question:** Can an agent comparison silently change its evaluator between runs?

| Field | Review |
| --- | --- |
| Upstream | [tensorzero/tensorzero](https://github.com/tensorzero/tensorzero) |
| Primary area | Agents & Decision Systems |
| Source commit | [62eb8f63e8ec62018d70420dbf1a8c5d1c026315](https://github.com/tensorzero/tensorzero/commit/62eb8f63e8ec62018d70420dbf1a8c5d1c026315) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/tensorzero/tensorzero/blob/62eb8f63e8ec62018d70420dbf1a8c5d1c026315/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Requires an unambiguous evaluation selection and sends the action under a config snapshot hash. A frozen evaluator config still needs a frozen dataset and reported sample count, especially with adaptive stopping. |

## Mechanism worth inspecting

RunEvaluationToolParams requires one evaluation definition or a function plus evaluator names and selects either a dataset or explicit datapoint IDs. The tool parses a config_snapshot_hash and dispatches the action under that snapshot. It can return means, standard errors, counts, and optional per-point results.

**Source trail:** [project overview](https://github.com/tensorzero/tensorzero/blob/62eb8f63e8ec62018d70420dbf1a8c5d1c026315/README.md) · [documentation](https://github.com/tensorzero/tensorzero/blob/62eb8f63e8ec62018d70420dbf1a8c5d1c026315/README.md#L145-L167) · [implementation](https://github.com/tensorzero/tensorzero/blob/62eb8f63e8ec62018d70420dbf1a8c5d1c026315/crates/autopilot-tools/src/tools/prod/run_evaluation.rs#L20-L81) · [additional source](https://github.com/tensorzero/tensorzero/blob/62eb8f63e8ec62018d70420dbf1a8c5d1c026315/crates/autopilot-tools/src/tools/prod/run_evaluation.rs#L245-L261).

## Important limit

The inspected tool does not itself prove a dataset is immutable. Precision-based early stopping can also make two runs use different N unless the receipt records the stopping rule and actual sample count.

## Questions to take into your own design

- Do repeated evaluations name both evaluator snapshot and dataset snapshot?
- Is actual N retained beside every comparison?

## Why this score for a trading system

A frozen evaluator config could improve agent experiments, but the inspected path does not establish trading relevance or immutable evaluation data.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
