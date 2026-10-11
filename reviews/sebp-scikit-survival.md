# scikit-survival — How can incomplete event observation distort a duration model's evaluation

**Decision question:** How can incomplete event observation distort a duration model's evaluation?

| Field | Review |
| --- | --- |
| Upstream | [scikit-survival](https://github.com/sebp/scikit-survival) |
| Primary area | Research & Reproducibility |
| Source commit | [6716d307184dd581e40f537f1f7d094b1b4b77be](https://github.com/sebp/scikit-survival/commit/6716d307184dd581e40f537f1f7d094b1b4b77be) |
| Reviewed | 2026-09-27 |
| Declared license | [GPL-3.0](https://github.com/sebp/scikit-survival/blob/6716d307184dd581e40f537f1f7d094b1b4b77be/COPYING) |
| Review depth | 3/3: documentation, implementation and relevant boundary tests read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Offers a disciplined treatment of right-censored outcomes and unsupported evaluation horizons. Potentially useful for execution-duration research, but it requires an explicit censoring model and complete observation evidence. |

## Project overview

A scikit-learn-compatible survival-analysis library for modelling time to events when some outcomes are censored. [Project documentation](https://github.com/sebp/scikit-survival/blob/6716d307184dd581e40f537f1f7d094b1b4b77be/README.rst#L15-L31).

## Mechanism worth inspecting

The IPCW concordance implementation estimates the censoring distribution from training outcomes, applies a fixed evaluation horizon when supplied and weights evaluable test outcomes. Tests cover horizons outside training support and a zero censoring-survival probability. [Estimator path](https://github.com/sebp/scikit-survival/blob/6716d307184dd581e40f537f1f7d094b1b4b77be/sksurv/metrics.py#L228-L278), [weight construction](https://github.com/sebp/scikit-survival/blob/6716d307184dd581e40f537f1f7d094b1b4b77be/sksurv/metrics.py#L318-L338); [boundary tests](https://github.com/sebp/scikit-survival/blob/6716d307184dd581e40f537f1f7d094b1b4b77be/tests/test_metrics.py#L378-L428).

## Important limit

Censoring assumptions and training support must fit the actual observation process. A missing fill event or broken collector cannot automatically be reclassified as a valid censored observation. The tests were read, not run.

## Questions to take into your own design

- Is the observation end known, or is the outcome missing because collection failed?
- Was the censoring model and evaluation horizon fixed using training data?

## Why this score for a trading system

2/5: statistically useful for a specialised duration study, with an indirect connection to the typical trading pipeline.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
