# truthound — Make invalid evidence fail at the JSON boundary

**Decision question:** Can a report contract reject unknown fields, implicit coercions and unbounded payloads?

| Field | Review |
| --- | --- |
| Upstream | [seadonggyun4/truthound](https://github.com/seadonggyun4/truthound) |
| Primary area | Data Quality & Lineage |
| Source commit | [fd94a2100088fd7ed0b3ad6e1817bd24ee986637](https://github.com/seadonggyun4/truthound/commit/fd94a2100088fd7ed0b3ad6e1817bd24ee986637) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its decoder rejects extra or missing fields, validates exact primitive types, bounds strings/items/integers, and reports stable error codes with JSON pointers. Strictness is valuable for evidence records but an incompatible schema rollout can reject old records; migration and versioning are needed. |

## What this project does

Data-quality tool with a strict schema-audit JSON contract. [README](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/README.md).

## Mechanism inspected

Its decoder rejects extra or missing fields, validates exact primitive types, bounds strings/items/integers, and reports stable error codes with JSON pointers. [Implementation](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/src/truthound/schema_audit/_contract.py#L12-L111).

## Limitation that matters

Strictness is valuable for evidence records but an incompatible schema rollout can reject old records; migration and versioning are needed. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Treat ledger and report inputs as versioned typed records; reject unknown fields and non-finite or coerced values before any scoring.

## Why this score

Its decoder rejects extra or missing fields, validates exact primitive types, bounds strings/items/integers, and reports stable error codes with JSON pointers. Strictness is valuable for evidence records but an incompatible schema rollout can reject old records; migration and versioning are needed.

## Source trail

[README](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/README.md) · [Implementation](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/src/truthound/schema_audit/_contract.py#L12-L111) · [License](https://github.com/seadonggyun4/truthound/blob/fd94a2100088fd7ed0b3ad6e1817bd24ee986637/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
