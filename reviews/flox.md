# FLOX: IOC cancellation and queue position are separate fill rules

**Decision question:** What must a simulator do with a non-crossing IOC and a passive queue position?

| Field | Review |
| --- | --- |
| Upstream | [FLOX-Foundation/flox](https://github.com/FLOX-Foundation/flox) |
| Primary area | Backtesting & Simulation |
| Source commit | [9dfacea4f558bb25a02f2023d0df5b1bf1ecc490](https://github.com/FLOX-Foundation/flox/commit/9dfacea4f558bb25a02f2023d0df5b1bf1ecc490) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/FLOX-Foundation/flox/blob/9dfacea4f558bb25a02f2023d0df5b1bf1ecc490/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Cancels a non-crossing IOC and tracks visible quantity ahead of a passive limit order in its simulated executor. Its bar-based queue model is an approximation; it does not establish a venue's actual order priority or fill probability. |

## Mechanism worth inspecting

The [fill-model guide](https://github.com/FLOX-Foundation/flox/blob/9dfacea4f558bb25a02f2023d0df5b1bf1ecc490/docs/how-to/backtest-realistic-fills.md#L1-L19) states separate rules for next-bar submission, taker book walking, triggered stops, and resting orders. In the [simulated executor](https://github.com/FLOX-Foundation/flox/blob/9dfacea4f558bb25a02f2023d0df5b1bf1ecc490/src/backtest/simulated_executor.cpp#L711-L764), a limit IOC that does not cross is canceled, while a passive order may enter a queue tracker seeded with visible quantity at its price. A crossing order is treated as an aggressor. The [cancel-all path](https://github.com/FLOX-Foundation/flox/blob/9dfacea4f558bb25a02f2023d0df5b1bf1ecc490/src/backtest/simulated_executor.cpp#L883-L928) detaches orders before emitting callbacks, limiting reentrancy problems.

## Important limit

The guide explicitly describes a queue model that fills on bars. Visible quantity at submission is not a complete exchange queue, and the inspected code does not prove that modeled fills match a live venue. The event rules are valuable as adversarial simulator cases, not as a claim of execution realism for every market.

## Questions to take into your own design

- Does non-crossing IOC cancel without resting?
- Is a passive fill tied to a stated queue assumption and future market evidence?
- Can a cancel callback mutate the set being canceled?

## Why this score for a trading system

IOC cancellation and passive-queue assumptions are direct fill-model questions; its bar-driven queue remains an approximation.

**Scope of this review:** We read the pinned README, fill-model guide, and selected executor branches. We did not run FLOX, compare modeled fills with exchange records, or inspect every binding.
