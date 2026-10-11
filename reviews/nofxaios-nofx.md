# NOFX — Keep the model outside the risk boundary

**Decision question:** Do code-enforced trading limits actually constrain an autonomous agent?

| Field | Review |
| --- | --- |
| Upstream | [NoFxAiOS/nofx](https://github.com/NoFxAiOS/nofx) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ef476f28926c7d0c03f105a19b18f91e30a652a7](https://github.com/NoFxAiOS/nofx/commit/ef476f28926c7d0c03f105a19b18f91e30a652a7) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 ([source](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The risk path arms its profit giveback close on underlying price movement rather than leverage-scaled margin PnL; it also holds a budget for planned margin. A code gate is valuable only if all order paths pass through it. |

## What this project does

A multi-venue trading terminal in which a model produces decisions and the runtime applies execution rules. [Project README](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/README.md#L68).

## Mechanism inspected

The risk path arms its profit giveback close on underlying price movement rather than leverage-scaled margin PnL; it also holds a budget for planned margin. [Implementation](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/trader/auto_trader_risk.go#L14). [Related source 1](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/docs/architecture/AGENT_MEMORY_AND_PLANNING.md#L21).

## Limitation that matters

A code gate is valuable only if all order paths pass through it. The review does not establish that every advertised stop or live safeguard is enforced across venues, and the project is a large autonomous trading stack. This is a source review, not a runtime or security test.

## Practical check for a trading system

Trace every order path to one guarded submission point and test failures after an exchange ACK.

## Why this score

Directly relevant to live risk boundaries, but the size of the agent stack and unverified venue coverage limit reuse.

## Source trail

[README](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/README.md#L68); [Implementation](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/trader/auto_trader_risk.go#L14); [Related source 1](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/docs/architecture/AGENT_MEMORY_AND_PLANNING.md#L21) - [License](https://github.com/NoFxAiOS/nofx/blob/ef476f28926c7d0c03f105a19b18f91e30a652a7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
