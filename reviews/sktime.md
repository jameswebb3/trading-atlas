# sktime: Keep forecast horizon and model update explicit

**Decision question:** Which observations were known when a forecast was made?

| Field | Review |
| --- | --- |
| Upstream | [sktime/sktime](https://github.com/sktime/sktime) |
| Primary area | Signals & Models |
| Source commit | [20982d73c7b9c5681b64bd343db0b5cd4af7a64a](https://github.com/sktime/sktime/commit/20982d73c7b9c5681b64bd343db0b5cd4af7a64a) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/sktime/sktime/blob/20982d73c7b9c5681b64bd343db0b5cd4af7a64a/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Requires a fitted forecaster and explicit forecast horizon; update is a separate state transition. The default update fallback can refit on all observed data, so replay must control exactly when update becomes available. |

## Mechanism worth inspecting

The base forecaster checks fitted state, validates exogenous X, and resolves the forecast horizon before prediction. Its update API advances the cutoff and may refit parameters on observations received so far. The separation is a useful contract for online signal generation.

**Source trail:** [project overview](https://github.com/sktime/sktime/blob/20982d73c7b9c5681b64bd343db0b5cd4af7a64a/README.md) · [documentation](https://github.com/sktime/sktime/blob/20982d73c7b9c5681b64bd343db0b5cd4af7a64a/docs/source/api_reference/forecasting.rst#L1-L30) · [implementation](https://github.com/sktime/sktime/blob/20982d73c7b9c5681b64bd343db0b5cd4af7a64a/sktime/forecasting/base/_base.py#L540-L592) · [additional source](https://github.com/sktime/sktime/blob/20982d73c7b9c5681b64bd343db0b5cd4af7a64a/sktime/forecasting/base/_base.py#L1297-L1317).

## Important limit

The API cannot tell whether an observation was published late or corrected after the fact. A trading implementation still needs available_at on every input and a recorded update schedule.

## Questions to take into your own design

- Does the forecast receipt contain cutoff, horizon, and model state version?
- Can a late observation change a past forecast during replay?

## Why this score for a trading system

Forecast cutoff and update state transfer to trading signals, but publication delays remain outside the forecaster contract.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
