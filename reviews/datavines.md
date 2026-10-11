# DataVines: inspect what a freshness rule actually counts

**Decision question:** Does a rule named freshness measure age, interval coverage, or timestamp validity?

| Field | Review |
| --- | --- |
| Upstream | [DataVines](https://github.com/datavane/datavines) |
| Primary area | Data Quality & Lineage |
| Source commit | [c0a8ed89317668279fd325c39d5ffefb54c0f724](https://github.com/datavane/datavines/commit/c0a8ed89317668279fd325c39d5ffefb54c0f724) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/datavane/datavines/blob/c0a8ed89317668279fd325c39d5ffefb54c0f724/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Provides scheduled SQL quality checks, profiling, and error-row output. Its freshness plugin builds a timestamp-window filter from configured boundaries; readers should not infer stream completeness or maximum data age from the rule's name. |

## Project overview

A pluggable data-quality service supports single-table rules, cross-table comparisons, scheduling, and result alerts through local JDBC or distributed engines. [Project documentation](https://github.com/datavane/datavines/blob/c0a8ed89317668279fd325c39d5ffefb54c0f724/README.md#L43-L62).

## Mechanism worth inspecting

The [freshness plugin configuration](https://github.com/datavane/datavines/blob/c0a8ed89317668279fd325c39d5ffefb54c0f724/datavines-metric/datavines-metric-plugins/datavines-metric-table-freshness/src/main/java/io/datavines/metric/plugin/Freshness.java#L29-L39) requires begin_time, deadline_time, and datetime_format. [Preparation](https://github.com/datavane/datavines/blob/c0a8ed89317668279fd325c39d5ffefb54c0f724/datavines-metric/datavines-metric-plugins/datavines-metric-table-freshness/src/main/java/io/datavines/metric/plugin/Freshness.java#L61-L77) delegates a time-window predicate to the connector and permits invalid-item output. The [plugin architecture](https://github.com/datavane/datavines/blob/c0a8ed89317668279fd325c39d5ffefb54c0f724/README.md#L75-L89) separates rules, engines, and error-data storage.

## Important limit

Connector-specific SQL and a result formula determine the final metric; the inspected plugin does not itself compare the newest event to the decision clock or enumerate expected missing intervals. Error-data output is also engine-dependent in the documented architecture.

## Questions to take into your own design

- Can the check's result state its exact predicate, population, and expected count?
- Are timestamp-window validity and expected-event completeness separate checks?

## Why this score for a trading system

2/5: useful separation of query predicates and invalid-row evidence, but the inspected freshness rule is too generic to establish market-feed reliability.

**Scope of this review:** README architecture/features and the complete freshness plugin; connector SQL generation and scheduler failover not verified.
