# QuantOS - Can an order fill without a current market price?

**Decision question:** Can an order fill without a current market price?

| Field | Review |
| --- | --- |
| Upstream | [AliJuya/QuantOS](https://github.com/AliJuya/QuantOS) |
| Primary area | Backtesting & Simulation |
| Source commit | [b3859e683c17f0325c7e042aae9912d785c57f8f](https://github.com/AliJuya/QuantOS/commit/b3859e683c17f0325c7e042aae9912d785c57f8f) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The simulated broker rejects an order when it has neither a stored market price nor a forced fill price; otherwise it applies directional slippage and fees. A forced_fill_price in order metadata bypasses the missing-market-price rejection, so its provenance must be controlled by the caller. |

## What this project does

A modular trading-research framework with replay, risk and simulated execution.

## Mechanism inspected

The simulated broker rejects an order when it has neither a stored market price nor a forced fill price; otherwise it applies directional slippage and fees.

## Limitation that matters

A forced_fill_price in order metadata bypasses the missing-market-price rejection, so its provenance must be controlled by the caller.

## Practical check for a trading system

Keep synthetic fill overrides explicit in run manifests and forbid them in production-equivalence tests.

## Why this score

2/5. A useful simulator seam whose override can hide absent market evidence.

## Source trail

[README](https://github.com/AliJuya/QuantOS/blob/b3859e683c17f0325c7e042aae9912d785c57f8f/README.md#L1); [docs/architecture/upgrade_roadmap.md](https://github.com/AliJuya/QuantOS/blob/b3859e683c17f0325c7e042aae9912d785c57f8f/docs/architecture/upgrade_roadmap.md#L1); [qcore/execution/brokers/simulator.py](https://github.com/AliJuya/QuantOS/blob/b3859e683c17f0325c7e042aae9912d785c57f8f/qcore/execution/brokers/simulator.py#L28).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
