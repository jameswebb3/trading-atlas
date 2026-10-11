# Prediction-Markets-Trading-Bot-Toolkits - Should a burst of large trades pause a strategy before an order?

**Decision question:** Should a burst of large trades pause a strategy before an order?

| Field | Review |
| --- | --- |
| Upstream | [HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits) |
| Primary area | Portfolio & Risk |
| Source commit | [b8a31fbedfa03554475e794691f72dea53f91dd9](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits/commit/b8a31fbedfa03554475e794691f72dea53f91dd9) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | An in-memory fast gate counts large trades in a time window, then requests a book-depth check and trips for insufficient depth. The trip history is process-local and a failed book fetch requires the caller to invoke trip explicitly. |

## What this project does

Prediction-market bot infrastructure with eligibility and risk gates.

## Mechanism inspected

An in-memory fast gate counts large trades in a time window, then requests a book-depth check and trips for insufficient depth.

## Limitation that matters

The trip history is process-local and a failed book fetch requires the caller to invoke trip explicitly.

## Practical check for a trading system

Make the pre-trade gate fail closed on missing book evidence and persist trip state if a restart must not clear it.

## Why this score

3/5. The two-stage gate is concrete but needs stronger failure and restart semantics.

## Source trail

[README](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits/blob/b8a31fbedfa03554475e794691f72dea53f91dd9/README.md#L1); [src/service/risk_guard.rs](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits/blob/b8a31fbedfa03554475e794691f72dea53f91dd9/src/service/risk_guard.rs#L59); [Root license](https://github.com/HarrierOnChain/Prediction-Markets-Trading-Bot-Toolkits/blob/b8a31fbedfa03554475e794691f72dea53f91dd9/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
