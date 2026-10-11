# Polylens - Can a failed order-book fetch be counted as a captured book?

**Decision question:** Can a failed order-book fetch be counted as a captured book?

| Field | Review |
| --- | --- |
| Upstream | [GNL324/polylens](https://github.com/GNL324/polylens) |
| Primary area | Market Data & Ingestion |
| Source commit | [ebae6fb97ce5e184f06251baaf38d6297e99628e](https://github.com/GNL324/polylens/commit/ebae6fb97ce5e184f06251baaf38d6297e99628e) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | Persists Kalshi book-fetch errors as records, yet increments the snapshot count for those placeholders. Do not read orderbooks_saved as valid order-book coverage without filtering error payloads. |

## What this project does

A prediction-market workbench whose Kalshi recorder persists market and order-book snapshots for downstream analysis.

## Mechanism inspected

The recorder discovers filtered markets, normalizes each market and saves a point-in-time row. It attempts a separate order-book request for each selected ticker and persists an error payload if that request raises.

## Limitation that matters

The same branch increments orderbooks_saved after writing the error payload. That counter is an attempted or stored record count, not a count of valid books; consumers must inspect raw_json or a separate quality flag before using coverage.

## Practical check for a trading system

Report capture attempts, successful decoded books and error placeholders as different numbers. A coverage numerator must exclude error records.

## Why this score

2/5 because The source exposes a concrete market-data denominator trap, but its recorder does not itself enforce a valid-book coverage gate.

## Source trail

[README overview](https://github.com/GNL324/polylens/blob/ebae6fb97ce5e184f06251baaf38d6297e99628e/README.md#L1); [Error placeholder and count](https://github.com/GNL324/polylens/blob/ebae6fb97ce5e184f06251baaf38d6297e99628e/src/analysis/kalshi_market_recorder.py#L39); [Recorded summary](https://github.com/GNL324/polylens/blob/ebae6fb97ce5e184f06251baaf38d6297e99628e/src/analysis/kalshi_market_recorder.py#L56); [License](https://github.com/GNL324/polylens/blob/ebae6fb97ce5e184f06251baaf38d6297e99628e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
