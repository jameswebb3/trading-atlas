# Awesome Systematic Trading — Beware the active-window denominator

**Decision question:** Can a strategy table change its score by trimming inactive NAV periods?

| Field | Review |
| --- | --- |
| Upstream | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) |
| Primary area | Signals & Models |
| Source commit | [ddfee8bb548bd6914191cb8fdb695d533ae16b0d](https://github.com/paperswithbacktest/awesome-systematic-trading/commit/ddfee8bb548bd6914191cb8fdb695d533ae16b0d) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The table builder discards flat NAV prefixes and suffixes, then measures only the remaining active window if it is long enough. That transformation changes the evaluation window and can hide capital sitting idle. |

## What this project does

A directory and generated comparison table for systematic-trading papers and strategies. [Project README](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/README.md#L15).

## Mechanism inspected

The table builder discards flat NAV prefixes and suffixes, then measures only the remaining active window if it is long enough. [Implementation](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/scripts/build_strategies_table.py#L98). [Related source 1](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/README.md#L24).

## Limitation that matters

That transformation changes the evaluation window and can hide capital sitting idle. The linked performance figures are not independent replications of the papers. This is a source review, not a runtime or security test.

## Practical check for a trading system

Publish both full-window and active-window statistics, with the exact start and end dates used.

## Why this score

Its measurement code exposes a concrete comparison hazard, while the strategy rankings are weak evidence for a live trading decision.

## Source trail

[README](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/README.md#L15); [Implementation](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/scripts/build_strategies_table.py#L98); [Related source 1](https://github.com/paperswithbacktest/awesome-systematic-trading/blob/ddfee8bb548bd6914191cb8fdb695d533ae16b0d/README.md#L24).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
