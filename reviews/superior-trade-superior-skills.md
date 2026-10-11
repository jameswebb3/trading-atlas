# superior-skills - Audit trading instructions against a pinned API contract

**Decision question:** Can trading docs teach an endpoint that the current API contract no longer exposes?

| Field | Review |
| --- | --- |
| Upstream | [Superior-Trade/superior-skills](https://github.com/Superior-Trade/superior-skills) |
| Primary area | Testing & Verification |
| Source commit | [9d41db54b231f77e35610a73230eaeffcb456215](https://github.com/Superior-Trade/superior-skills/commit/9d41db54b231f77e35610a73230eaeffcb456215) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A script extracts explicit HTTP method/path claims from skills and docs, normalizes path parameters, and fails if a claim is absent from the committed OpenAPI snapshot or references a legacy route. The regular-expression scan only sees explicit endpoint claims, and a stale snapshot can give false reassurance; it checks route existence, not payload, error or live behavior. |

## What this project does

Superior Skills contains trading-agent workflows and a snapshot of its Unified API contract. [README](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/README.md).

## Mechanism inspected

A script extracts explicit HTTP method/path claims from skills and docs, normalizes path parameters, and fails if a claim is absent from the committed OpenAPI snapshot or references a legacy route. [Implementation](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/scripts/audit-endpoints.mjs#L45-L126). [Related path](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/scripts/endpoint-claims.mjs#L1-L46).

## Limitation that matters

The regular-expression scan only sees explicit endpoint claims, and a stale snapshot can give false reassurance; it checks route existence, not payload, error or live behavior. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

For exchange/runbook documentation, compare documented operations to a dated contract snapshot and retain a separate producer/replay integration test for behavior.

## Why this score

A script extracts explicit HTTP method/path claims from skills and docs, normalizes path parameters, and fails if a claim is absent from the committed OpenAPI snapshot or references a legacy route. The regular-expression scan only sees explicit endpoint claims, and a stale snapshot can give false reassurance; it checks route existence, not payload, error or live behavior.

## Source trail

[README](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/README.md) - [Implementation](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/scripts/audit-endpoints.mjs#L45-L126) - [Related path](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/scripts/endpoint-claims.mjs#L1-L46) - [License](https://github.com/Superior-Trade/superior-skills/blob/9d41db54b231f77e35610a73230eaeffcb456215/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
