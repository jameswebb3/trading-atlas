# DataLineagePy - Does an unknown quality rule count as a completed check?

**Decision question:** Does an unknown quality rule count as a completed check?

| Field | Review |
| --- | --- |
| Upstream | [Arbaznazir/DataLineagePy](https://github.com/Arbaznazir/DataLineagePy) |
| Primary area | Data Quality & Lineage |
| Source commit | [669425617baf50805e48fe2fe7a3cbc92d7e6bba](https://github.com/Arbaznazir/DataLineagePy/commit/669425617baf50805e48fe2fe7a3cbc92d7e6bba) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The validator records an unknown rule as skipped and tallies passed, warning and error outcomes separately. Skipped rules are not counted as errors; a caller that checks only errors can miss a requested contract that never ran. |

## What this project does

A Python data-lineage library with named validation rules.

## Mechanism inspected

The validator records an unknown rule as skipped and tallies passed, warning and error outcomes separately.

## Limitation that matters

Skipped rules are not counted as errors; a caller that checks only errors can miss a requested contract that never ran.

## Practical check for a trading system

Fail the acceptance gate when any required rule is skipped, and retain rule-level results.

## Why this score

2/5. The explicit skipped state is useful if consumers make it blocking.

## Source trail

[README](https://github.com/Arbaznazir/DataLineagePy/blob/669425617baf50805e48fe2fe7a3cbc92d7e6bba/README.md#L1); [datalineagepy/core/validation.py](https://github.com/Arbaznazir/DataLineagePy/blob/669425617baf50805e48fe2fe7a3cbc92d7e6bba/datalineagepy/core/validation.py#L59); [datalineagepy/core/validation.py](https://github.com/Arbaznazir/DataLineagePy/blob/669425617baf50805e48fe2fe7a3cbc92d7e6bba/datalineagepy/core/validation.py#L91); [Root license](https://github.com/Arbaznazir/DataLineagePy/blob/669425617baf50805e48fe2fe7a3cbc92d7e6bba/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
