# HyperData Terminal — Label sampled and inferred market data

**Decision question:** Are liquidation counts exchange facts, samples, or heuristic estimates?

| Field | Review |
| --- | --- |
| Upstream | [Co-Messi/HyperData-Terminal](https://github.com/Co-Messi/HyperData-Terminal) |
| Primary area | Execution & Exchange Integration |
| Source commit | [5fd1f0264391de1b65b18014049ea61161d82d51](https://github.com/Co-Messi/HyperData-Terminal/commit/5fd1f0264391de1b65b18014049ea61161d82d51) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Its data-integrity documentation labels Hyperliquid liquidations as heuristic and distinguishes confirmed from sampled venue feeds. A heuristic liquidation series cannot be treated as exchange-confirmed ground truth. |

## What this project does

A multi-venue crypto terminal emphasizing feed coverage and integrity labels. [Project README](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/README.md#L22).

## Mechanism inspected

Its data-integrity documentation labels Hyperliquid liquidations as heuristic and distinguishes confirmed from sampled venue feeds. [Implementation](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/hyperdata_terminal/data_layer/liquidation_feed.py#L56). [Related source 1](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/docs/DATA_INTEGRITY.md#L8).

## Limitation that matters

A heuristic liquidation series cannot be treated as exchange-confirmed ground truth. The reviewed data path does not establish a complete census or independent accuracy test. This is a source review, not a runtime or security test.

## Practical check for a trading system

Attach method and coverage labels to every liquidation-derived feature before comparing it with trading outcomes.

## Why this score

Directly relevant to avoiding false labels in market-data research, while the feed coverage remains limited.

## Source trail

[README](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/README.md#L22); [Implementation](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/hyperdata_terminal/data_layer/liquidation_feed.py#L56); [Related source 1](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/docs/DATA_INTEGRITY.md#L8) - [License](https://github.com/Co-Messi/HyperData-Terminal/blob/5fd1f0264391de1b65b18014049ea61161d82d51/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
