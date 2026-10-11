# Kalshi Trading Framework - Can a model ablation inherit an optimistic fill proxy?

**Decision question:** Can a model ablation inherit an optimistic fill proxy?

| Field | Review |
| --- | --- |
| Upstream | [ferraijv/kalshi](https://github.com/ferraijv/kalshi) |
| Primary area | Research & Reproducibility |
| Source commit | [850276d670f9409aeb478579e09151fe782bc645](https://github.com/ferraijv/kalshi/commit/850276d670f9409aeb478579e09151fe782bc645) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README, relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Runs named feature ablations, but its rolling PnL uses a candle-derived midpoint fill proxy. Model ranking by midpoint PnL is not evidence of executable Kalshi edge. |

## What this project does

A Kalshi TSA-market research framework with a model registry, rolling backtest and feature-ablation runner.

## Mechanism inspected

The ablation runner records named feature sets and model metrics across a configured backtest window. Its rolling backtest derives an implied fill price from candle data, using bid/ask midpoint when available.

## Limitation that matters

A midpoint of bid and ask is not a taker execution price; the code itself calls the quantity an implied fill probability. Ablation ranking that uses this PnL proxy cannot be interpreted as attainable trading PnL without executable quotes and delay.

## Practical check for a trading system

Keep proper scoring of predicted probabilities separate from execution scoring; rerun any promoted variant at bid/ask with depth and latency.

## Why this score

2/5 because The experiment bookkeeping is useful, but the inspected fill proxy is a material economic limitation.

## Source trail

[README](https://github.com/ferraijv/kalshi/blob/850276d670f9409aeb478579e09151fe782bc645/README.md#L1); [src/kalshi/run_tsa_feature_ablation.py](https://github.com/ferraijv/kalshi/blob/850276d670f9409aeb478579e09151fe782bc645/src/kalshi/run_tsa_feature_ablation.py#L48); [src/kalshi/backtest_tsa.py](https://github.com/ferraijv/kalshi/blob/850276d670f9409aeb478579e09151fe782bc645/src/kalshi/backtest_tsa.py#L62); [src/kalshi/backtest_tsa.py](https://github.com/ferraijv/kalshi/blob/850276d670f9409aeb478579e09151fe782bc645/src/kalshi/backtest_tsa.py#L99).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
