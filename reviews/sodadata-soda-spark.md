# Soda Spark — A cleanup wrapper can suppress an exception

**Decision question:** Can a database adapter hide an error from its caller?

| Field | Review |
| --- | --- |
| Upstream | [Soda Spark](https://github.com/sodadata/soda-spark) |
| Primary area | Data Quality & Lineage |
| Source commit | [5d340e4008ce975ce54984351cff7171df20d75e](https://github.com/sodadata/soda-spark/commit/5d340e4008ce975ce54984351cff7171df20d75e) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/sodadata/soda-spark/blob/5d340e4008ce975ce54984351cff7171df20d75e/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The inspected cursor context manager closes its cursor in __exit__ and returns True. This is a source observation about the wrapper, not a demonstrated end-to-end false-positive scan. |

## Project overview

Legacy adapter exposing Soda SQL data checks on Spark DataFrames. [Documentation](https://github.com/sodadata/soda-spark/blob/5d340e4008ce975ce54984351cff7171df20d75e/README.md).

## Mechanism worth inspecting

The inspected cursor context manager closes its cursor in __exit__ and returns True. Under Python context-manager semantics, that return can suppress an exception raised inside the managed block. [Source](https://github.com/sodadata/soda-spark/blob/5d340e4008ce975ce54984351cff7171df20d75e/src/sodaspark/scan.py#L24-L48).

## Important limit

This is a source observation about the wrapper, not a demonstrated end-to-end false-positive scan. Caller and engine behavior would need separate validation. [Evidence 1](https://github.com/sodadata/soda-spark/blob/5d340e4008ce975ce54984351cff7171df20d75e/src/sodaspark/scan.py#L24-L48). [Evidence 2](https://github.com/sodadata/soda-spark/blob/5d340e4008ce975ce54984351cff7171df20d75e/README.md#L11-L22).

## Questions to take into your own design

- Does cleanup propagate a query failure to the run receipt?
- Can error-handling tests distinguish cleanup success from validation success?

## Why this score for a trading system

A concrete silent-error boundary in an older adapter; no reason to adopt another validation engine for it.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
