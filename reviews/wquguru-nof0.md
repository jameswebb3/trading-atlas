# nof0 — A fresh response can contain stale data

**Decision question:** Can a dashboard timestamp make yesterday’s trading snapshot look live?

| Field | Review |
| --- | --- |
| Upstream | [wquguru/nof0](https://github.com/wquguru/nof0) |
| Primary area | Execution & Exchange Integration |
| Source commit | [fe40d850bc47b0941ca215deac65e0c97d8ecd90](https://github.com/wquguru/nof0/commit/fe40d850bc47b0941ca215deac65e0c97d8ecd90) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found; README claims MIT |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | The loader reads account and trade files, then stamps the response with the current server time; its tests check that the timestamp is nonzero. Server response time is not source observation time. |

## What this project does

A crypto and Hyperliquid agent arena with a dashboard backed by stored JSON snapshots. [Project README](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/README.md#L43).

## Mechanism inspected

The loader reads account and trade files, then stamps the response with the current server time; its tests check that the timestamp is nonzero. [Implementation](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/go/internal/data/loader.go#L30). [Related source 1](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/README.md#L158). [Related source 2](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/gitbook/concept/core-workflow.md#L1).

## Limitation that matters

Server response time is not source observation time. A consumer could mistake an old position or trade snapshot for a fresh exchange update. This is a source review, not a runtime or security test.

## Practical check for a trading system

Expose source_observed_at and maximum acceptable age separately from response_time for every feed.

## Why this score

The failure mode maps directly to trading decisions from dashboards and agents, though the arena itself is not a validated strategy.

## Source trail

[README](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/README.md#L43); [Implementation](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/go/internal/data/loader.go#L30); [Related source 1](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/README.md#L158); [Related source 2](https://github.com/wquguru/nof0/blob/fe40d850bc47b0941ca215deac65e0c97d8ecd90/gitbook/concept/core-workflow.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
