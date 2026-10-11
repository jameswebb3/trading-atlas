# Cvxportfolio — Does a backtest report the requested portfolio or the trades it could execute

**Decision question:** Does a backtest report the requested portfolio or the trades it could execute?

| Field | Review |
| --- | --- |
| Upstream | [Cvxportfolio](https://github.com/cvxgrp/cvxportfolio) |
| Primary area | Backtesting & Simulation |
| Source commit | [351c782b9b8b395c1a5f886b77e0d55f1bc9396e](https://github.com/cvxgrp/cvxportfolio/commit/351c782b9b8b395c1a5f886b77e0d55f1bc9396e) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0-or-later](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A strong portfolio-simulation reference that preserves the gap between intended weights and executable trades. Liquidity caps, rounding and cash are explicit; order-book fills and derivatives accounting require a different execution model. |

## Project overview

Cvxportfolio combines portfolio policies, transaction-cost models and market simulation. Its simulator exposes the difference between target and feasible trades. [Project documentation](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/docs/simulator.rst#L19-L43).

## Mechanism worth inspecting

The policy sees past returns and volumes; simulation then cancels zero-volume trades, caps participation, rounds quantities and recomputes cash. A liquidity-cap test checks that requested trades exceed realized trades. [Simulation](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/cvxportfolio/simulator.py#L270-L334), [test read](https://github.com/cvxgrp/cvxportfolio/blob/351c782b9b8b395c1a5f886b77e0d55f1bc9396e/cvxportfolio/tests/test_simulator.py#L1067-L1087).

## Important limit

Current-period volume is used as an ex-post simulation input, not a quantity known to the policy at its decision time. Aggregate volume caps do not model queue position or perpetual margin mechanics.

## Questions to take into your own design

- Does a backtest report the requested portfolio or the trades it could execute?
- Are target weights, capped trades, cash changes and realized holdings retained separately?

## Why this score for a trading system

4/5: direct, tested distinction between proposed and realized trades. Aggregate stock-style liquidity assumptions limit the model's transfer to other venues.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
