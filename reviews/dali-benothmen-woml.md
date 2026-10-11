# woml - Bind a retry to the original state mutation

**Decision question:** Can a retried write silently become a different operation?

| Field | Review |
| --- | --- |
| Upstream | [dali-benothmen/woml](https://github.com/dali-benothmen/woml) |
| Primary area | Agents & Decision Systems |
| Source commit | [622b47c19a63e73acf573d0bcafefb1b6ce089d5](https://github.com/dali-benothmen/woml/commit/622b47c19a63e73acf573d0bcafefb1b6ce089d5) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Inside an immediate transaction it looks up a prior operation key and compares scope, operation, key and canonical input digest before returning the stored result as a duplicate. Its descriptor says provider idempotency is unsupported. A local state transaction cannot make an external exchange order idempotent. |

## What this project does

WOML provides durable workflow state backed by SQLite and scoped capabilities. [README](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/README.md).

## Mechanism inspected

Inside an immediate transaction it looks up a prior operation key and compares scope, operation, key and canonical input digest before returning the stored result as a duplicate. [Implementation](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/core/woml-engine/src/durable_state.rs#L504-L574). [Related path](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/core/woml-engine/src/durable_state.rs#L312-L326).

## Limitation that matters

Its descriptor says provider idempotency is unsupported. A local state transaction cannot make an external exchange order idempotent. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

For every retried state change, bind the identity to exact input and scope and reject a reused key with changed meaning.

## Why this score

Strong local retry semantics and conflict detection, but exchange effects still require their own reconciliation.

## Source trail

[README](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/README.md) - [Implementation](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/core/woml-engine/src/durable_state.rs#L504-L574) - [Related path](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/core/woml-engine/src/durable_state.rs#L312-L326) - [License](https://github.com/dali-benothmen/woml/blob/622b47c19a63e73acf573d0bcafefb1b6ce089d5/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
