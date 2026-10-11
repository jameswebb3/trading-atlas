# Matflow - Can a scientific input schema reject internally inconsistent records?

**Decision question:** Can a scientific input schema reject internally inconsistent records?

| Field | Review |
| --- | --- |
| Upstream | [hpcflow/matflow](https://github.com/hpcflow/matflow) |
| Primary area | Research & Reproducibility |
| Source commit | [2fec75e60a76dc3598bb57aec6a1205b6432a95b](https://github.com/hpcflow/matflow/commit/2fec75e60a76dc3598bb57aec6a1205b6432a95b) |
| Reviewed | 2026-10-11 |
| Declared license | MPL-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | The loader checks mutually required tensor inputs and validates masked array and numeric shapes. This domain-specific tensor contract does not directly address trading timestamps or market-data coverage. |

## What this project does

A materials-science workflow tool with typed loading parameters.

## Mechanism inspected

The loader checks mutually required tensor inputs and validates masked array and numeric shapes.

## Limitation that matters

This domain-specific tensor contract does not directly address trading timestamps or market-data coverage.

## Practical check for a trading system

Borrow the invariant style for paired fields and shapes, not the materials schema.

## Why this score

1/5. The validation code is concrete but distant from trading-system failure modes.

## Source trail

[README](https://github.com/hpcflow/matflow/blob/2fec75e60a76dc3598bb57aec6a1205b6432a95b/README.md#L1); [matflow/param_classes/load.py](https://github.com/hpcflow/matflow/blob/2fec75e60a76dc3598bb57aec6a1205b6432a95b/matflow/param_classes/load.py#L161); [matflow/param_classes/load.py](https://github.com/hpcflow/matflow/blob/2fec75e60a76dc3598bb57aec6a1205b6432a95b/matflow/param_classes/load.py#L190).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
