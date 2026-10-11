# arch: Forecast origin and target are different clocks

**Decision question:** Which date should a multi-step risk forecast be scored against?

| Field | Review |
| --- | --- |
| Upstream | [bashtage/arch](https://github.com/bashtage/arch) |
| Primary area | Portfolio & Risk |
| Source commit | [91a25ef4ab25ca5daac8317124b9c426a63d3567](https://github.com/bashtage/arch/commit/91a25ef4ab25ca5daac8317124b9c426a63d3567) |
| Reviewed | 2026-09-25 |
| Declared license | [BSD-3-Clause](https://github.com/bashtage/arch/blob/91a25ef4ab25ca5daac8317124b9c426a63d3567/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes forecast origin-versus-target alignment and analytic, simulation, and bootstrap variance methods. Using target-aligned output as if known at the target timestamp would create a timing error. |

## Mechanism worth inspecting

The forecast interface distinguishes an origin row containing future horizons from a target row aligned to realized outcomes. It also specifies when analytic forecasts are unavailable and simulation or bootstrap is required. That makes horizon alignment explicit in volatility reporting.

**Source trail:** [project overview](https://github.com/bashtage/arch/blob/91a25ef4ab25ca5daac8317124b9c426a63d3567/README.md) · [documentation](https://github.com/bashtage/arch/blob/91a25ef4ab25ca5daac8317124b9c426a63d3567/doc/source/bootstrap/timeseries-bootstraps.rst#L1-L20) · [implementation](https://github.com/bashtage/arch/blob/91a25ef4ab25ca5daac8317124b9c426a63d3567/arch/univariate/base.py#L992-L1043).

## Important limit

An aligned forecast table does not make its target-time value available at the target time. Calibration and regime stability still need out-of-sample evidence.

## Questions to take into your own design

- Does every risk forecast store the origin timestamp separately from the target timestamp?
- Are model and method changes preregistered before comparing realized risk?

## Why this score for a trading system

Origin-versus-target alignment prevents a concrete timing error in risk forecasts, but the model does not define a live trading limit.

**Scope of this review:** We read the pinned overview, the linked documentation, and the selected source paths. We did not install or run this project, validate its claimed performance, or audit every module.
