# Kalshi Order Book Capture - Can a polling collector say why book history is incomplete?

**Decision question:** Can a polling collector say why book history is incomplete?

| Field | Review |
| --- | --- |
| Upstream | [markm101/Kalshi-Orderbook-Scraper](https://github.com/markm101/Kalshi-Orderbook-Scraper) |
| Primary area | Market Data & Ingestion |
| Source commit | [a93303ee185ce44a14e47686d4aec481110a4119](https://github.com/markm101/Kalshi-Orderbook-Scraper/commit/a93303ee185ce44a14e47686d4aec481110a4119) |
| Reviewed | 2026-10-11 |
| Declared license | No root license file found at the reviewed commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Writes Kalshi book snapshots with explicit failure events and market lifecycle tracking; polling still leaves unobserved changes. A clean gaps.csv cannot certify continuity between successful polling instants. |

## What this project does

A read-only Kalshi collector that periodically discovers markets, fetches order-book batches and writes timestamped rows plus a gap log.

## Mechanism inspected

The capture loop records startup, discovery failures, empty selections, zero-row responses, parse failures and missing tickers as distinct gap events. It refreshes market status and keeps selected markets until closure; each saved level carries a snapshot grouping key.

## Limitation that matters

Gap logs explain observed collection failures, but polling between successful requests cannot recover unseen book changes. A row-level snapshot ID is not a guarantee that every update between two samples was observed. No root license file was found at the inspected commit.

## Practical check for a trading system

Use the gap ledger as a first coverage layer and label the feed sampled; reserve continuous-book claims for an event stream with sequence and resync evidence.

## Why this score

3/5 because Concrete Kalshi capture and failure taxonomy are useful, while interval sampling and missing licensing limit reuse.

## Source trail

[README output contract](https://github.com/markm101/Kalshi-Orderbook-Scraper/blob/a93303ee185ce44a14e47686d4aec481110a4119/README.md#L246); [Capture lifecycle](https://github.com/markm101/Kalshi-Orderbook-Scraper/blob/a93303ee185ce44a14e47686d4aec481110a4119/kalshi_capture/capture.py#L63); [Failure events](https://github.com/markm101/Kalshi-Orderbook-Scraper/blob/a93303ee185ce44a14e47686d4aec481110a4119/kalshi_capture/capture.py#L222); [Gap schema](https://github.com/markm101/Kalshi-Orderbook-Scraper/blob/a93303ee185ce44a14e47686d4aec481110a4119/kalshi_capture/gaps.py#L8).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
