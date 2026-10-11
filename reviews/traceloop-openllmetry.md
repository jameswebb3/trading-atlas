# OpenLLMetry - Evaluator errors should not look like scored rows

**Decision question:** Does an evaluator failure appear in the experiment error count?

| Field | Review |
| --- | --- |
| Upstream | [traceloop/openllmetry](https://github.com/traceloop/openllmetry) |
| Primary area | Operations & Observability |
| Source commit | [df4921a40940cdce136c4409380a55e9d4c7a96d](https://github.com/traceloop/openllmetry/commit/df4921a40940cdce136c4409380a55e9d4c7a96d) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Runs dataset-versioned agent experiments with per-row task and evaluator results under bounded concurrency. Evaluator exceptions are stored as strings inside successful rows rather than in the returned errors list; empty errors does not imply complete evaluation. |

## What this project does

An LLM observability SDK with dataset-backed experiment execution and evaluator calls. The inspected path executes tasks and evaluators per dataset row.

## Mechanism inspected

The runner pins a dataset slug and version, creates one task per row under a semaphore, validates task output for specified evaluators, and returns a results list plus an errors list. Source tests cover output-validation failures.

## Limitation that matters

A task failure becomes TaskResponse.error and reaches the errors list. An evaluator exception instead becomes an Error string inside the evaluations map of a successful TaskResponse, so a caller counting only errors can report a clean experiment even though its evaluator failed. In fire-and-forget mode it returns empty result and error lists after triggering tasks. This is a source review, not a runtime or security test.

## Practical check for a trading system

For strategy or agent evaluation, give task, metric and adjudicator failures distinct typed states. Block promotion whenever a required evaluator lacks a valid result, even if the task itself produced output.

## Why this score

2/5 because dataset-versioned evaluation is transferable, but this LLM SDK has a consequential failure-state ambiguity for evidence-gated decisions.

## Source trail

[README](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/README.md#L1); [Experiment runner](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/packages/traceloop-sdk/traceloop/sdk/experiment/experiment.py#L157); [Evaluator error path](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/packages/traceloop-sdk/traceloop/sdk/experiment/experiment.py#L185); [Result classification](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/packages/traceloop-sdk/traceloop/sdk/experiment/experiment.py#L250); [Validation test](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/packages/traceloop-sdk/tests/experiment/test_experiment.py#L125); [License](https://github.com/traceloop/openllmetry/blob/df4921a40940cdce136c4409380a55e9d4c7a96d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
