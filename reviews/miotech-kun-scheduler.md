# Kun Scheduler - Can a data-quality hook fail while the check still reports success?

**Decision question:** Can a data-quality hook fail while the check still reports success?

| Field | Review |
| --- | --- |
| Upstream | [miotech/kun-scheduler](https://github.com/miotech/kun-scheduler) |
| Primary area | Data Quality & Lineage |
| Source commit | [eb11176896d3867ea3fa219a1223c8917461927e](https://github.com/miotech/kun-scheduler/commit/eb11176896d3867ea3fa219a1223c8917461927e) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The executor runs before and after hooks around the main expectation. Hook exceptions are logged and swallowed; execute returns only the main run result, so a failed after-hook can be invisible to its caller. |

## What this project does

An orchestration platform with an expectation executor.

## Mechanism inspected

The executor runs before and after hooks around the main expectation.

## Limitation that matters

Hook exceptions are logged and swallowed; execute returns only the main run result, so a failed after-hook can be invisible to its caller.

## Practical check for a trading system

Make required post-check publication and receipt hooks part of the acceptance status.

## Why this score

2/5. The path exposes a concrete partial-success failure mode.

## Source trail

[README](https://github.com/miotech/kun-scheduler/blob/eb11176896d3867ea3fa219a1223c8917461927e/README.md#L1); [kun-data-quality/kun-data-quality-core/src/main/java/com/miotech/kun/dataquality/core/executor/ExpectationExecutor.java](https://github.com/miotech/kun-scheduler/blob/eb11176896d3867ea3fa219a1223c8917461927e/kun-data-quality/kun-data-quality-core/src/main/java/com/miotech/kun/dataquality/core/executor/ExpectationExecutor.java#L57); [kun-data-quality/kun-data-quality-core/src/main/java/com/miotech/kun/dataquality/core/executor/ExpectationExecutor.java](https://github.com/miotech/kun-scheduler/blob/eb11176896d3867ea3fa219a1223c8917461927e/kun-data-quality/kun-data-quality-core/src/main/java/com/miotech/kun/dataquality/core/executor/ExpectationExecutor.java#L77); [Root license](https://github.com/miotech/kun-scheduler/blob/eb11176896d3867ea3fa219a1223c8917461927e/LICENSE.txt#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
