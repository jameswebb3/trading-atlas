# PredictionMarketBench - Can a trading-agent benchmark separate no fill from order rejection?

**Decision question:** Can a trading-agent benchmark separate no fill from order rejection?

| Field | Review |
| --- | --- |
| Upstream | [Oddpool/PredictionMarketBench](https://github.com/Oddpool/PredictionMarketBench) |
| Primary area | Agents & Decision Systems |
| Source commit | [611d66941717310858683278940df21c33c406f2](https://github.com/Oddpool/PredictionMarketBench/commit/611d66941717310858683278940df21c33c406f2) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Grades agents against replayed Kalshi books and distinguishes a no-fill IOC from an actual rejection. Displayed depth and a simulated pro-rata maker queue do not prove venue fills. |

## What this project does

A Kalshi market-replay benchmark exposing market, book, cash, order and cancellation tools to trading agents.

## Mechanism inspected

The execution engine distinguishes non-crossing IOC orders that simply receive no fill from rejected orders, and it consumes executable book levels in price order with partial fills and per-fill taker fees.

## Limitation that matters

The README's maker-taker mode simulates queue position from displayed size and pro-rata allocation; neither is an observed individual queue priority. The inspected immediate execution path does not verify whether an order could arrive before a displayed quote changes. No root license text was verified.

## Practical check for a trading system

Grade agents on decisions, rejected actions and executable filled quantity separately; stress maker results under alternative queue assumptions.

## Why this score

3/5 because A source-visible execution benchmark is useful, but queue and arrival-time realism limit its grading authority.

## Source trail

[README](https://github.com/Oddpool/PredictionMarketBench/blob/611d66941717310858683278940df21c33c406f2/README.md#L82); [README](https://github.com/Oddpool/PredictionMarketBench/blob/611d66941717310858683278940df21c33c406f2/README.md#L128); [src/oddpool_bench/execution.py](https://github.com/Oddpool/PredictionMarketBench/blob/611d66941717310858683278940df21c33c406f2/src/oddpool_bench/execution.py#L130); [src/oddpool_bench/execution.py](https://github.com/Oddpool/PredictionMarketBench/blob/611d66941717310858683278940df21c33c406f2/src/oddpool_bench/execution.py#L163).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
