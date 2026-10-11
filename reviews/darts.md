# Darts: historical forecasts depend on the retraining policy

**Decision question:** Was a forecast model actually available at each replayed date?

| Field | Review |
| --- | --- |
| Upstream | [Darts](https://github.com/unit8co/darts) |
| Primary area | Signals & Models |
| Source commit | [10b314927024f5bb0b8f004bc6bd7cb48b32783e](https://github.com/unit8co/darts/commit/10b314927024f5bb0b8f004bc6bd7cb48b32783e) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/unit8co/darts/blob/10b314927024f5bb0b8f004bc6bd7cb48b32783e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Historical-forecast evaluation can retrain at every origin or reuse a pre-trained global model, with explicit window, stride, and horizon settings. That distinction is valuable; future covariates still need independent evidence that their values were known at each origin. |

## Project overview

Time-series forecasting and anomaly detection library with a common fit/predict interface across statistical and neural models. Supports historical evaluation, ensembles, and external covariates for model comparison.

[Project documentation](https://github.com/unit8co/darts/blob/10b314927024f5bb0b8f004bc6bd7cb48b32783e/README.md#L17-L30).

## Mechanism worth inspecting

The [overview](https://github.com/unit8co/darts/blob/10b314927024f5bb0b8f004bc6bd7cb48b32783e/README.md#L182-L210) distinguishes past and future covariates and historical backtesting. The [historical_forecasts signature and guide](https://github.com/unit8co/darts/blob/10b314927024f5bb0b8f004bc6bd7cb48b32783e/darts/models/forecasting/forecasting_model.py#L672-L729) expose train length, start, stride, retraining, and pre-trained mode. Retraining mode rebuilds a training window at each origin; pre-trained mode skips that step. The same returned forecast series could therefore have very different causal meaning.

## Important limit

A future-covariate label in an API does not prove the value was published before a past decision. This review did not inspect every model, and retrospective use of a modern pre-trained model would not represent what existed historically without a version cutoff.

## Questions to take into your own design

- For each forecast origin, which model version and training cutoff were available?
- Are covariate publication times recorded rather than inferred from their event dates?

## Why this score for a trading system

Its explicit replay and retraining controls help evaluate time-series models causally, while data publication and model-version provenance remain external.

**Scope of this review:** We read the pinned README and historical-forecast method documentation and source. We did not train or backtest a model.
