# Datachecks: a metric name does not establish its measurement scope

**Decision question:** Does a freshness check measure the same filtered dataset as a completeness check?

| Field | Review |
| --- | --- |
| Upstream | [Datachecks](https://github.com/datachecks/dcs-core) |
| Primary area | Data Quality & Lineage |
| Source commit | [425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9](https://github.com/datachecks/dcs-core/commit/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Provides configurable database quality metrics and thresholds. The inspected count and completeness paths forward filters, while the freshness value metric delegates only the table and timestamp field; measurement scope deserves an explicit contract. |

## Project overview

A database monitoring tool exposes reliability, uniqueness, completeness, numeric-distribution, and custom SQL checks. [Project documentation](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/README.md#L37-L47).

## Mechanism worth inspecting

The [configuration reference](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/docs/configuration/metric_configuration.md#L14-L22) exposes optional where filters and threshold expressions. [Row-count metrics](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/dcs_core/core/metric/reliability_metric.py#L46-L67) pass the configured filter to the data source. [Null validations](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/dcs_core/core/validation/completeness_validation.py#L24-L67) do the same, making the measured population explicit in their call.

## Important limit

The [freshness value metric](https://github.com/datachecks/dcs-core/blob/425a7f973b1fd07c80cf5a328b59aa6ef3c4ced9/dcs_core/core/metric/reliability_metric.py#L70-L95) supplies the dataset and timestamp field without forwarding filter_query. A whole-table recent timestamp cannot establish freshness for every symbol or partition. This is a source-level observation about this metric class, not a runtime finding about all Datachecks checks.

## Questions to take into your own design

- Can each check expose the exact population and timestamp field it measured?
- Can one recently updated symbol mask stale partitions in an aggregate freshness check?

## Why this score for a trading system

2/5: straightforward monitoring contracts with a concrete scope inconsistency to inspect. Market-specific completeness and per-partition freshness need additional design.

**Scope of this review:** README, metric configuration, reliability metrics, and null-validation implementation; connectors and other freshness validation classes not audited.
