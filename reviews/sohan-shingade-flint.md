# Flint - Does an empty tick interval mean no trades or a missing recorder?

**Decision question:** Does an empty tick interval mean no trades or a missing recorder?

| Field | Review |
| --- | --- |
| Upstream | [sohan-shingade/flint](https://github.com/sohan-shingade/flint) |
| Primary area | Market Data & Ingestion |
| Source commit | [5ce552c881097f37f38c6ee53146f1b64cb3db95](https://github.com/sohan-shingade/flint/commit/5ce552c881097f37f38c6ee53146f1b64cb3db95) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Executive assessment | Records asserted tick coverage separately from observed rows, preserving quiet markets without hiding recorder gaps. Coverage still depends on the capture process; bar-lane fills use a separate simulation model. |

## What this project does

A Hyperliquid-oriented local trading lab with explicit market-data coverage records and a shared backtest/paper engine.

## Mechanism inspected

CoverageLedger records ingester-asserted time spans, source and funding variant. A span can be covered even with zero rows; deleting data retracts the asserted range. Tick-feed completeness is therefore not inferred from the first and last observed trades.

## Limitation that matters

A coverage assertion is only as reliable as the recorder that writes it. The inspected Nautilus bar lane also uses a synthetic book for fill mirroring and says books are not wired there, so a complete tape does not by itself make bar fills realistic.

## Practical check for a trading system

Treat empty-but-observed intervals and unobserved intervals as different states, with capture provenance attached to every range.

## Why this score

4/5 because The source implements an important direct data-integrity distinction, with clear boundaries at recorder trust and execution fidelity.

## Source trail

[README](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/README.md#L158); [docs/redesign/DESIGN.md](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/docs/redesign/DESIGN.md#L1168); [flint/data/store/coverage.py](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/flint/data/store/coverage.py#L101); [flint/data/store/coverage.py](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/flint/data/store/coverage.py#L119); [flint/engine/nautilus/engine.py](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/flint/engine/nautilus/engine.py#L15); [License text](https://github.com/sohan-shingade/flint/blob/5ce552c881097f37f38c6ee53146f1b64cb3db95/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
