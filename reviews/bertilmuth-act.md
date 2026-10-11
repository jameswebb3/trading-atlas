# Act PBT — Validate each state change

**Decision question:** When should a state-machine property be checked?

| Field | Review |
| --- | --- |
| Upstream | [bertilmuth/act](https://github.com/bertilmuth/act) |
| Primary area | Testing & Verification |
| Source commit | [3552e6a973603374ffd2869daa1f39fa575bf764](https://github.com/bertilmuth/act/commit/3552e6a973603374ffd2869daa1f39fa575bf764) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its PropertyValidator applies every registered property to each change and returns the after-state. A transition check cannot prove that the observed event stream is complete or that an external venue side effect happened. |

## What this project does

A Java property-testing layer for state-machine transitions. [Project README](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/README.md#L1).

## Mechanism inspected

Its PropertyValidator applies every registered property to each change and returns the after-state. [Implementation](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/act-pbt/src/main/java/org/requirementsascode/act/statemachine/pbt/PropertyValidator.java#L19).

## Limitation that matters

A transition check cannot prove that the observed event stream is complete or that an external venue side effect happened. This is a source review, not a runtime or security test.

## Practical check for a trading system

Validate exposure, filled quantity, and terminal-state invariants after every replayed exchange event.

## Why this score

A clear state-transition test pattern, limited by the fidelity of its input events.

## Source trail

[README](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/README.md#L1); [Implementation](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/act-pbt/src/main/java/org/requirementsascode/act/statemachine/pbt/PropertyValidator.java#L19) - [License](https://github.com/bertilmuth/act/blob/3552e6a973603374ffd2869daa1f39fa575bf764/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
