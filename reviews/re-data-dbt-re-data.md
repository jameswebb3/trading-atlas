# re_data — Anomaly scores need an absence state

**Decision question:** How should monitoring distinguish normal data from no current measurement?

| Field | Review |
| --- | --- |
| Upstream | [re-data/dbt-re-data](https://github.com/re-data/dbt-re-data) |
| Primary area | Data Quality & Lineage |
| Source commit | [c93f125b3f4350fac914cfd82c0db37a30c81ad0](https://github.com/re-data/dbt-re-data/commit/c93f125b3f4350fac914cfd82c0db37a30c81ad0) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The SQL computes z-scores from current values and historical statistics, then applies a configured alert threshold. If a current value or baseline is null, the arithmetic does not produce a meaningful score; missing observation should not read as no anomaly. |

## What this project does

A dbt package for warehouse reliability metrics and anomaly alerts. [Project README](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/README.md#L1).

## Mechanism inspected

The SQL computes z-scores from current values and historical statistics, then applies a configured alert threshold. [Implementation](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/models/alerts/re_data_z_score.sql#L9). [Related source 1](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/models/alerts/re_data_anomalies.sql#L36). [Related source 2](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/integration_tests/README.md#L1).

## Limitation that matters

If a current value or baseline is null, the arithmetic does not produce a meaningful score; missing observation should not read as no anomaly. This is a source review, not a runtime or security test.

## Practical check for a trading system

Emit a separate missing-data status and cadence breach before interpreting any anomaly score.

## Why this score

The SQL is a useful example of metric/baseline coupling, but its warehouse stack is unnecessary for simple market-data gates.

## Source trail

[README](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/README.md#L1); [Implementation](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/models/alerts/re_data_z_score.sql#L9); [Related source 1](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/models/alerts/re_data_anomalies.sql#L36); [Related source 2](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/integration_tests/README.md#L1) - [License](https://github.com/re-data/dbt-re-data/blob/c93f125b3f4350fac914cfd82c0db37a30c81ad0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
