# Automated Paper Trading Bot - Can a strategy change exposure without bypassing risk rules?

**Decision question:** Can a strategy change exposure without bypassing risk rules?

| Field | Review |
| --- | --- |
| Upstream | [WalllerG/Automated-paper-trading-bot](https://github.com/WalllerG/Automated-paper-trading-bot) |
| Primary area | Portfolio & Risk |
| Source commit | [a5122059dd04dc74a430eadac9bc81b5ac34eee9](https://github.com/WalllerG/Automated-paper-trading-bot/commit/a5122059dd04dc74a430eadac9bc81b5ac34eee9) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Keeps position sizing and drawdown halts outside strategy code, with the same risk object in backtest and paper trading. The stop model fills exactly at its trigger price even when real markets can gap through it. |

## What this project does

An equities paper-trading system that shares strategy and risk objects between backtest and live loops.

## Mechanism inspected

The strategy supplies a target signal; RiskManager computes allowed weight and share count and halts on equity drawdown. The live loop reuses that risk object and acts on closed bars.

## Limitation that matters

Backtested stops execute exactly at the stop price, which the source itself calls optimistic under gaps. Shared objects reduce logic drift but do not prove that a real broker produces the same fills or state after restart.

## Practical check for a trading system

Separate alpha output from enforceable sizing and halt decisions, and report modeled stop fills as an optimistic bound.

## Why this score

3/5 because The risk boundary is visible in both paths, but stop and broker execution remain simplified.

## Source trail

[README](https://github.com/WalllerG/Automated-paper-trading-bot/blob/a5122059dd04dc74a430eadac9bc81b5ac34eee9/README.md#L154); [autotrade/risk/manager.py](https://github.com/WalllerG/Automated-paper-trading-bot/blob/a5122059dd04dc74a430eadac9bc81b5ac34eee9/autotrade/risk/manager.py#L39); [autotrade/risk/manager.py](https://github.com/WalllerG/Automated-paper-trading-bot/blob/a5122059dd04dc74a430eadac9bc81b5ac34eee9/autotrade/risk/manager.py#L67); [autotrade/engine/backtest.py](https://github.com/WalllerG/Automated-paper-trading-bot/blob/a5122059dd04dc74a430eadac9bc81b5ac34eee9/autotrade/engine/backtest.py#L149); [License text](https://github.com/WalllerG/Automated-paper-trading-bot/blob/a5122059dd04dc74a430eadac9bc81b5ac34eee9/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
