# elastic - Align noisy event timestamps to observations

**Decision question:** When two feeds describe the same event at different timestamps, how should offline alignment expose uncertainty?

| Field | Review |
| --- | --- |
| Upstream | [hyunsungkim-ds/elastic](https://github.com/hyunsungkim-ds/elastic) |
| Primary area | Market Data & Ingestion |
| Source commit | [e245224aad7450961eca40954ae2bc85e1e6e696](https://github.com/hyunsungkim-ds/elastic/commit/e245224aad7450961eca40954ae2bc85e1e6e696) |
| Reviewed | 2026-10-10 |
| Declared license | GPL-3.0 ([source](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It maps annotated event time to a nearby frame, searches a bounded candidate window and returns no-match when candidates or scores fail The nearest merge and motion features can use observations after the event; this is an offline reconciliation technique, not a causal live signal or an HL available_at policy |

## What this project does

An offline soccer event-to-tracking synchronizer [README](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/README.md).

## Mechanism inspected

It maps annotated event time to a nearby frame, searches a bounded candidate window and returns no-match when candidates or scores fail [Implementation](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/sync/elastic_greedy.py#L39-L57). [Related path](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/sync/elastic_greedy.py#L112-L135).

## Limitation that matters

The nearest merge and motion features can use observations after the event; this is an offline reconciliation technique, not a causal live signal or an HL available_at policy This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

For delayed market labels, retain original and aligned timestamps, candidate window, score and no-match. Keep the original publication timestamp authoritative for backtests

## Why this score

A specific alignment mechanism with a clear noncausal boundary; useful for diagnostics but not directly deployable

## Source trail

[README](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/README.md) - [Implementation](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/sync/elastic_greedy.py#L39-L57) - [Related path](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/sync/elastic_greedy.py#L112-L135) - [License](https://github.com/hyunsungkim-ds/elastic/blob/e245224aad7450961eca40954ae2bc85e1e6e696/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
