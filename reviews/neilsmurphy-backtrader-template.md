# backtrader_template — Fill deduplication can fail across ID formats

**Decision question:** Does replay deduplicate fills using the same representation it stores?

| Field | Review |
| --- | --- |
| Upstream | [neilsmurphy/backtrader_template](https://github.com/neilsmurphy/backtrader_template) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ad9311a3e152e8f4781ddd093b02da13cbd50792](https://github.com/neilsmurphy/backtrader_template/commit/ad9311a3e152e8f4781ddd093b02da13cbd50792) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | The broker checks whether a fill dictionary is present in an executed_fills list but stores only the fill ID. Replayed fills therefore do not match that membership test. This is a defect in the inspected adapter, not an operationally proven loss in the house; its exchange and Backtrader versions may differ. |

## What this project does

Backtrader template with a CCXT broker adapter and local order/fill reconciliation. [README](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/README.md).

## Mechanism inspected

The broker checks whether a fill dictionary is present in an executed_fills list but stores only the fill ID. Replayed fills therefore do not match that membership test. [Implementation](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/ccxtbt/ccxtbroker.py#L182-L218).

## Limitation that matters

This is a defect in the inspected adapter, not an operationally proven loss in the house; its exchange and Backtrader versions may differ. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Make fill IDs typed and stable at the adapter boundary; test duplicate fill replay, partial fills and terminal update ordering.

## Why this score

The broker checks whether a fill dictionary is present in an executed_fills list but stores only the fill ID. Replayed fills therefore do not match that membership test. This is a defect in the inspected adapter, not an operationally proven loss in the house; its exchange and Backtrader versions may differ.

## Source trail

[README](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/README.md) · [Implementation](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/ccxtbt/ccxtbroker.py#L182-L218) · [License](https://github.com/neilsmurphy/backtrader_template/blob/ad9311a3e152e8f4781ddd093b02da13cbd50792/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
