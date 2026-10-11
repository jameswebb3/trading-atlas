# FinRL_Podracer — A futures environment with no step is not a backtest

**Decision question:** Is the advertised futures environment executable as a trading simulator?

| Field | Review |
| --- | --- |
| Upstream | [AI4Finance-Foundation/FinRL_Podracer](https://github.com/AI4Finance-Foundation/FinRL_Podracer) |
| Primary area | Backtesting & Simulation |
| Source commit | [3e841f7d8cb47f7806063b39bcfa7a2b11472e06](https://github.com/AI4Finance-Foundation/FinRL_Podracer/commit/3e841f7d8cb47f7806063b39bcfa7a2b11472e06) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | The inspected `FutureTradingEnv` parses a CSV, randomly selects a window and constructs an account/position/price state. Its `step` method is `pass`; this path defines no action transition, fills, fees or reward, so the futures claim cannot support a replay result. |

## What this project does

FinRL successor project with reinforcement-learning agents and environment examples. [README](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/README.md).

## Mechanism inspected

The inspected `FutureTradingEnv` parses a CSV, randomly selects a window and constructs an account/position/price state. [Implementation](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/Podracer/src/elegantrl/envs/FutureTradingEnv.py#L8-L50).

## Limitation that matters

Its `step` method is `pass`; this path defines no action transition, fills, fees or reward, so the futures claim cannot support a replay result. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require a complete state-transition and fill path before accepting an RL environment as evidence of trading behavior.

## Why this score

The inspected `FutureTradingEnv` parses a CSV, randomly selects a window and constructs an account/position/price state. Its `step` method is `pass`; this path defines no action transition, fills, fees or reward, so the futures claim cannot support a replay result.

## Source trail

[README](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/README.md) · [Implementation](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/Podracer/src/elegantrl/envs/FutureTradingEnv.py#L8-L50) · [License](https://github.com/AI4Finance-Foundation/FinRL_Podracer/blob/3e841f7d8cb47f7806063b39bcfa7a2b11472e06/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
