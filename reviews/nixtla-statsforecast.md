# StatsForecast — a fallback changes the experiment

**Decision question:** Can a rolling evaluation silently switch the model that produced a forecast?

| Field | Review |
| --- | --- |
| Upstream | [StatsForecast](https://github.com/Nixtla/statsforecast) |
| Primary area | Research & Reproducibility |
| Source commit | [99f2408c20b9f0bd44d5e43f303b784f7851f900](https://github.com/Nixtla/statsforecast/commit/99f2408c20b9f0bd44d5e43f303b784f7851f900) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/Nixtla/statsforecast/blob/99f2408c20b9f0bd44d5e43f303b784f7851f900/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its rolling evaluator exposes refit and fallback paths. Record the effective model for each forecast: a successful fallback is useful operationally but changes what a model comparison is measuring. |

## Project overview

StatsForecast offers statistical forecasting models and rolling cross-validation with optional fallback models. [Project documentation](https://github.com/Nixtla/statsforecast/blob/99f2408c20b9f0bd44d5e43f303b784f7851f900/README.md#L10-L21).

## Mechanism worth inspecting

Cross-validation iterates over cutoffs, separates train and test slices and supports a refit policy. If fitting or forecasting raises and a fallback is configured, the fallback produces the result instead. [Cutoff/refit path](https://github.com/Nixtla/statsforecast/blob/99f2408c20b9f0bd44d5e43f303b784f7851f900/python/statsforecast/core.py#L290-L330); [fallback branch](https://github.com/Nixtla/statsforecast/blob/99f2408c20b9f0bd44d5e43f303b784f7851f900/python/statsforecast/core.py#L331-L345).

## Important limit

A model-named aggregate can conceal different effective forecasting paths unless fallback identity is recorded. Future exogenous values are drawn from the test slice and must genuinely be knowable at forecast time. A rolling cutoff alone proves neither assumption. [Future exogenous slice](https://github.com/Nixtla/statsforecast/blob/99f2408c20b9f0bd44d5e43f303b784f7851f900/python/statsforecast/core.py#L290-L301).

## Questions to take into your own design

- Does each forecast record the effective model, refit cutoff and fallback reason?
- Are future exogenous values versioned and known before forecast issuance?

## Why this score for a trading system

3/5: a useful experiment-provenance pattern, requiring trading-specific exogenous timing and costs rather than adoption of a forecasting stack.

**Scope of this review:** Rolling evaluation and fallback control flow; reported forecasting accuracy was not replicated.
