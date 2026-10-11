# Prefect: A workflow run needs versioned inputs and explicit state hooks

**Decision question:** Which flow version and parameters produced a result?

| Field | Review |
| --- | --- |
| Upstream | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) |
| Primary area | Operations & Observability |
| Source commit | [ee66f26aa603546a9b79e75c56b70385eae570b6](https://github.com/PrefectHQ/prefect/commit/ee66f26aa603546a9b79e75c56b70385eae570b6) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/PrefectHQ/prefect/blob/ee66f26aa603546a9b79e75c56b70385eae570b6/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Offers a flow version, typed parameter validation, and hooks for failure, completion, cancellation, and crash. Parameter validation may coerce values, and a flow version hash does not identify the dataset snapshot. |

## Mechanism worth inspecting

Flow records a version or derives one from the wrapped function’s source file, validates annotated parameters with Pydantic by default, and exposes hooks for terminal and running states. These are useful run-contract elements for batch research tasks.

**Source trail:** [project overview](https://github.com/PrefectHQ/prefect/blob/ee66f26aa603546a9b79e75c56b70385eae570b6/README.md) · [documentation](https://github.com/PrefectHQ/prefect/blob/ee66f26aa603546a9b79e75c56b70385eae570b6/README.md#L20-L45) · [implementation](https://github.com/PrefectHQ/prefect/blob/ee66f26aa603546a9b79e75c56b70385eae570b6/src/prefect/flows.py#L145-L225) · [additional source](https://github.com/PrefectHQ/prefect/blob/ee66f26aa603546a9b79e75c56b70385eae570b6/src/prefect/flows.py#L335-L348).

## Important limit

A code-file hash is not a complete environment or input-data identity. The documented parameter validation can coerce a string such as 5 into an integer, so exact submitted parameters may need separate retention.

## Questions to take into your own design

- Does each run receipt capture exact input bytes, normalized parameters, and source version?
- Do failure hooks leave an inspectable failure state?

## Why this score for a trading system

Flow versions and state hooks organize jobs, but they do not identify market-data snapshots or prove a result is reproducible.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
