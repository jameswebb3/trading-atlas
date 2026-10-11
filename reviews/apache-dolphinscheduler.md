# dolphinscheduler — A state machine should reject unknown states

**Decision question:** Can an unhandled task state be silently accepted?

| Field | Review |
| --- | --- |
| Upstream | [dolphinscheduler](https://github.com/apache/dolphinscheduler) |
| Primary area | Research & Reproducibility |
| Source commit | [93cb9a26b70f7fec4bc20232d93a6647708358f8](https://github.com/apache/dolphinscheduler/commit/93cb9a26b70f7fec4bc20232d93a6647708358f8) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The factory registers actions by execution status and verifies that every enum value has one, throwing for an unmapped state. Exhaustive state mapping says nothing about scientific acceptance or trial data quality; the platform is far larger than needed. |

## What this project does

A general workflow scheduler with explicit task-state actions. [README](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/README.md).

## Mechanism inspected

The factory registers actions by execution status and verifies that every enum value has one, throwing for an unmapped state. [Implementation](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/dolphinscheduler-master/src/main/java/org/apache/dolphinscheduler/server/master/engine/task/statemachine/TaskStateActionFactory.java#L29-L46).

## Limitation that matters

Exhaustive state mapping says nothing about scientific acceptance or trial data quality; the platform is far larger than needed. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add an exhaustive local test for all trial states and fail closed on a newly introduced status.

## Why this score

Transferable engineering pattern: The factory registers actions by execution status and verifies that every enum value has one, throwing for an unmapped state. Exhaustive state mapping says nothing about scientific acceptance or trial data quality; the platform is far larger than needed.

## Source trail

[README](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/README.md) · [Documentation](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/docs/docs/en/guide/monitor.md) · [Implementation](https://github.com/apache/dolphinscheduler/blob/93cb9a26b70f7fec4bc20232d93a6647708358f8/dolphinscheduler-master/src/main/java/org/apache/dolphinscheduler/server/master/engine/task/statemachine/TaskStateActionFactory.java#L29-L46).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
