# tsfresh — record which family received multiplicity correction

**Decision question:** What does feature-selection FDR actually cover?

| Field | Review |
| --- | --- |
| Upstream | [tsfresh](https://github.com/blue-yonder/tsfresh) |
| Primary area | Signals & Models |
| Source commit | [6af3c0030b6c9f02c3862a20e00cce87c984aa5b](https://github.com/blue-yonder/tsfresh/commit/6af3c0030b6c9f02c3862a20e00cce87c984aa5b) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/blue-yonder/tsfresh/blob/6af3c0030b6c9f02c3862a20e00cce87c984aa5b/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | An explicit reference for dependence-aware feature selection. Its FDR correction applies to the supplied table; repeated searches and invalid temporal p-values still need their own accounting. |

## Project overview

tsfresh extracts time-series features and selects relevant features with statistical tests and multiple-testing correction. [Project documentation](https://github.com/blue-yonder/tsfresh/blob/6af3c0030b6c9f02c3862a20e00cce87c984aa5b/tsfresh/feature_selection/relevance.py#L31-L55).

## Mechanism worth inspecting

The relevance calculation builds a p-value table and selects Benjamini–Hochberg when independence is asserted, otherwise Benjamini–Yekutieli. The dependence assumption changes the correction and is explicitly documented. [Assumption](https://github.com/blue-yonder/tsfresh/blob/6af3c0030b6c9f02c3862a20e00cce87c984aa5b/tsfresh/feature_selection/relevance.py#L122-L129); [selection](https://github.com/blue-yonder/tsfresh/blob/6af3c0030b6c9f02c3862a20e00cce87c984aa5b/tsfresh/feature_selection/relevance.py#L329-L349).

## Important limit

Correction of one feature table is not correction of every searched horizon, target, cutoff and repeated run. It also cannot repair invalid p-values from serially dependent samples. Combining tables uses the minimum p-value and an OR of relevance, which deserves a separate interpretation. [Table combination](https://github.com/blue-yonder/tsfresh/blob/6af3c0030b6c9f02c3862a20e00cce87c984aa5b/tsfresh/feature_selection/relevance.py#L377-L393).

## Questions to take into your own design

- Does the experiment ledger identify the entire tested feature/horizon family?
- Were p-values constructed with a temporal dependence model before FDR correction?

## Why this score for a trading system

3/5: an inspectable feature-family correction mechanism; financial sampling validity and campaign-wide search accounting require additional controls.

**Scope of this review:** Relevance testing and table combination, not a review of every extracted feature.
