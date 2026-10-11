# Kea2 — UI property tests do not replace venue tests

**Decision question:** Can a test harness record a caller and configuration before exploring a UI?

| Field | Review |
| --- | --- |
| Upstream | [Kea2](https://github.com/ecnusse/Kea2) |
| Primary area | Testing & Verification |
| Source commit | [a294f566527aacf629a0793c53e70fb020824d0e](https://github.com/ecnusse/Kea2/commit/a294f566527aacf629a0793c53e70fb020824d0e) |
| Reviewed | 2026-10-06 |
| Declared license | [Kea2 Revised License (restricted redistribution)](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | The Python API validates that its config directory exists and returns structured run results with caller metadata. The target is a mobile UI, and its SDK license restricts redistribution; there is no direct HL execution value. |

## What this project does

An Android UI property-testing harness with a custom restrictive license. [README](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/README.md).

## Mechanism inspected

The Python API validates that its config directory exists and returns structured run results with caller metadata. [Implementation](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/kea2/kea2_api.py#L32-L87).

## Limitation that matters

The target is a mobile UI, and its SDK license restricts redistribution; there is no direct HL execution value. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not adopt; keep caller/config identity as a generic reminder for test receipts.

## Why this score

Indirect relevance only: The Python API validates that its config directory exists and returns structured run results with caller metadata. The target is a mobile UI, and its SDK license restricts redistribution; there is no direct HL execution value.

## Source trail

[README](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/README.md) · [Documentation](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/docs/manual_en.md) · [Implementation](https://github.com/ecnusse/Kea2/blob/a294f566527aacf629a0793c53e70fb020824d0e/kea2/kea2_api.py#L32-L87).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
