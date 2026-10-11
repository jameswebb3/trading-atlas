# AgriQuant AI - Can a historical forecast be reconstructed from the event it was meant to predict?

**Decision question:** Can a historical forecast be reconstructed from the event it was meant to predict?

| Field | Review |
| --- | --- |
| Upstream | [AgriQuantAI/AgriQuant-AI](https://github.com/AgriQuantAI/AgriQuant-AI) |
| Primary area | Backtesting & Simulation |
| Source commit | [6b8a25e7e0eeb6d8d672ff7fc0e03999be16f84f](https://github.com/AgriQuantAI/AgriQuant-AI/commit/6b8a25e7e0eeb6d8d672ff7fc0e03999be16f84f) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The backtest dates a forecast three days before an event but builds its severity from that event actuals. The generated timestamp is retrospective: it does not establish that the forecast was available at that time. |

## What this project does

An agricultural event backtest with simulated forecasts.

## Mechanism inspected

The backtest dates a forecast three days before an event but builds its severity from that event actuals.

## Limitation that matters

The generated timestamp is retrospective: it does not establish that the forecast was available at that time.

## Practical check for a trading system

Require archived forecast vintages or mark the exercise as retrospective reconstruction.

## Why this score

1/5. The code visibly demonstrates a lookahead trap, not transferable alpha.

## Source trail

[README](https://github.com/AgriQuantAI/AgriQuant-AI/blob/6b8a25e7e0eeb6d8d672ff7fc0e03999be16f84f/README.md#L1); [backtest.py](https://github.com/AgriQuantAI/AgriQuant-AI/blob/6b8a25e7e0eeb6d8d672ff7fc0e03999be16f84f/backtest.py#L64); [backtest.py](https://github.com/AgriQuantAI/AgriQuant-AI/blob/6b8a25e7e0eeb6d8d672ff7fc0e03999be16f84f/backtest.py#L94).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
