# Prediction Market Backtester - Does the reported latency actually delay each simulated order?

**Decision question:** Does the reported latency actually delay each simulated order?

| Field | Review |
| --- | --- |
| Upstream | [Quentin-Piot/prediction-market-backtester](https://github.com/Quentin-Piot/prediction-market-backtester) |
| Primary area | Backtesting & Simulation |
| Source commit | [c77dff74680bceadc4e028019821db7a54bf1014](https://github.com/Quentin-Piot/prediction-market-backtester/commit/c77dff74680bceadc4e028019821db7a54bf1014) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Queues orders by bar-index latency and records full run artifacts; the default latency is zero and book depth is absent. A zero-bar configuration can fill on the same snapshot that produced the signal. |

## What this project does

A Polymarket/Kalshi research engine with explicit trade-quality checks, fills, portfolio accounting and per-run artifacts.

## Mechanism inspected

Incoming orders enter a pending queue with ready_bar_index equal to the current bar plus configured latency. Orders for other markets remain queued until their matching snapshot arrives. The simulator then applies spread, slippage, fees and cash or position limits.

## Limitation that matters

The configuration defaults latency_bars to zero, so the default can execute an incoming order on the current snapshot. Fills are immediate after activation with no historical depth or partial-fill queue. A two-cent spread proxy may replace a real quote.

## Practical check for a trading system

Inspect the actual latency setting in every result, not just the existence of a latency parameter; label proxy-spread and immediate-fill runs separately from book-backed ones.

## Why this score

3/5 because Transparent order activation and run artifacts are useful, but zero default delay and proxy fills restrict causal/execution conclusions.

## Source trail

[README execution assumptions](https://github.com/Quentin-Piot/prediction-market-backtester/blob/c77dff74680bceadc4e028019821db7a54bf1014/README.md#L70); [Latency default](https://github.com/Quentin-Piot/prediction-market-backtester/blob/c77dff74680bceadc4e028019821db7a54bf1014/src/pm_bt/execution/simulator.py#L16); [Pending-order activation](https://github.com/Quentin-Piot/prediction-market-backtester/blob/c77dff74680bceadc4e028019821db7a54bf1014/src/pm_bt/execution/simulator.py#L127); [Input quality checks](https://github.com/Quentin-Piot/prediction-market-backtester/blob/c77dff74680bceadc4e028019821db7a54bf1014/src/pm_bt/data/quality.py#L50); [License](https://github.com/Quentin-Piot/prediction-market-backtester/blob/c77dff74680bceadc4e028019821db7a54bf1014/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
