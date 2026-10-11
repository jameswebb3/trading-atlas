# Fractal DeFi — Action atomicity is not step atomicity

**Decision question:** Can a failed multi-action strategy step leave a partial portfolio change?

| Field | Review |
| --- | --- |
| Upstream | [Logarithm-Labs/fractal-defi](https://github.com/Logarithm-Labs/fractal-defi) |
| Primary area | Execution & Exchange Integration |
| Source commit | [081f33f746f9f4fc43d0726f30c613ba660e989b](https://github.com/Logarithm-Labs/fractal-defi/commit/081f33f746f9f4fc43d0726f30c613ba660e989b) |
| Reviewed | 2026-10-10 |
| Declared license | BSD-3-Clause ([source](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The architecture validates or rolls back a single risk-increasing perpetual action, but explicitly does not wrap a list of strategy actions in one transaction. If the second action fails, the first can remain applied; a backtest that assumes all-or-nothing behavior would misstate exposure. |

## What this project does

A composable DeFi research library with generic spot, lending, pool, and perpetual entities. [Project README](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/README.md#L12).

## Mechanism inspected

The architecture validates or rolls back a single risk-increasing perpetual action, but explicitly does not wrap a list of strategy actions in one transaction. [Implementation](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/fractal/core/entities/protocols/hyperliquid.py#L149). [Related source 1](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/ARCHITECTURE.md#L154).

## Limitation that matters

If the second action fails, the first can remain applied; a backtest that assumes all-or-nothing behavior would misstate exposure. Protocol economics are simplified. This is a source review, not a runtime or security test.

## Practical check for a trading system

Record intent and outcome per action, and test failure at every point of a multi-order strategy step.

## Why this score

Its distinction between per-action and per-step guarantees transfers to execution and replay design.

## Source trail

[README](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/README.md#L12); [Implementation](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/fractal/core/entities/protocols/hyperliquid.py#L149); [Related source 1](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/ARCHITECTURE.md#L154) - [License](https://github.com/Logarithm-Labs/fractal-defi/blob/081f33f746f9f4fc43d0726f30c613ba660e989b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
