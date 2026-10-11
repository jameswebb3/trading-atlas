# NeuralForecast — a future-feature role is a declaration

**Decision question:** Does a future exogenous column actually exist before a forecast is issued?

| Field | Review |
| --- | --- |
| Upstream | [NeuralForecast](https://github.com/Nixtla/neuralforecast) |
| Primary area | Signals & Models |
| Source commit | [556d35f78bd67600ffda10bbecd10e71f78515e5](https://github.com/Nixtla/neuralforecast/commit/556d35f78bd67600ffda10bbecd10e71f78515e5) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/Nixtla/neuralforecast/blob/556d35f78bd67600ffda10bbecd10e71f78515e5/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its exogenous channels make input roles explicit. A column declared as future-known still needs independent availability evidence; structural validation alone cannot prevent late-published trading inputs. |

## Project overview

NeuralForecast offers neural forecasting models with historical, future and static exogenous feature channels. [Project documentation](https://github.com/Nixtla/neuralforecast/blob/556d35f78bd67600ffda10bbecd10e71f78515e5/README.md#L21-L21).

## Mechanism worth inspecting

The base model separates historical, future and static exogenous lists, and `_check_exog` rejects columns absent from the corresponding temporal or static inputs. Categorical features must also belong to a declared channel. [Presence checks](https://github.com/Nixtla/neuralforecast/blob/556d35f78bd67600ffda10bbecd10e71f78515e5/neuralforecast/common/_base_model.py#L546-L566); [categorical role checks](https://github.com/Nixtla/neuralforecast/blob/556d35f78bd67600ffda10bbecd10e71f78515e5/neuralforecast/common/_base_model.py#L568-L579).

## Important limit

Column presence is not evidence of publication-time availability. Scheduled calendar values may be known ahead; future prices, revised metrics and observed funding are different. The inspected checks validate structural roles, not the point-in-time provenance of every value.

## Questions to take into your own design

- What source and timestamp prove each future exogenous value was known at issuance?
- Can a present but late-published column fail the feature contract before training starts?

## Why this score for a trading system

2/5: a useful distinction between feature roles and availability evidence; the large modeling stack adds no established trading advantage in this review.

**Scope of this review:** Base-model exogenous schema checks; architecture performance and normalization paths were not evaluated.
