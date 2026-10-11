# AI Hedge Fund Crypto: separate an LLM's risk instructions from enforced limits

**Decision question:** Is a position limit checked by code or merely supplied to the decision prompt?

| Field | Review |
| --- | --- |
| Upstream | [AI Hedge Fund Crypto](https://github.com/51bitquant/ai-hedge-fund-crypto) |
| Primary area | Agents & Decision Systems |
| Source commit | [c6750e0041cb2e528856864783585427c45cc34d](https://github.com/51bitquant/ai-hedge-fund-crypto/commit/c6750e0041cb2e528856864783585427c45cc34d) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Separates strategy, risk, and portfolio-decision nodes, making the LLM decision path inspectable. The reviewed risk node values positions at cost basis, while the decision function returns parsed model output without a local quantity-limit check; useful chiefly as a review case. |

## Mechanism worth inspecting

The [architecture](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/README.md#L95-L104) describes separate data, strategy, risk, and decision stages, with a [custom-node guide](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/README.md#L342-L381). The [risk node](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/src/graph/risk_management_node.py#L26-L55) calculates a per-position budget using cash and stored cost basis. The [portfolio node](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/src/graph/portfolio_management_node.py#L29-L38) translates this budget into maximum quantity; its [decision function](https://github.com/51bitquant/ai-hedge-fund-crypto/blob/c6750e0041cb2e528856864783585427c45cc34d/src/graph/portfolio_management_node.py#L149-L184) requests JSON, invokes the LLM/parser chain, and returns the result. These boundaries help locate where an independent enforcement layer belongs.

## Important limit

The inspected decision function contains no post-parse comparison with the calculated maximum quantity. This is a finding about that function, not proof that every downstream path lacks checks. Cost basis is also different from current marked exposure, even though current prices are collected. The README's return charts were not independently replicated and do not establish profitability.

## Questions to take into your own design

- Does deterministic code validate action, sign, quantity, current exposure, and aggregate budget after model output?
- Are risk calculations based on current marks and instrument economics rather than acquisition cost alone?

## Why this score for a trading system

2/5: directly themed around crypto decisions, but the inspected risk and LLM boundaries offer cautionary examples rather than a convincing capital-protection mechanism. No return or live-readiness claim is validated.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
