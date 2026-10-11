# Swiple — Persist the validation result, not just the task result

**Decision question:** Can a completed worker task still contain failed data checks?

| Field | Review |
| --- | --- |
| Upstream | [Swiple](https://github.com/Swiple/swiple) |
| Primary area | Data Quality & Lineage |
| Source commit | [35c639a6773c39ef08cbf4becde6ac56f9e82e54](https://github.com/Swiple/swiple/commit/35c639a6773c39ef08cbf4becde6ac56f9e82e54) |
| Reviewed | 2026-09-27 |
| Declared license | [Elastic License 2.0 (source available)](https://github.com/Swiple/swiple/blob/35c639a6773c39ef08cbf4becde6ac56f9e82e54/LICENSE.md) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Runner validates an expectation suite, preserves run identifiers and dispatches an action based on validation.success. Worker completion and document persistence do not mean every expectation passed. |

## Project overview

Data-quality monitoring interface using expectation-based validation, scheduling and alerts; source available under Elastic License 2.0. [Documentation](https://github.com/Swiple/swiple/blob/35c639a6773c39ef08cbf4becde6ac56f9e82e54/README.md).

## Mechanism worth inspecting

Runner validates an expectation suite, preserves run identifiers and dispatches an action based on validation.success. The worker stores the resulting validation document under a new identifier. [Source](https://github.com/Swiple/swiple/blob/35c639a6773c39ef08cbf4becde6ac56f9e82e54/backend/app/core/runner.py#L111-L166).

## Important limit

Worker completion and document persistence do not mean every expectation passed. Elastic License 2.0 adds usage restrictions; this is not an unrestricted open-source monitoring component. [Evidence 1](https://github.com/Swiple/swiple/blob/35c639a6773c39ef08cbf4becde6ac56f9e82e54/backend/app/core/runner.py#L111-L166). [Evidence 2](https://github.com/Swiple/swiple/blob/35c639a6773c39ef08cbf4becde6ac56f9e82e54/backend/app/worker/tasks/validation.py#L1-L18).

## Questions to take into your own design

- Does the stored receipt expose validation.success independently of task completion?
- Are expectation exceptions retained alongside ordinary check failures?

## Why this score for a trading system

A relevant result-recording pattern already common in quality systems, with restricted licensing and a larger service footprint.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
