# motherduck-control-tower - Show a stale lineage edge instead of hiding it

**Decision question:** Does a cross-system map reveal a stale or unreadable source account?

| Field | Review |
| --- | --- |
| Upstream | [SDB-Ryan/motherduck-control-tower](https://github.com/SDB-Ryan/motherduck-control-tower) |
| Primary area | Data Quality & Lineage |
| Source commit | [965a7e938ab02597f0634341ce7e2a8b0c2e3b75](https://github.com/SDB-Ryan/motherduck-control-tower/commit/965a7e938ab02597f0634341ce7e2a8b0c2e3b75) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The manifest validator checks typed references and positive stale_hours. During collection, an unavailable or stale shared account becomes an explicit stale-account issue while the rest of the map can still be built. The collector intentionally continues when a shared account is stale or unreadable; users must treat the affected graph segment as incomplete. The implementation is coupled to MotherDuck. |

## What this project does

Control Tower maps MotherDuck objects and run health from a registry-backed manifest. [README](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/README.md).

## Mechanism inspected

The manifest validator checks typed references and positive stale_hours. During collection, an unavailable or stale shared account becomes an explicit stale-account issue while the rest of the map can still be built. [Implementation](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/build-manifest/scripts/_manifest_schema.py#L49-L91). [Related path](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/control-tower-collector/flight.py#L761-L847).

## Limitation that matters

The collector intentionally continues when a shared account is stale or unreadable; users must treat the affected graph segment as incomplete. The implementation is coupled to MotherDuck. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Attach freshness and accessibility state to each source edge and block conclusions that depend on an incomplete segment.

## Why this score

The explicit edge-level stale state is a strong pattern; its warehouse-specific collector and continued partial output limit direct reuse.

## Source trail

[README](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/README.md) - [Implementation](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/build-manifest/scripts/_manifest_schema.py#L49-L91) - [Related path](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/control-tower-collector/flight.py#L761-L847) - [License](https://github.com/SDB-Ryan/motherduck-control-tower/blob/965a7e938ab02597f0634341ce7e2a8b0c2e3b75/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
