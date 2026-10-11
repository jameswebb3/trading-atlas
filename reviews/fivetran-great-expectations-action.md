# Great Expectations Action — Debug mode changes the gate

**Decision question:** Does a failed checkpoint always fail the automation job?

| Field | Review |
| --- | --- |
| Upstream | [fivetran/great_expectations_action](https://github.com/fivetran/great_expectations_action) |
| Primary area | Data Quality & Lineage |
| Source commit | [5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5](https://github.com/fivetran/great_expectations_action/commit/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The shell loop collects failed checkpoint names and a failure flag; it exits nonzero only when its debug input is unset. With debug enabled, a failed validation can complete the action successfully ([source](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/run_checkpoints.sh#L83-L88)). |

## What this project does

A GitHub Action that runs one or more Great Expectations checkpoints. [Project README](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/README.md#L1).

## Mechanism inspected

The shell loop collects failed checkpoint names and a failure flag; it exits nonzero only when its debug input is unset. [Implementation](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/run_checkpoints.sh#L25).

## Limitation that matters

With debug enabled, a failed validation can complete the action successfully ([source](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/run_checkpoints.sh#L83-L88)). A report link or output flag cannot substitute for the process exit code. This is a source review, not a runtime or security test.

## Practical check for a trading system

Test the gate in every configured mode and require explicit failure propagation before downstream trading data is accepted.

## Why this score

The source exposes a precise config-dependent false green in a quality gate.

## Source trail

[README](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/README.md#L1); [Implementation](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/run_checkpoints.sh#L25) - [License](https://github.com/fivetran/great_expectations_action/blob/5d719a6d2828fb263e8226ab3ad4e4902f1a2ed5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
