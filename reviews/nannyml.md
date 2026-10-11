# NannyML: a monitoring estimate has conditions, not ground truth

**Decision question:** Can estimated model performance replace delayed ground-truth outcomes?

| Field | Review |
| --- | --- |
| Upstream | [NannyML/nannyml](https://github.com/NannyML/nannyml) |
| Primary area | Operations & Observability |
| Source commit | [4c86ee350dc541cb244f965cf555b4b2a004ae99](https://github.com/NannyML/nannyml/commit/4c86ee350dc541cb244f965cf555b4b2a004ae99) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Fits a confidence-based estimator on labeled reference data and reports estimated metrics by chunks when recent labels are unavailable. Its own documentation requires calibrated probabilities and no concept drift; a regime change can invalidate the proxy precisely when monitoring matters most. |

## Mechanism worth inspecting

The [README](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/README.md#L43-L48) presents performance estimation without recent targets. The [technical explanation](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/docs/how_it_works/performance_estimation.rst#L24-L43) derives estimated classification metrics from calibrated prediction probabilities. In code, [`_fit`](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/nannyml/performance_estimation/confidence_based/cbpe.py#L316-L337) needs labeled reference data; [`_estimate`](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/nannyml/performance_estimation/confidence_based/cbpe.py#L339-L399) generates chunk-level estimates from recent data.

## Important limit

The [documented assumptions](https://github.com/NannyML/nannyml/blob/4c86ee350dc541cb244f965cf555b4b2a004ae99/docs/how_it_works/performance_estimation.rst#L235-L291) include calibrated probabilities, no concept drift, no shift to unseen feature regions, and adequate sample size. A proxy can signal what to inspect, but cannot certify realized trading PnL or replace observed outcomes.

## Questions to take into your own design

- Are probabilities calibrated on a reference period relevant to the current regime?
- Is the estimate labeled as proxy and later reconciled against outcomes?
- What happens when coverage or sample size is too small?

## Why this score for a trading system

Confidence-based proxy monitoring may inform model watchlists, but its calibration and no-drift assumptions are too indirect for trading decisions.

**Scope of this review:** We read the pinned README, technical documentation, and CBPE fit/estimate paths. We did not fit a model, validate calibration, or test trading data.
