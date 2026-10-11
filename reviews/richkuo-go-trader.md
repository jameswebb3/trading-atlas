# go-trader - Can a live decision be compared honestly with a closed-bar backtest?

**Decision question:** Can a live decision be compared honestly with a closed-bar backtest?

| Field | Review |
| --- | --- |
| Upstream | [richkuo/go-trader](https://github.com/richkuo/go-trader) |
| Primary area | Research & Reproducibility |
| Source commit | [165c26492bd2c1d26374c5784bfcf6558273b7b0](https://github.com/richkuo/go-trader/commit/165c26492bd2c1d26374c5784bfcf6558273b7b0) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | The comparison classifies closed-bar versus forming-bar decisions and refuses to claim parity when historical decision inputs were not recorded. Even closed-bar mode can read bars later corrected by the venue and the scheduled check may lag the simulated boundary. |

## What this project does

A crypto trading system with a detailed booked-ledger comparison tool.

## Mechanism inspected

The comparison classifies closed-bar versus forming-bar decisions and refuses to claim parity when historical decision inputs were not recorded.

## Limitation that matters

Even closed-bar mode can read bars later corrected by the venue and the scheduled check may lag the simulated boundary.

## Practical check for a trading system

Record the actual decision input snapshot and source cutoff alongside each live order before claiming replay parity.

## Why this score

4/5. The code articulates a precise evidence boundary that is directly relevant to backtest/live comparison.

## Source trail

[README](https://github.com/richkuo/go-trader/blob/165c26492bd2c1d26374c5784bfcf6558273b7b0/README.md#L1); [docs/backtesting-registry.md](https://github.com/richkuo/go-trader/blob/165c26492bd2c1d26374c5784bfcf6558273b7b0/docs/backtesting-registry.md#L1); [backtest/ledger_compare.py](https://github.com/richkuo/go-trader/blob/165c26492bd2c1d26374c5784bfcf6558273b7b0/backtest/ledger_compare.py#L202); [Root license](https://github.com/richkuo/go-trader/blob/165c26492bd2c1d26374c5784bfcf6558273b7b0/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
