# bt: account for nonlinear costs without making unknown liquidity free

**Decision question:** What happens to a size-aware cost model when volume is zero or unavailable?

| Field | Review |
| --- | --- |
| Upstream | [bt](https://github.com/pmorissette/bt) |
| Primary area | Backtesting & Simulation |
| Source commit | [002c3c071a462168199e4d62312297201819085e](https://github.com/pmorissette/bt/commit/002c3c071a462168199e4d62312297201819085e) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Builds portfolio backtests from composable selection, weighting, and rebalance steps. Its cost-model interface accepts volume and volatility, but both supplied nonlinear models return zero cost when volume is nonpositive. |

## Project overview

A portfolio backtesting framework combines reusable algorithms into nested strategies and tracks positions, cash, and performance. [Project documentation](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/README.md#L10-L45).

## Mechanism worth inspecting

The [cost-model guide](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/docs/source/Cost_Models.md#L3-L35) distinguishes a quantity/price commission hook from models using volume and volatility. The [model interface](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/bt/core.py#L2216-L2232) makes those inputs explicit. Its [cash-outlay solver](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/bt/core.py#L1617-L1709) adjusts quantity for commissions and raises on nonconvergence, rather than silently exceeding the requested cash allocation.

## Important limit

The [square-root model](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/bt/core.py#L2257-L2262) and [Almgren-Chriss model](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/bt/core.py#L2296-L2302) return zero when volume is nonpositive. That is unsuitable as a default interpretation of missing liquidity. The [documentation](https://github.com/pmorissette/bt/blob/002c3c071a462168199e4d62312297201819085e/docs/source/Cost_Models.md#L19-L35) also uses calibrated assumptions from an equity-oriented example; these are not portable venue facts.

## Questions to take into your own design

- Can an invalid volume input cause a large simulated trade to become free?
- Does a cost-aware rebalance preserve cash constraints and expose solver failure?

## Why this score for a trading system

3/5: useful size-aware cost and cash-allocation mechanisms, limited by zero-cost defaults and invalid-volume behavior requiring explicit policy.

**Scope of this review:** README, nonlinear-cost guide, cost-model implementations, and commission-aware cash allocation; no reported example returns replicated.
