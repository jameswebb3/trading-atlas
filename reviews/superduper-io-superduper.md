# Superduper — Treat a hash match as no change, not validation

**Decision question:** When does a deployed ML component count as the same version?

| Field | Review |
| --- | --- |
| Upstream | [superduper-io/superduper](https://github.com/superduper-io/superduper) |
| Primary area | Research & Reproducibility |
| Source commit | [6d192e7bf255f913b445a44dc9486e7013ddc6bc](https://github.com/superduper-io/superduper/commit/6d192e7bf255f913b445a44dc9486e7013ddc6bc) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The apply path loads the current component and marks it same when the component hash matches, preserving its version. A matching component hash does not identify input data or prove the deployed component is healthy; those need separate provenance and runtime checks. |

## What this project does

A data and AI platform with component application and versioning. [Project README](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/README.md#L1).

## Mechanism inspected

The apply path loads the current component and marks it same when the component hash matches, preserving its version. [Implementation](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/superduper/base/apply.py#L300).

## Limitation that matters

A matching component hash does not identify input data or prove the deployed component is healthy; those need separate provenance and runtime checks. This is a source review, not a runtime or security test.

## Practical check for a trading system

Bind model version to code/config hash and data manifest, then record deployment health independently.

## Why this score

A useful version-comparison pattern, but the platform is far broader than the required contract.

## Source trail

[README](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/README.md#L1); [Implementation](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/superduper/base/apply.py#L300) - [License](https://github.com/superduper-io/superduper/blob/6d192e7bf255f913b445a44dc9486e7013ddc6bc/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
