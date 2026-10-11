# EurekAgent — Resume requires artifacts and budget

**Decision question:** Can an agent resume a stage that already exhausted its budget without completing its outputs?

| Field | Review |
| --- | --- |
| Upstream | [THU-Team-Eureka/EurekAgent](https://github.com/THU-Team-Eureka/EurekAgent) |
| Primary area | Agents & Decision Systems |
| Source commit | [fb96df897dfb99797a77623aa0dd9ee178fe89d2](https://github.com/THU-Team-Eureka/EurekAgent/commit/fb96df897dfb99797a77623aa0dd9ee178fe89d2) |
| Reviewed | 2026-10-10 |
| Declared license | AGPL-3.0 ([source](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its resume preflight checks the next stage, elapsed budget, manifest, and required artifacts; exhausted time with invalid artifacts returns a needs-extra-time state. The policy is specific to its research loop and does not validate the scientific result of a completed artifact. |

## What this project does

An autonomous research-agent workflow with persisted stages and budgets. [Project README](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/README.md#L1).

## Mechanism inspected

Its resume preflight checks the next stage, elapsed budget, manifest, and required artifacts; exhausted time with invalid artifacts returns a needs-extra-time state. [Implementation](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/src/resume_preflight.py#L33).

## Limitation that matters

The policy is specific to its research loop and does not validate the scientific result of a completed artifact. This is a source review, not a runtime or security test.

## Practical check for a trading system

On restart, check budget, manifest hash, and required evidence before allowing the next trading study stage.

## Why this score

A concrete fail-closed resume gate for research automation.

## Source trail

[README](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/README.md#L1); [Implementation](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/src/resume_preflight.py#L33) - [License](https://github.com/THU-Team-Eureka/EurekAgent/blob/fb96df897dfb99797a77623aa0dd9ee178fe89d2/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
