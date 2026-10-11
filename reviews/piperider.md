# PipeRider: review data changes beside code changes

**Decision question:** Can unchanged SQL still produce a changed downstream dataset?

| Field | Review |
| --- | --- |
| Upstream | [PipeRider](https://github.com/InfuseAI/piperider) |
| Primary area | Data Quality & Lineage |
| Source commit | [523762ca163640bb34b4d4efe66d15880cc8be8c](https://github.com/InfuseAI/piperider/commit/523762ca163640bb34b4d4efe66d15880cc8be8c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Compares dbt profiling reports and separates code changes from observed data changes. The useful pattern is reviewing downstream row, column, and profile differences before merging; the project declares that it has been superseded by Recce. |

## Project overview

A data-review CLI compares base and target dbt runs, profiles models, and reports downstream impact. [Project documentation](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/README.md#L19-L38).

## Mechanism worth inspecting

The [comparison interface](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/docs/commands/piperider-compare-report.md#L8-L22) takes explicit base and target report files. [Implicit data-change detection](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/piperider_cli/dbt/changeset.py#L902-L927) compares row counts, column counts, and per-column profiles only when both tables were profiled. [Profile comparison](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/piperider_cli/dbt/changeset.py#L52-L75) checks columns from both sides so additions and removals affect the result.

## Important limit

A profile summary can stay equal while individual records change. [Comparison scope](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/piperider_cli/compare_report.py#L157-L183) can trim one side to resources in the other. The [maintenance notice](https://github.com/InfuseAI/piperider/blob/523762ca163640bb34b4d4efe66d15880cc8be8c/README.md#L16-L17) says PipeRider is superseded and no longer regularly updated; use the review pattern rather than assuming current integration support.

## Questions to take into your own design

- Does a data-transform change include a base/target report at the same dataset vintage?
- Are skipped or unprofiled resources visible rather than counted as unchanged?

## Why this score for a trading system

2/5: a practical data-review pattern with explicit coverage limits, reduced by declared maintenance status and profile-level comparison.

**Scope of this review:** README maintenance notice, comparison command documentation, scope selection, and implicit/profile comparison source.
