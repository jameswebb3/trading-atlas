# pmxt - Can cross-venue events be mapped without silently losing a source?

**Decision question:** Can cross-venue events be mapped without silently losing a source?

| Field | Review |
| --- | --- |
| Upstream | [pmxt-dev/pmxt](https://github.com/pmxt-dev/pmxt) |
| Primary area | Market Data & Ingestion |
| Source commit | [4a367d812541154002eedda36b0916a3cf68e0f2](https://github.com/pmxt-dev/pmxt/commit/4a367d812541154002eedda36b0916a3cf68e0f2) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The router maps a normalized series to venue series and fans out event fetches while retaining sourceExchange. A venue fetch exception is logged and converted to an empty list, making incomplete coverage look like an empty result. |

## What this project does

A unified client and router for prediction-market venues.

## Mechanism inspected

The router maps a normalized series to venue series and fans out event fetches while retaining sourceExchange.

## Limitation that matters

A venue fetch exception is logged and converted to an empty list, making incomplete coverage look like an empty result.

## Practical check for a trading system

Emit per-venue coverage and partial-result status with every aggregate event query.

## Why this score

3/5. The cross-venue mapping is concrete; its failure policy must be tightened for evidence-grade datasets.

## Source trail

[README](https://github.com/pmxt-dev/pmxt/blob/4a367d812541154002eedda36b0916a3cf68e0f2/readme.md#L1); [docs/MIGRATE_FROM_DOMEAPI.md](https://github.com/pmxt-dev/pmxt/blob/4a367d812541154002eedda36b0916a3cf68e0f2/docs/MIGRATE_FROM_DOMEAPI.md#L1); [core/src/router/Router.ts](https://github.com/pmxt-dev/pmxt/blob/4a367d812541154002eedda36b0916a3cf68e0f2/core/src/router/Router.ts#L249); [core/src/router/Router.ts](https://github.com/pmxt-dev/pmxt/blob/4a367d812541154002eedda36b0916a3cf68e0f2/core/src/router/Router.ts#L228); [Root license](https://github.com/pmxt-dev/pmxt/blob/4a367d812541154002eedda36b0916a3cf68e0f2/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
