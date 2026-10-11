# FinRL: an RL environment encodes a specific market, not trading in general

**Decision question:** Which exchange assumptions are hidden inside a trading agent's reward?

| Field | Review |
| --- | --- |
| Upstream | [FinRL](https://github.com/AI4Finance-Foundation/FinRL) |
| Primary area | Signals & Models |
| Source commit | [3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c](https://github.com/AI4Finance-Foundation/FinRL/commit/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/AI4Finance-Foundation/FinRL/blob/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Its classic stock environment charges buy/sell costs, limits share sales to holdings, and can force liquidation under a turbulence threshold. These are explicit assumptions for equities, not a model of perpetual margin, funding, order acknowledgements, or Hyperliquid fills. |

## Mechanism worth inspecting

The [project overview](https://github.com/AI4Finance-Foundation/FinRL/blob/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c/README.md#L26-L57) distinguishes the classic FinRL stack from its newer production-oriented project. The [environment notes](https://github.com/AI4Finance-Foundation/FinRL/blob/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c/docs/source/finrl_meta/Environment_layer.rst#L8-L20) state transaction-cost and risk-aversion assumptions. In the [stock trading environment](https://github.com/AI4Finance-Foundation/FinRL/blob/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c/finrl/meta/env_stock_trading/env_stocktrading.py#L113-L164), sells are capped by held shares and charged a configured percentage; [the step path](https://github.com/AI4Finance-Foundation/FinRL/blob/3a0ab5cf3ddf0b59d25f7fd7e435811a18838c6c/finrl/meta/env_stock_trading/env_stocktrading.py#L313-L335) converts actions to integer shares and orders sells before buys.

## Important limit

The code inspected is for shares. It does not expose funding settlements, liquidation mechanics, exchange order lifecycle, or live execution delays. Reported RL returns from this environment cannot be generalized to a perp venue.

## Questions to take into your own design

- Are reward, costs, and action constraints written down for the actual instrument?
- Can a policy exploit fill or liquidation behavior that exists only in simulation?

## Why this score for a trading system

The environment is a useful example of making action and cost rules explicit, but its stock mechanics are materially different from perpetual futures.

**Scope of this review:** We read the pinned README, environment notes, and selected stock-environment code. We did not train an agent.
