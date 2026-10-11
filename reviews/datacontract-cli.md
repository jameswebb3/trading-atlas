# Data Contract CLI: portable checks still need a coverage contract

**Decision question:** What does a freshness check actually prove about a dataset?

| Field | Review |
| --- | --- |
| Upstream | [datacontract/datacontract-cli](https://github.com/datacontract/datacontract-cli) |
| Primary area | Data Quality & Lineage |
| Source commit | [4939107524060c725f88fe6b517de4aba05d3139](https://github.com/datacontract/datacontract-cli/commit/4939107524060c725f88fe6b517de4aba05d3139) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/datacontract/datacontract-cli/blob/4939107524060c725f88fe6b517de4aba05d3139/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Defines quality rules as a named metric, arguments, and one comparator, then compiles them for data backends. The inspected freshness query compares MAX(timestamp) with now; a recent row can hide missing interior intervals. |

## Mechanism worth inspecting

The [README](https://github.com/datacontract/datacontract-cli/blob/4939107524060c725f88fe6b517de4aba05d3139/README.md#L15-L35) frames schema, quality, and service levels as one data contract. Its [library rule format](https://github.com/datacontract/datacontract-cli/blob/4939107524060c725f88fe6b517de4aba05d3139/docs/docs/quality-rules/library.md#L7-L31) names a metric, optional arguments, and one comparator; row counts, duplicate values, nulls, and explicit missing sentinels have distinct meanings. In the inspected HANA backend, the [freshness check](https://github.com/datacontract/datacontract-cli/blob/4939107524060c725f88fe6b517de4aba05d3139/datacontract/engines/hana/hana_quality_check.py#L493-L520) computes seconds since the maximum timestamp and compares it with a threshold.

## Important limit

A fresh maximum proves there is a recent row, not that every expected interval or symbol is present. A contract for time-series research also needs per-series cadence, interior-gap counts, the timestamp's meaning, and the observed denominator. We inspected this backend's query, not every engine's implementation.

## Questions to take into your own design

- Is the metric's unit and denominator explicit?
- Does freshness mean newest row only or continuous coverage?
- Are unavailable and invalid results distinct from a measured zero?

## Why this score for a trading system

Named data-quality rules transfer to trading feeds, but a last-timestamp freshness check can miss interior market-data gaps.

**Scope of this review:** We read the pinned README, library-rule documentation, and one HANA implementation. We did not execute a contract or compare other backends.
