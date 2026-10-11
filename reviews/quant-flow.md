# Quant Flow: a failed query must remain unknown

**Decision question:** What should an order monitor do when open-order or position queries fail?

| Field | Review |
| --- | --- |
| Upstream | [web3spreads/quant-flow](https://github.com/web3spreads/quant-flow) |
| Primary area | Execution & Exchange Integration |
| Source commit | [3f05254f066f32af0c90b94fbbe6db2e87f3f518](https://github.com/web3spreads/quant-flow/commit/3f05254f066f32af0c90b94fbbe6db2e87f3f518) |
| Reviewed | 2026-09-25 |
| Declared license | No license file found at the reviewed commit; [repository tree](https://github.com/web3spreads/quant-flow/tree/3f05254f066f32af0c90b94fbbe6db2e87f3f518) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Quant Flow skips order decisions when open-order or position queries fail, preserving an unknown state. The same path removes a watched order after a local timeout, and no license file was found at the reviewed commit. |

## Mechanism worth inspecting

The [architecture document](https://github.com/web3spreads/quant-flow/blob/3f05254f066f32af0c90b94fbbe6db2e87f3f518/docs/architecture.md#L7-L21) separates decision, trading, and protection components. In the order monitor, a failed open-order request returns `None`; the [code skips that cycle](https://github.com/web3spreads/quant-flow/blob/3f05254f066f32af0c90b94fbbe6db2e87f3f518/src/trading/order_manager.py#L153-L162) instead of equating the failure with an empty order list. A failed position query similarly [postpones removal or protective-order decisions](https://github.com/web3spreads/quant-flow/blob/3f05254f066f32af0c90b94fbbe6db2e87f3f518/src/trading/order_manager.py#L188-L196). This is a useful three-way distinction: found, absent with authoritative evidence, and unknown because the query failed.

## Important limits

The same monitor [removes a watched order after a local time limit](https://github.com/web3spreads/quant-flow/blob/3f05254f066f32af0c90b94fbbe6db2e87f3f518/src/trading/order_manager.py#L167-L181). The inspected branch does not first establish that the exchange order has reached a terminal state. Its later inference from position direction is also not an exact per-order fill record. The README describes an LLM-assisted trading system; this review covers only the deterministic order-monitor path, not strategy quality.

The absence of a visible license file at the pinned commit makes code reuse inappropriate without further clarification. The behavior can still inform an independently written state contract.

## Why this score for a trading system

Unknown-versus-empty order state is directly useful, while timeout removal and absent licensing sharply limit this as a trading reference.

**Scope of this review:** We read the pinned README, architecture document, and order monitor. We did not run Quant Flow or inspect every protective-order path.
