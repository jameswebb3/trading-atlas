# Validoopsie - Can a dynamic validator catalog hide which checks ran?

**Decision question:** Can a dynamic validator catalog hide which checks ran?

| Field | Review |
| --- | --- |
| Upstream | [akmalsoliev/Validoopsie](https://github.com/akmalsoliev/Validoopsie) |
| Primary area | Data Quality & Lineage |
| Source commit | [4af82fae466bb032ac0fcc448bbfdce740d61b7b](https://github.com/akmalsoliev/Validoopsie/commit/4af82fae466bb032ac0fcc448bbfdce740d61b7b) |
| Reviewed | 2026-10-11 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It discovers validation classes and accumulates pass/fail status for checks attached to a frame. Dynamic discovery can change the effective rule set unless each run records the resolved validator list and configuration. |

## What this project does

A Python DataFrame validation toolkit.

## Mechanism inspected

It discovers validation classes and accumulates pass/fail status for checks attached to a frame.

## Limitation that matters

Dynamic discovery can change the effective rule set unless each run records the resolved validator list and configuration.

## Practical check for a trading system

Pin the exact checks and severity policy in every quality receipt.

## Why this score

2/5. A useful reminder that a green aggregate is not enough without rule identity.

## Source trail

[README](https://github.com/akmalsoliev/Validoopsie/blob/4af82fae466bb032ac0fcc448bbfdce740d61b7b/README.md#L1); [validoopsie/validate.py](https://github.com/akmalsoliev/Validoopsie/blob/4af82fae466bb032ac0fcc448bbfdce740d61b7b/validoopsie/validate.py#L62); [Root license](https://github.com/akmalsoliev/Validoopsie/blob/4af82fae466bb032ac0fcc448bbfdce740d61b7b/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
