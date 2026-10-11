# unit-threaded Property Tests - Can a failing generated test be replayed from its report?

**Decision question:** Can a failing generated test be replayed from its report?

| Field | Review |
| --- | --- |
| Upstream | [atilaneves/unit-threaded](https://github.com/atilaneves/unit-threaded) |
| Primary area | Testing & Verification |
| Source commit | [ae1cbb77353ba6e9441eced6cbd6c11cde96490d](https://github.com/atilaneves/unit-threaded/commit/ae1cbb77353ba6e9441eced6cbd6c11cde96490d) |
| Reviewed | 2026-10-11 |
| Declared license | BSD-3-Clause |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Failure messages include the random seed and input, and single-argument cases can shrink the failing value. This language-specific runner does not encode trading order-state or time-series invariants on its own. |

## What this project does

A property-testing package for the D language.

## Mechanism inspected

Failure messages include the random seed and input, and single-argument cases can shrink the failing value.

## Limitation that matters

This language-specific runner does not encode trading order-state or time-series invariants on its own.

## Practical check for a trading system

Record seed, minimized counterexample and scenario version for every generated trading test.

## Why this score

2/5. The replay receipt is concrete; adapting the package itself is unnecessary.

## Source trail

[README](https://github.com/atilaneves/unit-threaded/blob/ae1cbb77353ba6e9441eced6cbd6c11cde96490d/README.md#L1); [subpackages/property/source/unit_threaded/property.d](https://github.com/atilaneves/unit-threaded/blob/ae1cbb77353ba6e9441eced6cbd6c11cde96490d/subpackages/property/source/unit_threaded/property.d#L22); [subpackages/property/source/unit_threaded/property.d](https://github.com/atilaneves/unit-threaded/blob/ae1cbb77353ba6e9441eced6cbd6c11cde96490d/subpackages/property/source/unit_threaded/property.d#L82); [Root license](https://github.com/atilaneves/unit-threaded/blob/ae1cbb77353ba6e9441eced6cbd6c11cde96490d/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
