# KORE - Does a binary-market replay respect depth, cash and order expiry?

**Decision question:** Does a binary-market replay respect depth, cash and order expiry?

| Field | Review |
| --- | --- |
| Upstream | [Cole-Godfrey/kore](https://github.com/Cole-Godfrey/kore) |
| Primary area | Backtesting & Simulation |
| Source commit | [8879161b5667b8e64e0e3786a276a42766f7676d](https://github.com/Cole-Godfrey/kore/commit/8879161b5667b8e64e0e3786a276a42766f7676d) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Walks displayed binary-book depth, checks cash and positions, and records orders that expire before their latency elapses. Displayed size at a snapshot is an upper bound on executable size after order latency. |

## What this project does

A Kalshi order-book replay engine with strategy callbacks, binary YES/NO quote conversion, fees, portfolio checks and settlement.

## Mechanism inspected

The book model derives a YES ask from the reciprocal NO bid and walks displayed levels for marketable fills. The portfolio refuses cash-insufficient buys or sells beyond held size. Orders still pending at market close are recorded as expired before settlement is applied.

## Limitation that matters

Displayed depth is a book-state bound, not proof that an arriving order could take that size before the quote changed. The model is for Kalshi binary contracts, so its payout and fee rules must not be transferred to perpetuals.

## Practical check for a trading system

Use reciprocal-book pricing and explicit expired-order accounting as references; calibrate latency and fillability with an independently captured tape.

## Why this score

4/5 because The code implements direct book-aware fill and portfolio constraints with explicit close handling, though realized queue/arrival behavior remains unverified.

## Source trail

[README execution scope](https://github.com/Cole-Godfrey/kore/blob/8879161b5667b8e64e0e3786a276a42766f7676d/README.md#L11); [Reciprocal quote and depth](https://github.com/Cole-Godfrey/kore/blob/8879161b5667b8e64e0e3786a276a42766f7676d/src/kalshi_backtest/orderbook.py#L35); [Cash and position checks](https://github.com/Cole-Godfrey/kore/blob/8879161b5667b8e64e0e3786a276a42766f7676d/src/kalshi_backtest/portfolio.py#L32); [Order expiry and settlement](https://github.com/Cole-Godfrey/kore/blob/8879161b5667b8e64e0e3786a276a42766f7676d/src/kalshi_backtest/backtest.py#L241); [License](https://github.com/Cole-Godfrey/kore/blob/8879161b5667b8e64e0e3786a276a42766f7676d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
