# StochVolModels - When is a numerical option calibration result safe to accept?

**Decision question:** When is a numerical option calibration result safe to accept?

| Field | Review |
| --- | --- |
| Upstream | [ArturSepp/StochVolModels](https://github.com/ArturSepp/StochVolModels) |
| Primary area | Signals Models |
| Source commit | [6aa6dfdd8fa50d36a74305820d97f214a1d29389](https://github.com/ArturSepp/StochVolModels/commit/6aa6dfdd8fa50d36a74305820d97f214a1d29389) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Checks optimizer success, parameter shape, finiteness and bounds before accepting a calibrated vector; test code verifies constraints and weighted objective wiring. Those checks certify numerical admissibility of the returned vector, not predictive value, stability across dates or executable trading edge. |

## What this project does

A research library for European-option pricing under stochastic-volatility models, with transform pricing, simulation and constrained calibration interfaces.

## Mechanism inspected

validate_optimization_result rejects unsuccessful optimizers, missing or nonnumeric parameters, wrong vector size, nonfinite values and bound violations. The model interface separates analytic chain pricing from Monte Carlo pricing. A source test replaces the optimizer and inspects the weighted objective, Feller constraint, method and parameter bounds used by Heston calibration.

## Limitation that matters

A numerically valid in-bounds parameter vector can still fit a noisy or wrong quote surface, change sharply next day, or produce no trading benefit. The provided contract test checks function wiring with a fake optimizer, not market calibration performance. Using options as a signal for perpetuals would require a separate causal data feed and validation.

## Practical check for a trading system

Keep numerical acceptance separate from economic acceptance: optimizer status, finite/bounded parameters, residual quality, stability and out-of-sample decision gain should have independent gates.

## Why this score

3/5 because its explicit optimizer-result guard and constraint tests are a transferable model-risk pattern, but the option model and data are outside a perp-only execution path.

## Source trail

[README](https://github.com/ArturSepp/StochVolModels/blob/6aa6dfdd8fa50d36a74305820d97f214a1d29389/README.md#L205); [Calibration result guard](https://github.com/ArturSepp/StochVolModels/blob/6aa6dfdd8fa50d36a74305820d97f214a1d29389/src/stochvolmodels/pricers/model_pricer.py#L44); [Heston constraint test](https://github.com/ArturSepp/StochVolModels/blob/6aa6dfdd8fa50d36a74305820d97f214a1d29389/src/stochvolmodels/tests/test_model_calibration_contracts.py#L220); [License](https://github.com/ArturSepp/StochVolModels/blob/6aa6dfdd8fa50d36a74305820d97f214a1d29389/LICENSE.txt#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
