# Apache Airflow — Can a workflow report success while an important intermediate task failed

**Decision question:** Can a workflow report success while an important intermediate task failed?

| Field | Review |
| --- | --- |
| Upstream | [Apache Airflow](https://github.com/apache/airflow) |
| Primary area | Research & Reproducibility |
| Source commit | [1d916545b2b1bb36ca79c8d7691f7b662419348c](https://github.com/apache/airflow/commit/1d916545b2b1bb36ca79c8d7691f7b662419348c) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/apache/airflow/blob/1d916545b2b1bb36ca79c8d7691f7b662419348c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Documents a workflow-success rule that can conceal an intermediate failure behind a successful terminal task. Useful for separating completed orchestration from valid research output. |

## Project overview

A platform for defining, scheduling and monitoring task workflows through directed acyclic graphs. [Project documentation](https://github.com/apache/airflow/blob/1d916545b2b1bb36ca79c8d7691f7b662419348c/README.md#L45-L49).

## Mechanism worth inspecting

The documented DAG outcome depends on leaf states, and the guide warns that a successful all_done leaf can mask an intermediate failure. Source selects effective leaves, treating teardown tasks specially, before assigning success when all selected terminal tasks are successful. [Outcome caveat](https://github.com/apache/airflow/blob/1d916545b2b1bb36ca79c8d7691f7b662419348c/airflow-core/docs/core-concepts/dag-run.rst#L29-L41); [effective leaves](https://github.com/apache/airflow/blob/1d916545b2b1bb36ca79c8d7691f7b662419348c/airflow-core/src/airflow/models/dagrun.py#L1169-L1191), [success branch](https://github.com/apache/airflow/blob/1d916545b2b1bb36ca79c8d7691f7b662419348c/airflow-core/src/airflow/models/dagrun.py#L1351-L1355).

## Important limit

The outcome describes the graph's completion rule, not research validity. Cleanup success must not substitute for required data, checks or output artefacts.

## Questions to take into your own design

- Are all required research checks evaluated independently of the terminal cleanup task?
- Can a successful final report conceal a missing upstream artefact?

## Why this score for a trading system

3/5: a precise transferable failure mode at the workflow-to-evidence boundary.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
