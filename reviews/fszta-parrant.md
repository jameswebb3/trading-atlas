# parrant — Four-state policy results preserve why evidence is unknown

**Decision question:** Should a missing check and a broken check produce the same decision?

| Field | Review |
| --- | --- |
| Upstream | [Fszta/parrant](https://github.com/Fszta/parrant) |
| Primary area | Testing & Verification |
| Source commit | [dead7db51edb0bea8d9e2298e49d1a846d6f739a](https://github.com/Fszta/parrant/commit/dead7db51edb0bea8d9e2298e49d1a846d6f739a) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Policy values distinguish UNKNOWN_MISSING from UNKNOWN_ERROR; AND and OR merge causes, and a CI gate maps BLOCK to exit one while WARN and ALLOW pass. The policy algebra is useful only if upstream checks report missing and error honestly; WARN is deliberately nonblocking. |

## What this project does

Lineage policy engine that evaluates evidence into true, false, missing or error states. [README](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/README.md).

## Mechanism inspected

Policy values distinguish UNKNOWN_MISSING from UNKNOWN_ERROR; AND and OR merge causes, and a CI gate maps BLOCK to exit one while WARN and ALLOW pass. [Implementation](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/parrant/lineage/policy.py#L86-L140). [Test source](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/tests/unit/lineage/test_ci_policy_gate.py#L18-L37).

## Limitation that matters

The policy algebra is useful only if upstream checks report missing and error honestly; WARN is deliberately nonblocking. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep missing evidence distinct from failed evaluation in research and release gates; define which states block a weight change.

## Why this score

Policy values distinguish UNKNOWN_MISSING from UNKNOWN_ERROR; AND and OR merge causes, and a CI gate maps BLOCK to exit one while WARN and ALLOW pass. The policy algebra is useful only if upstream checks report missing and error honestly; WARN is deliberately nonblocking.

## Source trail

[README](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/README.md) · [Implementation](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/parrant/lineage/policy.py#L86-L140) · [Test source](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/tests/unit/lineage/test_ci_policy_gate.py#L18-L37) · [License](https://github.com/Fszta/parrant/blob/dead7db51edb0bea8d9e2298e49d1a846d6f739a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
