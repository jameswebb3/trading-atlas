# future-agi - Name the repair window after a handoff gap

**Decision question:** What should an operator see when a committed source batch fails downstream?

| Field | Review |
| --- | --- |
| Upstream | [future-agi/future-agi](https://github.com/future-agi/future-agi) |
| Primary area | Operations & Observability |
| Source commit | [5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813](https://github.com/future-agi/future-agi/commit/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | After a catalog handoff failure it verifies tenant scope and timestamp for each span, groups usable observations into inclusive repair windows, and counts unresolved spans separately. The warning is neither a durable journal nor an automatic backfill. A bad scope or timestamp leaves a case requiring manual investigation. |

## What this project does

Future AGI collects agent traces and maintains an observed catalog for later queries. [README](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/README.md).

## Mechanism inspected

After a catalog handoff failure it verifies tenant scope and timestamp for each span, groups usable observations into inclusive repair windows, and counts unresolved spans separately. [Implementation](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/fi-collector/pkg/observedcatalog/handoff.go#L8-L60). [Related path](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/fi-collector/pkg/traceavailable/publisher.go#L184-L224).

## Limitation that matters

The warning is neither a durable journal nor an automatic backfill. A bad scope or timestamp leaves a case requiring manual investigation. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

At each data handoff, record a bounded repair scope and an explicit unresolved count without treating a warning log as proof of recovery.

## Why this score

The pattern helps incident response, although agent traces and market feeds have different sequence guarantees.

## Source trail

[README](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/README.md) - [Implementation](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/fi-collector/pkg/observedcatalog/handoff.go#L8-L60) - [Related path](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/fi-collector/pkg/traceavailable/publisher.go#L184-L224) - [License](https://github.com/future-agi/future-agi/blob/5b0fb4c8b622b3d07f0f514865e6f8b7f96b9813/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
