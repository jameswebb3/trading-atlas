# qcstm — Shrink order-event sequences without breaking their preconditions

**Decision question:** Can a failing order-state sequence be reduced to the smallest valid replay?

| Field | Review |
| --- | --- |
| Upstream | [jmid/qcstm](https://github.com/jmid/qcstm) |
| Primary area | Testing & Verification |
| Source commit | [352ca8def568f398ad0e6188db425e9b178a5534](https://github.com/jmid/qcstm/commit/352ca8def568f398ad0e6188db425e9b178a5534) |
| Reviewed | 2026-10-09 |
| Declared license | BSD-style ([source](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/LICENCE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A command generator depends on model state; the list shrinker is filtered by preconditions before comparison with the system under test, so a reduced counterexample remains a valid sequence. The library models sequential commands, while exchange ACK/fill/cancel interleavings and restart need explicit asynchronous event modeling; no direct HL adapter is included. |

## What this project does

Small OCaml state-machine property-testing layer on QCheck. [README](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/README.md).

## Mechanism inspected

A command generator depends on model state; the list shrinker is filtered by preconditions before comparison with the system under test, so a reduced counterexample remains a valid sequence. [Implementation](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/src/qCSTM.ml#L14-L47). [Related implementation](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/src/qCSTM.ml#L65-L116).

## Limitation that matters

The library models sequential commands, while exchange ACK/fill/cancel interleavings and restart need explicit asynchronous event modeling; no direct HL adapter is included. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Generate valid submit, ACK, partial-fill, cancel and restart histories, then shrink failures while preserving causal preconditions and the recorded event order.

## Why this score

A command generator depends on model state; the list shrinker is filtered by preconditions before comparison with the system under test, so a reduced counterexample remains a valid sequence. The library models sequential commands, while exchange ACK/fill/cancel interleavings and restart need explicit asynchronous event modeling; no direct HL adapter is included.

## Source trail

[README](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/README.md) · [Implementation](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/src/qCSTM.ml#L14-L47) · [Related implementation](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/src/qCSTM.ml#L65-L116) · [License](https://github.com/jmid/qcstm/blob/352ca8def568f398ad0e6188db425e9b178a5534/LICENCE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
