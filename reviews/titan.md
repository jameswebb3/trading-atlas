# Titan: a replaced order must survive the old order's late terminal event

**Decision question:** Can a late terminal update for a replaced order close its successor?

| Field | Review |
| --- | --- |
| Upstream | [dominolu/titan](https://github.com/dominolu/titan) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fa6a1535f02839fc5a1978aa7bca2f5feee98079](https://github.com/dominolu/titan/commit/fa6a1535f02839fc5a1978aa7bca2f5feee98079) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/dominolu/titan/blob/fa6a1535f02839fc5a1978aa7bca2f5feee98079/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Titan ignores a terminal update for an old exchange order ID after a replacement opens under the same client ID. The state transition is explicit in code, but this review did not verify it against live event traces. |

## Mechanism worth inspecting

Titan's [runtime overview](https://github.com/dominolu/titan/blob/fa6a1535f02839fc5a1978aa7bca2f5feee98079/README.md#L5-L20) separates event and execution components. The Hyperliquid order manager documents a specific event-order problem: a modification can cancel an old exchange order and open a new one while retaining the client order ID. Its [update branch](https://github.com/dominolu/titan/blob/fa6a1535f02839fc5a1978aa7bca2f5feee98079/connector/src/hyperliquid/ordermanager.rs#L102-L113) ignores a late terminal event whose exchange order ID differs from the current one. It then derives [incremental executed quantity from cumulative fill state](https://github.com/dominolu/titan/blob/fa6a1535f02839fc5a1978aa7bca2f5feee98079/connector/src/hyperliquid/ordermanager.rs#L121-L144) and gates updates by exchange timestamp.

This is a sharper identity model than one map keyed only by client order ID. It separates the intent's persistent identity from each venue order instance.

## Boundary and practical use

The [event-engine design](https://github.com/dominolu/titan/blob/fa6a1535f02839fc5a1978aa7bca2f5feee98079/docs/event_engine_technical_design.md#L1-L24) still lists some cross-component work as pending. We did not inspect tests for this exact permutation or verify it with live traces. A builder can nonetheless turn the observed branch into a focused fixture: open old ID, modify to new ID, receive old terminal late, keep the new order open, and avoid double-counting fills.

## Why this score for a trading system

Guarding an order replacement against a delayed old terminal event is directly relevant, though the path was not validated against venue traces.

**Scope of this review:** We read the pinned README, design document, and Hyperliquid order manager. We did not run Titan or inspect its full event engine.
