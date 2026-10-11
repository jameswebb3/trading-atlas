# simmer-sdk - Do Hyperliquid order fields imply the same product?

**Decision question:** Do Hyperliquid order fields imply the same product?

| Field | Review |
| --- | --- |
| Upstream | [SpartanLabsXyz/simmer-sdk](https://github.com/SpartanLabsXyz/simmer-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [318d4b70a06f88ae288983deb60c18b4dfe26d7c](https://github.com/SpartanLabsXyz/simmer-sdk/commit/318d4b70a06f88ae288983deb60c18b4dfe26d7c) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Executive assessment | It builds signed YES/NO outcome orders with TIF, reduce-only and optional CLOID. HIP-4 outcome contracts are not USDC perpetuals; price domain and asset IDs differ. |

## What this project does

A multi-venue prediction-market SDK with a Hyperliquid HIP-4 adapter.

## Mechanism inspected

It builds signed YES/NO outcome orders with TIF, reduce-only and optional CLOID.

## Limitation that matters

HIP-4 outcome contracts are not USDC perpetuals; price domain and asset IDs differ.

## Practical check for a trading system

Keep product type and asset namespace explicit in exchange adapters.

## Why this score

2/5. Concrete envelope, outside perps alpha.

## Source trail

[README](https://github.com/SpartanLabsXyz/simmer-sdk/blob/318d4b70a06f88ae288983deb60c18b4dfe26d7c/README.md#L1); [simmer_sdk/hyperliquid_venue.py](https://github.com/SpartanLabsXyz/simmer-sdk/blob/318d4b70a06f88ae288983deb60c18b4dfe26d7c/simmer_sdk/hyperliquid_venue.py#L138); [Root license](https://github.com/SpartanLabsXyz/simmer-sdk/blob/318d4b70a06f88ae288983deb60c18b4dfe26d7c/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
