# VOOI Funding Bot — The cancel race creates half-leg exposure

**Decision question:** What happens when one leg fills while a cross-venue cancel is in flight?

| Field | Review |
| --- | --- |
| Upstream | [vooi-app/vooi-funding-bot-example](https://github.com/vooi-app/vooi-funding-bot-example) |
| Primary area | Signals & Models |
| Source commit | [c3ceab29e80bb26fd6bde128280cb5da5428f3f1](https://github.com/vooi-app/vooi-funding-bot-example/commit/c3ceab29e80bb26fd6bde128280cb5da5428f3f1) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The code distinguishes unknown positions from empty ones and rechecks position around a limit-order cancel race. Its own header lists no client-order-ID reconciliation after a 5xx and no journal recovery after a crash; the strategy also depends on two venues. |

## What this project does

An MVP for cross-venue perpetual funding arbitrage, potentially including Hyperliquid as one leg. [Project README](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/README.md#L19).

## Mechanism inspected

The code distinguishes unknown positions from empty ones and rechecks position around a limit-order cancel race. [Implementation](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/fundbot/mvp.py#L1). [Related source 1](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/docs/STRATEGY.md#L96). [Related source 2](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/fundbot/mvp.py#L1118).

## Limitation that matters

Its own header lists no client-order-ID reconciliation after a 5xx and no journal recovery after a crash; the strategy also depends on two venues. This is a source review, not a runtime or security test.

## Practical check for a trading system

Model each leg as an independently reconciled position and block retries while either venue outcome is unknown.

## Why this score

The race handling is informative for execution, while its cross-venue alpha is outside single-venue applicability.

## Source trail

[README](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/README.md#L19); [Implementation](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/fundbot/mvp.py#L1); [Related source 1](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/docs/STRATEGY.md#L96); [Related source 2](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/fundbot/mvp.py#L1118) - [License](https://github.com/vooi-app/vooi-funding-bot-example/blob/c3ceab29e80bb26fd6bde128280cb5da5428f3f1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
