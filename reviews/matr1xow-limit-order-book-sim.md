# limit-order-book-sim - How much maker edge survives plausible queue positions?

**Decision question:** How much maker edge survives plausible queue positions?

| Field | Review |
| --- | --- |
| Upstream | [Matr1xOw/limit-order-book-sim](https://github.com/Matr1xOw/limit-order-book-sim) |
| Primary area | Backtesting & Simulation |
| Source commit | [923a4da9827cba58c56a43e0f215d870246a914f](https://github.com/Matr1xOw/limit-order-book-sim/commit/923a4da9827cba58c56a43e0f215d870246a914f) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Simulates passive queue position under cancellation bounds and checks reconstructed books against separate snapshots. If edge exists only under the ahead-cancellation assumption, the maker fill result is not robust. |

## What this project does

A limit-order-book reconstruction and passive-order fill simulator for message data, with an independent market-by-price snapshot validation path.

## Mechanism inspected

A passive order joins behind visible size at its price and receives fills only after queue-ahead volume is consumed. The simulator brackets unknown cancellation location with ahead/behind assumptions; validate.py compares a reconstructed message stream to independent book snapshots.

## Limitation that matters

A level-size feed cannot identify precisely which cancellations were ahead of the simulated order. The code therefore offers bounds rather than a single verified fill probability. Its inspected data adapters use equity-market microstructure, so venue and fee assumptions must be reworked for crypto perps.

## Practical check for a trading system

Run queue-position sensitivity bands and reconcile a rebuilt book against a separate feed before accepting maker backtest profits.

## Why this score

4/5 because Direct queue and independent-book validation mechanisms are visible; unknown cancellation priority remains a fundamental limit.

## Source trail

[README cancellation bounds](https://github.com/Matr1xOw/limit-order-book-sim/blob/923a4da9827cba58c56a43e0f215d870246a914f/README.md#L105); [Queue fill model](https://github.com/Matr1xOw/limit-order-book-sim/blob/923a4da9827cba58c56a43e0f215d870246a914f/simulator.py#L1); [Independent reconstruction check](https://github.com/Matr1xOw/limit-order-book-sim/blob/923a4da9827cba58c56a43e0f215d870246a914f/validate.py#L156); [Book-state model](https://github.com/Matr1xOw/limit-order-book-sim/blob/923a4da9827cba58c56a43e0f215d870246a914f/book.py#L1); [License](https://github.com/Matr1xOw/limit-order-book-sim/blob/923a4da9827cba58c56a43e0f215d870246a914f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
