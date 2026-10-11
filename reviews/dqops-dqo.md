# DQOps — Keep sensors distinct from threshold rules

**Decision question:** How should a data gate separate measurement from policy?

| Field | Review |
| --- | --- |
| Upstream | [dqops/dqo](https://github.com/dqops/dqo) |
| Primary area | Data Quality & Lineage |
| Source commit | [384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7](https://github.com/dqops/dqo/commit/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7) |
| Reviewed | 2026-10-10 |
| Declared license | Business Source License 1.1 ([source](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | AbstractCheckSpec models a sensor that measures data and separate warning, error, and fatal threshold rules. Its monitoring time scale in the inspected code is daily or monthly, too coarse for minute-level market feeds; the platform has a restrictive Business Source License. |

## What this project does

A data-quality operations platform with table checks, scheduling, dashboards, and incidents. [Project README](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/README.md#L1).

## Mechanism inspected

AbstractCheckSpec models a sensor that measures data and separate warning, error, and fatal threshold rules. [Implementation](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/dqops/src/main/java/com/dqops/checks/AbstractCheckSpec.java#L48). [Related source 1](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/docs/index.md#L25). [Related source 2](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/dqops/src/main/java/com/dqops/checks/CheckTimeScale.java#L16).

## Limitation that matters

Its monitoring time scale in the inspected code is daily or monthly, too coarse for minute-level market feeds; the platform has a restrictive Business Source License. This is a source review, not a runtime or security test.

## Practical check for a trading system

Store observed value, cadence, threshold version, and gate outcome as separate fields.

## Why this score

The measurement-policy split transfers, but its cadence and license make the platform a poor trading dependency.

## Source trail

[README](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/README.md#L1); [Implementation](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/dqops/src/main/java/com/dqops/checks/AbstractCheckSpec.java#L48); [Related source 1](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/docs/index.md#L25); [Related source 2](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/dqops/src/main/java/com/dqops/checks/CheckTimeScale.java#L16) - [License](https://github.com/dqops/dqo/blob/384f79c7b1bc1a0f0a1e6e684ec8c3b2b95986e7/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
