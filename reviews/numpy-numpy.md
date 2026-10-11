# NumPy — an empty sum is not evidence of zero activity

**Decision question:** Can an all-missing input become a plausible zero in a trading report?

| Field | Review |
| --- | --- |
| Upstream | [NumPy](https://github.com/numpy/numpy) |
| Primary area | Data Quality & Lineage |
| Source commit | [a98529dfd92d73fd4d40ebaaf285cf2463bb92b1](https://github.com/numpy/numpy/commit/a98529dfd92d73fd4d40ebaaf285cf2463bb92b1) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/numpy/numpy/blob/a98529dfd92d73fd4d40ebaaf285cf2463bb92b1/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its NaN-aware sum deliberately returns zero for all-missing and empty slices. Trading reports need a separate coverage field so absent evidence cannot look like zero activity or zero loss. |

## Project overview

NumPy provides multidimensional arrays and numerical operations; its NaN-aware reductions define how missing observations affect aggregates. [Project documentation](https://github.com/numpy/numpy/blob/a98529dfd92d73fd4d40ebaaf285cf2463bb92b1/numpy/lib/_nanfunctions_impl.py#L640-L663).

## Mechanism worth inspecting

`nansum` replaces NaNs with zero before calling `sum`. The documented result for an empty or all-NaN slice is zero. This is an intentional numerical contract, and an important distinction when zero also means no trades, no flow or no loss. [Implementation](https://github.com/numpy/numpy/blob/a98529dfd92d73fd4d40ebaaf285cf2463bb92b1/numpy/lib/_nanfunctions_impl.py#L730-L732); [documented behavior](https://github.com/numpy/numpy/blob/a98529dfd92d73fd4d40ebaaf285cf2463bb92b1/numpy/lib/_nanfunctions_impl.py#L640-L647).

## Important limit

The scalar does not carry data coverage or an explanation for missing values. A correct numerical reduction can therefore be an invalid business observation. Preserve expected count, observed count and validity separately rather than changing all zeros to missing.

## Questions to take into your own design

- Does a zero aggregate distinguish a complete empty period from a missing feed?
- Can downstream thresholds reject an aggregate whose valid-observation count is insufficient?

## Why this score for a trading system

3/5: a fundamental missing-data contract with direct consequences for research and reporting; domain coverage controls remain application work.

**Scope of this review:** NaN-aware sum semantics, not a general NumPy correctness or performance audit.
