# Pandera: Collect row failures without quietly changing the dataset

**Decision question:** Can a schema report all bad rows while preserving the original sample?

| Field | Review |
| --- | --- |
| Upstream | [unionai-oss/pandera](https://github.com/unionai-oss/pandera) |
| Primary area | Data Quality & Lineage |
| Source commit | [bf4fa9c9dabf0e87b76675f8ab332db67232db3b](https://github.com/unionai-oss/pandera/commit/bf4fa9c9dabf0e87b76675f8ab332db67232db3b) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/unionai-oss/pandera/blob/bf4fa9c9dabf0e87b76675f8ab332db67232db3b/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Lazy validation collects multiple schema failures and exposes row-level failure cases. The optional drop-invalid-rows path changes the sample and must be an explicit decision in research. |

## Project overview

Dataframe validation library for schemas, types, and custom checks. Collects row-level failure details, helping research pipelines identify invalid inputs before building features or evaluating strategies.

[Project documentation](https://github.com/unionai-oss/pandera/blob/bf4fa9c9dabf0e87b76675f8ab332db67232db3b/README.md#L34-L42).

## Mechanism worth inspecting

The lazy-validation guide shows aggregated failure cases rather than stopping at the first error. The pandas backend collects errors across parsers and checks; if drop_invalid_rows is enabled, it may return a reduced frame instead of raising all collected errors.

**Source trail:** [project overview](https://github.com/unionai-oss/pandera/blob/bf4fa9c9dabf0e87b76675f8ab332db67232db3b/README.md) · [documentation](https://github.com/unionai-oss/pandera/blob/bf4fa9c9dabf0e87b76675f8ab332db67232db3b/docs/source/lazy_validation.md#L45-L92) · [implementation](https://github.com/unionai-oss/pandera/blob/bf4fa9c9dabf0e87b76675f8ab332db67232db3b/pandera/backends/pandas/container.py#L68-L156).

## Important limit

Row removal can change sample composition and downstream metrics. A schema can verify columns and values but cannot infer whether a value was available at the decision timestamp unless that rule is encoded.

## Questions to take into your own design

- Does a quality gate report the excluded rows and denominator?
- Is row removal forbidden or separately approved before evaluation?

## Why this score for a trading system

Aggregated row failures can protect a research sample, but optional invalid-row dropping can silently change the population.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
