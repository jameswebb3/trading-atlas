# aeon — replacing undefined features changes their meaning

**Decision question:** Does a feature vector distinguish undefined statistics from genuine zeros?

| Field | Review |
| --- | --- |
| Upstream | [aeon](https://github.com/aeon-toolkit/aeon) |
| Primary area | Signals & Models |
| Source commit | [b41692460188f670dd60b25356bf6929430b6c9a](https://github.com/aeon-toolkit/aeon/commit/b41692460188f670dd60b25356bf6929430b6c9a) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/aeon-toolkit/aeon/blob/b41692460188f670dd60b25356bf6929430b6c9a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Catch22 makes its missing-feature policy explicit. Optional NaN and infinity replacement produces zeros, so a trading feature contract should preserve validity rather than silently treating every output as observed. |

## Project overview

aeon is a time-series learning toolkit; its Catch22 transform produces a compact set of descriptive features. [Project documentation](https://github.com/aeon-toolkit/aeon/blob/b41692460188f670dd60b25356bf6929430b6c9a/aeon/transformations/collection/feature_based/_catch22.py#L96-L138).

## Mechanism worth inspecting

Catch22 exposes `replace_nans`. When enabled, the implementation converts NaN and positive/negative infinity to zero in the feature array. The default at this pin is false. [Constructor](https://github.com/aeon-toolkit/aeon/blob/b41692460188f670dd60b25356bf6929430b6c9a/aeon/transformations/collection/feature_based/_catch22.py#L208-L219); [replacement](https://github.com/aeon-toolkit/aeon/blob/b41692460188f670dd60b25356bf6929430b6c9a/aeon/transformations/collection/feature_based/_catch22.py#L412-L415).

## Important limit

Zero imputation merges undefined behavior with an observed value of zero unless validity is preserved separately. Catch22 summarizes its whole supplied window; neither imputation nor extraction defines a live prediction cutoff or makes these features trading alpha.

## Questions to take into your own design

- Do constant, short or otherwise degenerate windows retain feature-validity flags?
- Does the same missingness policy apply in historical replay and live feature production?

## Why this score for a trading system

2/5: a concrete feature-validity caution, but another generic descriptor set offers limited incremental value to trading without independent validation.

**Scope of this review:** Catch22 NaN replacement and its supplied-window contract, not all aeon estimators.
