# Hyperliquid-Data-Layer-API - Is a convenient historical endpoint enough to prove data completeness?

**Decision question:** Is a convenient historical endpoint enough to prove data completeness?

| Field | Review |
| --- | --- |
| Upstream | [moondevonyt/Hyperliquid-Data-Layer-API](https://github.com/moondevonyt/Hyperliquid-Data-Layer-API) |
| Primary area | Market Data & Ingestion |
| Source commit | [bffd370cde88082a1e85772f2fabaf312a0a9014](https://github.com/moondevonyt/Hyperliquid-Data-Layer-API/commit/bffd370cde88082a1e85772f2fabaf312a0a9014) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Executive assessment | The client sends authenticated GET requests to a hosted base URL and returns parsed endpoint responses. The inspected wrapper does not expose collection provenance, coverage gaps or source timestamps for each record; no root license was verified. |

## What this project does

A client wrapper for a hosted Hyperliquid data API covering liquidations, positions and other endpoints.

## Mechanism inspected

The client sends authenticated GET requests to a hosted base URL and returns parsed endpoint responses.

## Limitation that matters

The inspected wrapper does not expose collection provenance, coverage gaps or source timestamps for each record; no root license was verified.

## Practical check for a trading system

Treat hosted responses as unverified external data until a separate coverage and origin audit is available.

## Why this score

1/5. The topic is relevant, but the wrapper does not solve evidence quality and adds SaaS dependence.

## Source trail

[README](https://github.com/moondevonyt/Hyperliquid-Data-Layer-API/blob/bffd370cde88082a1e85772f2fabaf312a0a9014/README.md#L1); [docs/polymarket-profitable-traders.md](https://github.com/moondevonyt/Hyperliquid-Data-Layer-API/blob/bffd370cde88082a1e85772f2fabaf312a0a9014/docs/polymarket-profitable-traders.md#L1); [api.py](https://github.com/moondevonyt/Hyperliquid-Data-Layer-API/blob/bffd370cde88082a1e85772f2fabaf312a0a9014/api.py#L159).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
