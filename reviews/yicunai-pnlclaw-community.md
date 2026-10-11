# Pnlclaw-community — Spot cash arithmetic is not a perpetual portfolio

**Decision question:** Does the backtest account for perpetual margin and funding?

| Field | Review |
| --- | --- |
| Upstream | [YicunAI/Pnlclaw-community](https://github.com/YicunAI/Pnlclaw-community) |
| Primary area | Backtesting & Simulation |
| Source commit | [933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb](https://github.com/YicunAI/Pnlclaw-community/commit/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb) |
| Reviewed | 2026-10-09 |
| Declared license | AGPL-3.0 ([source](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | A fill updates cash by the full price times quantity plus or minus fee and records signed inventory; bar close marks equity as cash plus quantity times latest price. The inspected portfolio is spot-style accounting. It does not model perpetual margin, funding, liquidation or venue exposure, so its equity curve cannot validate an HL USDC perpetual strategy. |

## What this project does

Local-first crypto research desktop with a strategy workflow and a lightweight backtest portfolio. [README](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/README.md).

## Mechanism inspected

A fill updates cash by the full price times quantity plus or minus fee and records signed inventory; bar close marks equity as cash plus quantity times latest price. [Implementation](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/packages/backtest-engine/pnlclaw_backtest/portfolio.py#L50-L82).

## Limitation that matters

The inspected portfolio is spot-style accounting. It does not model perpetual margin, funding, liquidation or venue exposure, so its equity curve cannot validate an HL USDC perpetual strategy. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require instrument-specific accounting tests for margin, funding, fees, partial fills and liquidation before using a crypto backtest as perpetual evidence.

## Why this score

A fill updates cash by the full price times quantity plus or minus fee and records signed inventory; bar close marks equity as cash plus quantity times latest price. The inspected portfolio is spot-style accounting. It does not model perpetual margin, funding, liquidation or venue exposure, so its equity curve cannot validate an HL USDC perpetual strategy.

## Source trail

[README](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/README.md) · [Implementation](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/packages/backtest-engine/pnlclaw_backtest/portfolio.py#L50-L82) · [License](https://github.com/YicunAI/Pnlclaw-community/blob/933014faffa38fd2de6c5d9ecdb3c6dc1fe2f2bb/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
