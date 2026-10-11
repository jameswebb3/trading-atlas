# old-coder - Evidence tied to source state

**Decision question:** Does a passing test report belong to the exact code it claims to cover?

| Field | Review |
| --- | --- |
| Upstream | [AmazingAng/old-coder](https://github.com/AmazingAng/old-coder) |
| Primary area | Testing & Verification |
| Source commit | [a0eb529d393a1cb3ccc564e32b2104e7e75c7a29](https://github.com/AmazingAng/old-coder/commit/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The source-state verifier refuses dirty or untracked Git files, then hashes an explicit source manifest and rechecks HEAD and manifest during hashing Its claimed coverage belongs to the demonstrated project and does not prove a trading invariant; the report itself documents omitted layers and invalid earlier controls |

## What this project does

A software-delivery skill with a worked rate-limiter gauntlet and an evidence report [README](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/README.md).

## Mechanism inspected

The source-state verifier refuses dirty or untracked Git files, then hashes an explicit source manifest and rechecks HEAD and manifest during hashing [Implementation](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/demo-rate-limiter/tools/source_state.py#L73-L180). [Related path](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/demo-rate-limiter/evidence.md#L78-L120).

## Limitation that matters

Its claimed coverage belongs to the demonstrated project and does not prove a trading invariant; the report itself documents omitted layers and invalid earlier controls This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

Require each trading test report to name the exact source commit, test command, failed gate, and negative control. A stale report must not promote a new build

## Why this score

A concrete evidence-binding example; score is limited because the example is not an independent trading validation

## Source trail

[README](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/README.md) - [Implementation](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/demo-rate-limiter/tools/source_state.py#L73-L180) - [Related path](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/demo-rate-limiter/evidence.md#L78-L120) - [License](https://github.com/AmazingAng/old-coder/blob/a0eb529d393a1cb3ccc564e32b2104e7e75c7a29/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
