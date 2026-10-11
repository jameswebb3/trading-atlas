# CleoLOB — Refuse analyses that exceed the data's capabilities

**Decision question:** Can aggregate L2 data support an exact passive-fill claim?

| Field | Review |
| --- | --- |
| Upstream | [damraka/CleoLOB](https://github.com/damraka/CleoLOB) |
| Primary area | Backtesting & Simulation |
| Source commit | [4f90ef8cc5fce58d855f49561aff116a2bf7de8c](https://github.com/damraka/CleoLOB/commit/4f90ef8cc5fce58d855f49561aff116a2bf7de8c) |
| Reviewed | 2026-10-10 |
| Declared license | LGPL-3.0 |
| Review depth | 2/3: README, relevant source inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Its analysis registry specifies required data capabilities and returns NOT_AVAILABLE with missing fields rather than weakening an exact-fill study silently. The gate trusts the declared venue and dataset contract; it does not establish that the raw feed is complete or that simulated fills match a real venue. |

## What this project does

CleoLOB is a market-microstructure and execution research framework with historical replay, simulated execution, calibration and model-risk studies. [Project README](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/README.md#L1).

## Mechanism inspected

The capability table requires aggregate depth and trade prints for bounded replay, but exact FIFO position and observed fills for exact passive-fill analysis. An unknown analysis raises, while missing capabilities produce NOT_AVAILABLE and a list of missing fields. [Capability gate](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/lob/v07/data/capability.py#L13).

## Limitation that matters

This is a contract over declared capabilities. It is not a check that every input event arrived, nor empirical proof of execution realism. The project reports separate historical limits and model-risk results rather than treating simulator output as live evidence. This is a source review, not a runtime or security test.

## Practical check for a trading system

Before scoring an execution idea, declare the market-data evidence required by that question. Return an explicit unavailable result when order identity or observed fills are absent; retain L2-derived bounds as bounds.

## Why this score

4/5 because the explicit distinction between L2 replay and exact queue/fill evidence is directly useful when deciding what a trading study may claim.

## Source trail

[README](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/README.md#L29); [Capability gate](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/lob/v07/data/capability.py#L13); [Model-risk report](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/docs/v07-model-risk.md#L127); [License](https://github.com/damraka/CleoLOB/blob/4f90ef8cc5fce58d855f49561aff116a2bf7de8c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
