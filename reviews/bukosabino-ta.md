# Technical Analysis Library in Python — Can filling missing indicator values introduce future information

**Decision question:** Can filling missing indicator values introduce future information?

| Field | Review |
| --- | --- |
| Upstream | [Technical Analysis Library in Python](https://github.com/bukosabino/ta) |
| Primary area | Signals & Models |
| Source commit | [a890410710a6e483c9ba08da7f3dd5089e4b9dff](https://github.com/bukosabino/ta/commit/a890410710a6e483c9ba08da7f3dd5089e4b9dff) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/bukosabino/ta/blob/a890410710a6e483c9ba08da7f3dd5089e4b9dff/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Shows how optional filling can both shorten warm-up and backfill leading gaps from later values. Useful for causal feature tests, with the risky branch clearly distinguished from the default behavior. |

## Project overview

A pandas- and NumPy-based feature library for OHLCV time series. [Project documentation](https://github.com/bukosabino/ta/blob/a890410710a6e483c9ba08da7f3dd5089e4b9dff/README.md#L10-L16).

## Mechanism worth inspecting

When fillna is enabled and the helper's replacement value is minus one, it applies forward fill followed by backward fill. That second step can fill leading gaps from later data. Separately, SMA and EMA helpers change min_periods to zero when fillna is enabled. [Fill policy and warm-up](https://github.com/bukosabino/ta/blob/a890410710a6e483c9ba08da7f3dd5089e4b9dff/ta/utils.py#L17-L36), [rolling helpers](https://github.com/bukosabino/ta/blob/a890410710a6e483c9ba08da7f3dd5089e4b9dff/ta/utils.py#L59-L66).

## Important limit

The behavior is conditional: fillna defaults to false, and backward fill requires the minus-one branch. It would be inaccurate to claim that every indicator or default calculation leaks future data.

## Questions to take into your own design

- Does adding future data change an earlier filled indicator value?
- Are shortened warm-up and filled outputs distinguished from fully observed values?

## Why this score for a trading system

3/5: a directly relevant, conditional leakage example that can become a small deterministic test.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
