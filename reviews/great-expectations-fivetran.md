# Great Expectations (Fivetran fork): Checkpoint results precede downstream actions

**Decision question:** Does a data check carry an inspectable result before a workflow acts?

| Field | Review |
| --- | --- |
| Upstream | [fivetran/great_expectations](https://github.com/fivetran/great_expectations) |
| Primary area | Data Quality & Lineage |
| Source commit | [0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e](https://github.com/fivetran/great_expectations/commit/0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/fivetran/great_expectations/blob/0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Runs named validation definitions and constructs a checkpoint result before executing actions. Only the configured checks and selected batch are evaluated; the checkpoint does not infer missing historical intervals. |

## Mechanism worth inspecting

The checkpoint documentation describes batch parameters, expectation parameters, validation results, and actions. In the implementation, an empty validation set raises, results are collected, then the action list runs against a constructed result. That ordering makes the evidence passed to each action explicit.

**Source trail:** [project overview](https://github.com/fivetran/great_expectations/blob/0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e/README.md) · [documentation](https://github.com/fivetran/great_expectations/blob/0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e/docs/docusaurus/docs/core/trigger_actions_based_on_results/run_a_checkpoint.md#L72-L81) · [implementation](https://github.com/fivetran/great_expectations/blob/0ffedfd29c2a53e05f10d46bbdac1cccb32ccb9e/great_expectations/checkpoint/checkpoint.py#L314-L341).

## Important limit

A green checkpoint only covers its selected definitions and batch. It does not establish causal availability, full feed coverage, or a gap-free history without checks for those conditions. This review is of the Fivetran fork at the pinned commit.

## Questions to take into your own design

- Does every action receive the exact validation result that authorized it?
- Is a missing interval modeled as a failing expectation?

## Why this score for a trading system

Checkpoint ordering is a generic quality-gate pattern; the inspected rules do not supply trading-specific continuity or time checks.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
