# Wisp - Is the advertised backtest available in the reviewed build?

**Decision question:** Is the advertised backtest available in the reviewed build?

| Field | Review |
| --- | --- |
| Upstream | [wisp-trading/wisp](https://github.com/wisp-trading/wisp) |
| Primary area | Backtesting & Simulation |
| Source commit | [b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48](https://github.com/wisp-trading/wisp/commit/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and test source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | Advertises backtesting while its inspected backtest service returns unavailable. The live strategy example does not establish the missing replay engine. |

## What this project does

A Go terminal workstation for live trading and strategy scaffolding, with backtesting advertised on its homepage.

## Mechanism inspected

The inspected backtest service explicitly returns an unavailable error from both interactive and programmatic entry points. Its funding-tilt example reads live position size before choosing an exit quantity.

## Limitation that matters

The current build offers a useful live position-size guard but no runnable backtest behind the inspected service. Treating its README backtesting claim as evidence of deterministic replay would be unsound.

## Practical check for a trading system

Verify the actual entry point and supported build before using a project as a backtest reference; reuse only the separately inspected live-position guard as an idea.

## Why this score

1/5. The advertised headline and source diverge on the requested capability, giving little backtest mechanism to borrow.

## Source trail

[README](https://github.com/wisp-trading/wisp/blob/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48/README.md#L5); [internal/handlers/strategies/backtest/services/backtest.go](https://github.com/wisp-trading/wisp/blob/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48/internal/handlers/strategies/backtest/services/backtest.go#L10); [internal/handlers/strategies/backtest/services/backtest.go](https://github.com/wisp-trading/wisp/blob/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48/internal/handlers/strategies/backtest/services/backtest.go#L17); [examples/funding-tilt/strategy.go](https://github.com/wisp-trading/wisp/blob/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48/examples/funding-tilt/strategy.go#L151); [License text](https://github.com/wisp-trading/wisp/blob/b34ac40475b6554fb0cefe8ef0a15d9d6c1ddd48/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
