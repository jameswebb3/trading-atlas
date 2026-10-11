# Nova_funding_hub - Can normalized funding hide venue and symbol assumptions?

**Decision question:** Can normalized funding hide venue and symbol assumptions?

| Field | Review |
| --- | --- |
| Upstream | [SoYuCry/Nova_funding_hub](https://github.com/SoYuCry/Nova_funding_hub) |
| Primary area | Market Data & Ingestion |
| Source commit | [23403f43d7455e1c862d9ffe519b9dac2faf01a3](https://github.com/SoYuCry/Nova_funding_hub/commit/23403f43d7455e1c862d9ffe519b9dac2faf01a3) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Executive assessment | The adapter fetches metaAndAssetCtxs for default and xyz universes, maps symbols and emits a one-hour interval field. The timestamp is local fetch time, symbols are rewritten to USDT-like form and only two universes are queried here. |

## What this project does

A cross-exchange funding comparison service including a Hyperliquid adapter.

## Mechanism inspected

The adapter fetches metaAndAssetCtxs for default and xyz universes, maps symbols and emits a one-hour interval field.

## Limitation that matters

The timestamp is local fetch time, symbols are rewritten to USDT-like form and only two universes are queried here.

## Practical check for a trading system

Keep venue-native asset IDs, source time and explicit universe coverage when comparing funding.

## Why this score

2/5. The adapter exposes useful scope decisions, but its normalized record can misstate provenance.

## Source trail

[README](https://github.com/SoYuCry/Nova_funding_hub/blob/23403f43d7455e1c862d9ffe519b9dac2faf01a3/README.md#L1); [exchanges/hyperliquid.py](https://github.com/SoYuCry/Nova_funding_hub/blob/23403f43d7455e1c862d9ffe519b9dac2faf01a3/exchanges/hyperliquid.py#L50); [Root license](https://github.com/SoYuCry/Nova_funding_hub/blob/23403f43d7455e1c862d9ffe519b9dac2faf01a3/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
