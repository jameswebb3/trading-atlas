# stock — Partial collection needs an explicit denominator

**Decision question:** Does a scheduled data job report the expected and succeeded universe?

| Field | Review |
| --- | --- |
| Upstream | [myhhub/stock](https://github.com/myhhub/stock) |
| Primary area | Data Quality & Lineage |
| Source commit | [b6e0ca2268cfbadd02f5ed052159c187b6670231](https://github.com/myhhub/stock/commit/b6e0ca2268cfbadd02f5ed052159c187b6670231) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The daily backtest data job logs an exception per stock and continues, leaving the run able to complete with a partial set of securities. Equities collection is not a Hyperliquid feed; the inspected path does not establish how downstream consumers detect incompleteness. |

## What this project does

Equity data collector and backtest job suite that loops over securities. [README](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/README.md).

## Mechanism inspected

The daily backtest data job logs an exception per stock and continues, leaving the run able to complete with a partial set of securities. [Implementation](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/job/backtest_data_daily_job.py#L45-L94).

## Limitation that matters

Equities collection is not a Hyperliquid feed; the inspected path does not establish how downstream consumers detect incompleteness. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Attach expected count, successful count and explicit exclusions to each batch manifest; fail or quarantine a partial run before research consumes it.

## Why this score

The daily backtest data job logs an exception per stock and continues, leaving the run able to complete with a partial set of securities. Equities collection is not a Hyperliquid feed; the inspected path does not establish how downstream consumers detect incompleteness.

## Source trail

[README](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/README.md) · [Implementation](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/instock/job/backtest_data_daily_job.py#L45-L94) · [License](https://github.com/myhhub/stock/blob/b6e0ca2268cfbadd02f5ed052159c187b6670231/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
