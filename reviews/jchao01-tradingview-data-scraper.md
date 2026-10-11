# TradingView-data-scraper — A rendered chart is a weak market-data contract

**Decision question:** Does a chart scraper preserve source timing and completeness?

| Field | Review |
| --- | --- |
| Upstream | [jchao01/TradingView-data-scraper](https://github.com/jchao01/TradingView-data-scraper) |
| Primary area | Market Data & Ingestion |
| Source commit | [b58529809a690261fb9a2caac0b60fdeccbb608d](https://github.com/jchao01/TradingView-data-scraper/commit/b58529809a690261fb9a2caac0b60fdeccbb608d) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | A request-supplied URL is opened in a browser, and the service parses page classes plus embedded chart options for bars and indicators. The path depends on UI structure, accepts arbitrary URLs, suppresses TLS errors and records no local receipt/completeness contract. It is unsuitable as a trusted historical feed for trading research. |

## What this project does

Small Flask service that renders a TradingView page with a headless browser and extracts chart JSON from the DOM. [README](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/README.md).

## Mechanism inspected

A request-supplied URL is opened in a browser, and the service parses page classes plus embedded chart options for bars and indicators. [Implementation](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/app.py#L32-L44). [Related implementation](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/app.py#L52-L90).

## Limitation that matters

The path depends on UI structure, accepts arbitrary URLs, suppresses TLS errors and records no local receipt/completeness contract. It is unsuitable as a trusted historical feed for trading research. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Prefer venue or licensed source data with event time, receipt time and gap accounting; keep rendered-page extraction out of causal backtests.

## Why this score

A request-supplied URL is opened in a browser, and the service parses page classes plus embedded chart options for bars and indicators. The path depends on UI structure, accepts arbitrary URLs, suppresses TLS errors and records no local receipt/completeness contract. It is unsuitable as a trusted historical feed for trading research.

## Source trail

[README](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/README.md) · [Implementation](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/app.py#L32-L44) · [Related implementation](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/app.py#L52-L90) · [License](https://github.com/jchao01/TradingView-data-scraper/blob/b58529809a690261fb9a2caac0b60fdeccbb608d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
