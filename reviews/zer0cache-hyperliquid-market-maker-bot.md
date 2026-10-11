# Hyperliquid Market Maker Bot — Markout needs warmup and feed health

**Decision question:** When can a maker bot trust its own adverse-selection signal?

| Field | Review |
| --- | --- |
| Upstream | [zer0cache/hyperliquid-market-maker-bot](https://github.com/zer0cache/hyperliquid-market-maker-bot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [49ba15b161eea7edfaebd84f3842f2e697a6e41c](https://github.com/zer0cache/hyperliquid-market-maker-bot/commit/49ba15b161eea7edfaebd84f3842f2e697a6e41c) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Its per-side fill-markout tracker widens quotes after a warmup threshold; execution health records fill polling and position mismatch separately. Markout measured only on the bot’s own fills is selected data. |

## What this project does

A Hyperliquid maker bot with inventory control, side-specific toxicity, and execution reconciliation. [Project README](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/README.md#L24).

## Mechanism inspected

Its per-side fill-markout tracker widens quotes after a warmup threshold; execution health records fill polling and position mismatch separately. [Implementation](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/internal/execution/live.go#L959). [Related source 1](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/docs/ALGORITHM.md#L24). [Related source 2](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/internal/quoting/toxicity.go#L148).

## Limitation that matters

Markout measured only on the bot’s own fills is selected data. A quiet side or stale fill poll can make the estimate appear safe without evidence. This is a source review, not a runtime or security test.

## Practical check for a trading system

Gate adaptive quotes on sample count, fill-feed age, and position reconciliation; report untouched-side uncertainty.

## Why this score

Directly relevant maker-risk mechanics, but no license was located and the signal needs selection-bias controls.

## Source trail

[README](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/README.md#L24); [Implementation](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/internal/execution/live.go#L959); [Related source 1](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/docs/ALGORITHM.md#L24); [Related source 2](https://github.com/zer0cache/hyperliquid-market-maker-bot/blob/49ba15b161eea7edfaebd84f3842f2e697a6e41c/internal/quoting/toxicity.go#L148).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
