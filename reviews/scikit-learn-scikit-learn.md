# Scikit-learn — Does a time-series gap represent elapsed time or rows

**Decision question:** Does a time-series gap represent elapsed time or rows?

| Field | Review |
| --- | --- |
| Upstream | [Scikit-learn](https://github.com/scikit-learn/scikit-learn) |
| Primary area | Research & Reproducibility |
| Source commit | [857849927da6e988d7d026b17aef214d43e5f26e](https://github.com/scikit-learn/scikit-learn/commit/857849927da6e988d7d026b17aef214d43e5f26e) |
| Reviewed | 2026-09-26 |
| Declared license | [BSD-3-Clause](https://github.com/scikit-learn/scikit-learn/blob/857849927da6e988d7d026b17aef214d43e5f26e/COPYING) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A strong general ML reference with a consequential time-series caveat: its gap counts samples. Trading validation must separately enforce label overlap, elapsed-time embargoes and historical availability. |

## Project overview

Scikit-learn provides machine-learning estimators and validation utilities. This review focuses on the contract of its time-series splitter. [Project documentation](https://github.com/scikit-learn/scikit-learn/blob/857849927da6e988d7d026b17aef214d43e5f26e/README.rst#L49-L58).

## Mechanism worth inspecting

TimeSeriesSplit explicitly defines gap as a sample count and requires equally spaced samples for comparable fold durations. The implementation computes the training endpoint by subtracting that count from the test start. [API contract](https://github.com/scikit-learn/scikit-learn/blob/857849927da6e988d7d026b17aef214d43e5f26e/sklearn/model_selection/_split.py#L1116-L1161), [split construction](https://github.com/scikit-learn/scikit-learn/blob/857849927da6e988d7d026b17aef214d43e5f26e/sklearn/model_selection/_split.py#L1299-L1330).

## Important limit

A sample-count gap is not a purge based on label end-times or a fixed elapsed-time embargo. Irregular trading observations need explicit timestamps and information-availability checks.

## Questions to take into your own design

- Does a time-series gap represent elapsed time or rows?
- How are label end-times purged when observations are not equally spaced?

## Why this score for a trading system

3/5: useful transferable validation semantics, not a trading-specific leakage-proof cross-validator.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
