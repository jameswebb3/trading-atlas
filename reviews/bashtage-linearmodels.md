# linearmodels — panel rows can share two sources of dependence

**Decision question:** Do significance estimates account for dependence within both dates and instruments?

| Field | Review |
| --- | --- |
| Upstream | [linearmodels](https://github.com/bashtage/linearmodels) |
| Primary area | Research & Reproducibility |
| Source commit | [ec0f288906af00e1bada43b5a802a0c7a746c292](https://github.com/bashtage/linearmodels/commit/ec0f288906af00e1bada43b5a802a0c7a746c292) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/bashtage/linearmodels/blob/ec0f288906af00e1bada43b5a802a0c7a746c292/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its two-way covariance makes date and instrument dependence explicit. A useful sensitivity reference for panel research, provided cluster counts and the sampling assumptions are reported alongside significance. |

## Project overview

linearmodels supplies panel, instrumental-variable and other linear estimators with specialized covariance calculations. [Project documentation](https://github.com/bashtage/linearmodels/blob/ec0f288906af00e1bada43b5a802a0c7a746c292/README.md#L11-L21).

## Mechanism worth inspecting

Two-way clustered covariance combines the covariance for each cluster axis and subtracts the covariance of their intersection. The implementation exposes this calculation rather than treating every panel row as independent. [Cluster construction](https://github.com/bashtage/linearmodels/blob/ec0f288906af00e1bada43b5a802a0c7a746c292/linearmodels/panel/covariance.py#L314-L328); [inclusion/exclusion](https://github.com/bashtage/linearmodels/blob/ec0f288906af00e1bada43b5a802a0c7a746c292/linearmodels/panel/covariance.py#L330-L339).

## Important limit

Cluster labels, the number of independent clusters and the regression design still determine whether inference is defensible. Two-way clustering does not establish causation, handle every serial dependence pattern or correct a research campaign's selection bias.

## Questions to take into your own design

- Do cross-sectional tests report independent dates as well as instrument-row counts?
- How sensitive is the conclusion to date clusters, instrument clusters and the existing block-based estimator?

## Why this score for a trading system

3/5: a precise panel-dependence reference, requiring a justified sampling design and sufficient cluster counts in financial data.

**Scope of this review:** Two-way clustered covariance construction; no regression replication or estimator-wide audit.
