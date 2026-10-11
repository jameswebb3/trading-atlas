# finhack — Missing factor values and errors can become plausible empty outputs

**Decision question:** Can a factor pipeline hide missing market inputs?

| Field | Review |
| --- | --- |
| Upstream | [FinHackCN/finhack](https://github.com/FinHackCN/finhack) |
| Primary area | Signals & Models |
| Source commit | [dedbbd0b7accfed035ba05f07d76726d8754bbf7](https://github.com/FinHackCN/finhack/commit/dedbbd0b7accfed035ba05f07d76726d8754bbf7) |
| Reviewed | 2026-10-09 |
| Declared license | GPL-3.0 ([source](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/LICENSE.txt)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The factor loader fills missing values with zero; on exceptions it logs and returns an empty DataFrame, and callers can treat an empty frame as no result. Zero imputation can create an invented signal state, while error-to-empty collapses data absence and computation failure; stock factors do not transfer directly to HL perps. |

## What this project does

Broad Chinese quant framework for factors, backtests and live integration; README says a rewrite is underway. [README](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/README.md).

## Mechanism inspected

The factor loader fills missing values with zero; on exceptions it logs and returns an empty DataFrame, and callers can treat an empty frame as no result. [Implementation](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/finhack/factor/default/alphaEngine.py#L790-L829).

## Limitation that matters

Zero imputation can create an invented signal state, while error-to-empty collapses data absence and computation failure; stock factors do not transfer directly to HL perps. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep missingness and errors typed separately in feature construction; require available_at and explicit null policy before any alpha preregistration.

## Why this score

The factor loader fills missing values with zero; on exceptions it logs and returns an empty DataFrame, and callers can treat an empty frame as no result. Zero imputation can create an invented signal state, while error-to-empty collapses data absence and computation failure; stock factors do not transfer directly to HL perps.

## Source trail

[README](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/README.md) · [Implementation](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/finhack/factor/default/alphaEngine.py#L790-L829) · [License](https://github.com/FinHackCN/finhack/blob/dedbbd0b7accfed035ba05f07d76726d8754bbf7/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
