# Open Source Asset Pricing — Identifier validity is not information availability

**Decision question:** Can a valid security link still create a timing error?

| Field | Review |
| --- | --- |
| Upstream | [Open Source Asset Pricing](https://github.com/OpenSourceAP/CrossSection) |
| Primary area | Signals & Models |
| Source commit | [8db892442c2c3a3779b0f1eac4370d3655be15a1](https://github.com/OpenSourceAP/CrossSection/commit/8db892442c2c3a3779b0f1eac4370d3655be15a1) |
| Reviewed | 2026-09-27 |
| Declared license | [GPL-2.0](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | SignalMasterTable joins monthly stock keys and applies validity intervals and ranking to optional OptionMetrics links. A date-valid identifier mapping does not establish when a characteristic was published. |

## Project overview

Research code for reconstructing stock-level characteristics and portfolio implementations from asset-pricing studies. [Documentation](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/README.md).

## Mechanism worth inspecting

SignalMasterTable joins monthly stock keys and applies validity intervals and ranking to optional OptionMetrics links. Missing optional providers are represented explicitly. [Source](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/Signals/pyCode/SignalMasterTable.py#L53-L59).

## Important limit

A date-valid identifier mapping does not establish when a characteristic was published. The inspected master-table code is not proof that every predictor uses point-in-time inputs; much of its source data requires licensed access. [Evidence 1](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/Signals/pyCode/SignalMasterTable.py#L53-L59). [Evidence 2](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/Signals/pyCode/SignalMasterTable.py#L103-L154). [Evidence 3](https://github.com/OpenSourceAP/CrossSection/blob/8db892442c2c3a3779b0f1eac4370d3655be15a1/README.md#L25-L36).

## Questions to take into your own design

- Are identifier validity and value availability separate contracts?
- Does missing licensed input stay missing rather than changing the population silently?

## Why this score for a trading system

Directly relevant signal-construction evidence, with equity-specific and data-access limits; no claim that published equity predictors transfer to crypto.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
