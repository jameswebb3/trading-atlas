# novafabric - Attest what a capture contains and what it lost

**Decision question:** Does a signed run prove that all source events were captured?

| Field | Review |
| --- | --- |
| Upstream | [MSKazemi/novafabric](https://github.com/MSKazemi/novafabric) |
| Primary area | Research & Reproducibility |
| Source commit | [eb13e8fa1709010392681e908c883e13a9cd4f9e](https://github.com/MSKazemi/novafabric/commit/eb13e8fa1709010392681e908c883e13a9cd4f9e) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | It counts event streams, reads dropped counts and active hooks, derives a timestamp window, and can sign the assertion against the capsule manifest. Drop counts and capture level come from the producer manifest. If a producer omits an event without reporting it, the signature preserves an incomplete claim. |

## What this project does

NovaFabric packages run evidence and records a separate completeness assertion. [README](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/README.md).

## Mechanism inspected

It counts event streams, reads dropped counts and active hooks, derives a timestamp window, and can sign the assertion against the capsule manifest. [Implementation](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/src/novafabric/evidence/completeness.py#L117-L175). [Related path](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/src/novafabric/evidence/admissibility.py#L159-L183).

## Limitation that matters

Drop counts and capture level come from the producer manifest. If a producer omits an event without reporting it, the signature preserves an incomplete claim. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Separate artifact integrity from coverage, retain source sequence evidence, and mark completeness unknown when independent loss evidence is missing.

## Why this score

The explicit coverage fields improve research auditability, while the producer-only claim needs corroboration.

## Source trail

[README](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/README.md) - [Implementation](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/src/novafabric/evidence/completeness.py#L117-L175) - [Related path](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/src/novafabric/evidence/admissibility.py#L159-L183) - [License](https://github.com/MSKazemi/novafabric/blob/eb13e8fa1709010392681e908c883e13a9cd4f9e/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
