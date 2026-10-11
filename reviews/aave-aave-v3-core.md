# Aave V3 Core — How does liquidation severity depend on account state

**Decision question:** How does liquidation severity depend on account state?

| Field | Review |
| --- | --- |
| Upstream | [Aave V3 Core](https://github.com/aave/aave-v3-core) |
| Primary area | Portfolio & Risk |
| Source commit | [782f51917056a53a2c228701058a6c3fb233684a](https://github.com/aave/aave-v3-core/commit/782f51917056a53a2c228701058a6c3fb233684a) |
| Reviewed | 2026-09-26 |
| Declared license | [BUSL-1.1 text; MIT change license dated 2023-01-27](https://github.com/aave/aave-v3-core/blob/782f51917056a53a2c228701058a6c3fb233684a/LICENSE.md) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A historical lending-risk reference that separates account health from the amount liquidated. The codebase is deprecated; its close-factor rules describe Aave rather than a general margin engine. |

## Project overview

This repository contains an older Aave V3 lending implementation. Its README states that it is deprecated and points to V3 Origin. [Project documentation](https://github.com/aave/aave-v3-core/blob/782f51917056a53a2c228701058a6c3fb233684a/README.md#L1-L27).

## Mechanism worth inspecting

The account interface distinguishes collateral, debt, borrowing capacity and health factor. Liquidation debt is capped by a close factor selected from the health factor, then by the requested repayment. [Account fields](https://github.com/aave/aave-v3-core/blob/782f51917056a53a2c228701058a6c3fb233684a/contracts/interfaces/IPool.sol#L467-L488), [debt cap](https://github.com/aave/aave-v3-core/blob/782f51917056a53a2c228701058a6c3fb233684a/contracts/protocol/libraries/logic/LiquidationLogic.sol#L354-L385).

## Important limit

These thresholds and units are Aave-specific and belong to a deprecated codebase. They must not be transferred into a perpetual-margin model without the actual venue's contract.

## Questions to take into your own design

- How does liquidation severity depend on account state?
- Are liquidation thresholds and units versioned for the actual protocol under review?

## Why this score for a trading system

2/5: concrete on-chain risk arithmetic, limited by deprecated maintenance and protocol-specific liquidation assumptions.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
