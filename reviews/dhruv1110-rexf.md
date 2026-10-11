# Rexf - Can a report choose the best run without a declared primary metric?

**Decision question:** Can a report choose the best run without a declared primary metric?

| Field | Review |
| --- | --- |
| Upstream | [dhruv1110/rexf](https://github.com/dhruv1110/rexf) |
| Primary area | Research & Reproducibility |
| Source commit | [addd64493adf448ff0aa32141d9e189702d64213](https://github.com/dhruv1110/rexf/commit/addd64493adf448ff0aa32141d9e189702d64213) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It treats the maximum as best for every metric and uses the first metric key as the recommendation proxy. Lower-is-better metrics and unordered or mutable metric sets can produce a misleading winner. |

## What this project does

An experiment comparison assistant.

## Mechanism inspected

It treats the maximum as best for every metric and uses the first metric key as the recommendation proxy.

## Limitation that matters

Lower-is-better metrics and unordered or mutable metric sets can produce a misleading winner.

## Practical check for a trading system

Declare metric direction and the primary metric before comparing runs.

## Why this score

2/5. The code makes a concrete metric-selection trap visible.

## Source trail

[README](https://github.com/dhruv1110/rexf/blob/addd64493adf448ff0aa32141d9e189702d64213/README.md#L1); [rexf/intelligence/smart_compare.py](https://github.com/dhruv1110/rexf/blob/addd64493adf448ff0aa32141d9e189702d64213/rexf/intelligence/smart_compare.py#L143); [rexf/intelligence/smart_compare.py](https://github.com/dhruv1110/rexf/blob/addd64493adf448ff0aa32141d9e189702d64213/rexf/intelligence/smart_compare.py#L320); [Root license](https://github.com/dhruv1110/rexf/blob/addd64493adf448ff0aa32141d9e189702d64213/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
