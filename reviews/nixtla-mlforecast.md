# MLForecast — endpoint equality is not full feature constancy

**Decision question:** What evidence supports declaring a feature static across a series?

| Field | Review |
| --- | --- |
| Upstream | [MLForecast](https://github.com/Nixtla/mlforecast) |
| Primary area | Signals & Models |
| Source commit | [dc594bf6c8aa54bb446ec5fdefc09f90f6aaa706](https://github.com/Nixtla/mlforecast/commit/dc594bf6c8aa54bb446ec5fdefc09f90f6aaa706) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/Nixtla/mlforecast/blob/dc594bf6c8aa54bb446ec5fdefc09f90f6aaa706/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | A useful static-feature contract with a visible boundary: the inspected check compares first and last values. Full-history constancy and time-varying instrument metadata need a stronger application check. |

## Project overview

MLForecast builds time-series forecasting features for machine-learning models, with explicit static and dynamic feature roles. [Project documentation](https://github.com/Nixtla/mlforecast/blob/dc594bf6c8aa54bb446ec5fdefc09f90f6aaa706/README.md#L18-L20).

## Mechanism worth inspecting

If static features are unspecified, the inspected path infers them from columns outside the time, target and partition roles. It compares static values at each series' first and last rows and stores end values. [Inference and check](https://github.com/Nixtla/mlforecast/blob/dc594bf6c8aa54bb446ec5fdefc09f90f6aaa706/mlforecast/core.py#L850-L889).

## Important limit

Equality at the endpoints does not establish that every intermediate value was constant. A value can change and later return to its original value. The inspected check is a useful guard, but a stronger application contract needs all-row constancy or an explicit dynamic role.

## Questions to take into your own design

- Could an instrument attribute change inside the history and return before the final row?
- Are time-varying exchange rules and metadata explicitly treated as dynamic vintages?

## Why this score for a trading system

2/5: a specific schema-validation boundary, with limited reason to adopt another forecasting framework merely to implement full-series constancy checks.

**Scope of this review:** Static-feature inference and endpoint validation; forecast algorithms and all preprocessing paths were not audited.
