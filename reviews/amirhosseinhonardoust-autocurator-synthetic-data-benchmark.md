# Autocurator - Does synthetic-data coverage measure trading usefulness?

**Decision question:** Does synthetic-data coverage measure trading usefulness?

| Field | Review |
| --- | --- |
| Upstream | [AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark](https://github.com/AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark) |
| Primary area | Data Quality & Lineage |
| Source commit | [8d371f55013648fe1a204fd82fba9ff76a7d6523](https://github.com/AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark/commit/8d371f55013648fe1a204fd82fba9ff76a7d6523) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its k-nearest-neighbor geometry reports precision, recall, density and coverage between real and synthetic samples. Geometric similarity does not validate event ordering, tails, market regimes or executable fills. |

## What this project does

A benchmark for synthetic-data fidelity and coverage.

## Mechanism inspected

Its k-nearest-neighbor geometry reports precision, recall, density and coverage between real and synthetic samples.

## Limitation that matters

Geometric similarity does not validate event ordering, tails, market regimes or executable fills.

## Practical check for a trading system

Assess synthetic tapes against separate timing, tail and execution invariants.

## Why this score

2/5. The multi-axis idea transfers; its geometric score is not a trading validation gate.

## Source trail

[README](https://github.com/AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark/blob/8d371f55013648fe1a204fd82fba9ff76a7d6523/README.md#L1); [src/autocurator/metrics/coverage.py](https://github.com/AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark/blob/8d371f55013648fe1a204fd82fba9ff76a7d6523/src/autocurator/metrics/coverage.py#L23); [Root license](https://github.com/AmirhosseinHonardoust/Autocurator-Synthetic-Data-Benchmark/blob/8d371f55013648fe1a204fd82fba9ff76a7d6523/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
