# Riskfolio-Lib: Estimate inputs before optimizing weights

**Decision question:** How much of an optimized portfolio comes from covariance choices?

| Field | Review |
| --- | --- |
| Upstream | [dcajasn/Riskfolio-Lib](https://github.com/dcajasn/Riskfolio-Lib) |
| Primary area | Portfolio & Risk |
| Source commit | [8724297f5a252755229b7284495389223af70b95](https://github.com/dcajasn/Riskfolio-Lib/commit/8724297f5a252755229b7284495389223af70b95) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/dcajasn/Riskfolio-Lib/blob/8724297f5a252755229b7284495389223af70b95/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Keeps expected-return and covariance estimation methods as explicit choices before optimization. Selecting an estimator and objective on the same short sample can create an impressive but unstable weight vector. |

## Mechanism worth inspecting

Portfolio.assets_stats exposes separate choices for expected return and covariance, including historical, EWMA, and shrinkage estimators. The optimization interface then consumes risk and constraint choices. This separation helps attribute a weight change to an estimator versus an objective.

**Source trail:** [project overview](https://github.com/dcajasn/Riskfolio-Lib/blob/8724297f5a252755229b7284495389223af70b95/README.md) · [documentation](https://github.com/dcajasn/Riskfolio-Lib/blob/8724297f5a252755229b7284495389223af70b95/README.md#L25-L45) · [implementation](https://github.com/dcajasn/Riskfolio-Lib/blob/8724297f5a252755229b7284495389223af70b95/riskfolio/src/Portfolio.py#L1156-L1197).

## Important limit

A large menu of estimators invites selection on noise. The code does not by itself provide honest out-of-sample selection, fee-aware execution, or leverage constraints appropriate to any particular exchange.

## Questions to take into your own design

- Which estimator produced each proposed weight set?
- Was that choice fixed before evaluating the portfolio?

## Why this score for a trading system

Estimator choice affects trading weights, but the large optimizer menu can amplify selection noise on short samples.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
