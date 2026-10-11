# Homerun - What happens when a learned maker fill model cannot score?

**Decision question:** What happens when a learned maker fill model cannot score?

| Field | Review |
| --- | --- |
| Upstream | [braedonsaunders/homerun](https://github.com/braedonsaunders/homerun) |
| Primary area | Backtesting & Simulation |
| Source commit | [6cb8ea5614e7a1b6f4c692a5b17436e888904092](https://github.com/braedonsaunders/homerun/commit/6cb8ea5614e7a1b6f4c692a5b17436e888904092) |
| Reviewed | 2026-10-11 |
| Declared license | AGPL-3.0 |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Combines seeded latency and book replay, while defaulting an unscorable learned fill to probability 1.0. Report fallback coverage before treating maker fill estimates as empirical. |

## What this project does

A large prediction-market platform that advertises book replay, measured latency and learned fill probabilities.

## Mechanism inspected

Its backtest engine wires a seeded latency model and a configurable fill-model snapshot into the matching path. The same configuration also defines a fallback fill probability.

## Limitation that matters

At the reviewed commit, fill_probability_fallback defaults to 1.0 when a loaded model cannot score. This is optimistic for a passive order; claims of replay fidelity therefore depend on proving the model scored each order or setting a conservative fallback. The project is AGPL-3.0.

## Practical check for a trading system

Expose model coverage, fallback count and sensitivity to pessimistic fill assumptions next to any maker PnL.

## Why this score

2/5 because Useful direct fill-model architecture, but a success-like fallback materially weakens unqualified backtest claims.

## Source trail

[README](https://github.com/braedonsaunders/homerun/blob/6cb8ea5614e7a1b6f4c692a5b17436e888904092/README.md#L102); [backend/services/backtest/engine.py](https://github.com/braedonsaunders/homerun/blob/6cb8ea5614e7a1b6f4c692a5b17436e888904092/backend/services/backtest/engine.py#L99); [backend/services/backtest/engine.py](https://github.com/braedonsaunders/homerun/blob/6cb8ea5614e7a1b6f4c692a5b17436e888904092/backend/services/backtest/engine.py#L104); [backend/services/backtest/engine.py](https://github.com/braedonsaunders/homerun/blob/6cb8ea5614e7a1b6f4c692a5b17436e888904092/backend/services/backtest/engine.py#L169); [License text](https://github.com/braedonsaunders/homerun/blob/6cb8ea5614e7a1b6f4c692a5b17436e888904092/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
