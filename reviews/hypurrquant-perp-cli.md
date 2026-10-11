# Perp CLI — A failed risk check must not become PASS

**Decision question:** Can exception handling silently bypass a pre-trade risk limit?

| Field | Review |
| --- | --- |
| Upstream | [hypurrquant/perp-cli](https://github.com/hypurrquant/perp-cli) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ed94cfd46259ff9186bf4f2489252a4f8f773e31](https://github.com/hypurrquant/perp-cli/commit/ed94cfd46259ff9186bf4f2489252a4f8f773e31) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Its pre-trade validator invokes a risk module after size and leverage checks; the response contract distinguishes errors and retryability. The inspected catch path records the risk-limits check as passed when the risk module throws, turning a missing risk verdict into a false green. |

## What this project does

A multi-venue perpetual-futures CLI with machine-readable response and validation contracts. [Project README](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/README.md#L1).

## Mechanism inspected

Its pre-trade validator invokes a risk module after size and leverage checks; the response contract distinguishes errors and retryability. [Implementation](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/src/trade-validator.ts#L199). [Related source 1](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/API_RESPONSE_SPEC.md#L6). [Related source 2](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/src/trade-validator.ts#L218-L220).

## Limitation that matters

The inspected catch path records the risk-limits check as passed when the risk module throws, turning a missing risk verdict into a false green. This is a source review, not a runtime or security test.

## Practical check for a trading system

Inject a risk-module failure and assert that order submission is blocked with an explicit Unknown or Error state.

## Why this score

Directly useful as an adversarial safety case; the bypass prevents treating this validator as a trustworthy live gate.

## Source trail

[README](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/README.md#L1); [Implementation](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/src/trade-validator.ts#L199); [Related source 1](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/API_RESPONSE_SPEC.md#L6); [Related source 2](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/src/trade-validator.ts#L199) - [License](https://github.com/hypurrquant/perp-cli/blob/ed94cfd46259ff9186bf4f2489252a4f8f773e31/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
