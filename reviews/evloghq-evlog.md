# evlog - Redact on policy failure, but verify logging was initialized

**Decision question:** Can a broken redaction callback leak a sensitive field?

| Field | Review |
| --- | --- |
| Upstream | [evloghq/evlog](https://github.com/evloghq/evlog) |
| Primary area | Operations & Observability |
| Source commit | [1b6e1b92531309fec393a210db9494f901190383](https://github.com/evloghq/evlog/commit/1b6e1b92531309fec393a210db9494f901190383) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | A matched field is replaced with a fixed marker when its redaction callback throws or returns a non-string value. The logger applies configured redaction before emitting the formatted event. Its own fallback path warns that a production process without initLogger emits with no redaction and no drain. Correct per-field fallback does not secure an uninitialized logging pipeline. |

## What this project does

evlog emits structured, wide application events and supports recursive field redaction. [README](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/README.md).

## Mechanism inspected

A matched field is replaced with a fixed marker when its redaction callback throws or returns a non-string value. The logger applies configured redaction before emitting the formatted event. [Implementation](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/src/redact.ts#L102-L164). [Related path](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/src/logger.ts#L249-L310).

## Limitation that matters

Its own fallback path warns that a production process without initLogger emits with no redaction and no drain. Correct per-field fallback does not secure an uninitialized logging pipeline. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Fail startup if required redaction and durable drain are absent. Exercise a throwing redactor and verify the sensitive value never reaches the sink.

## Why this score

The failure-safe replacement is concrete, but configuration coverage and event durability must be checked separately.

## Source trail

[README](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/README.md) - [Implementation](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/src/redact.ts#L102-L164) - [Related path](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/packages/evlog/src/logger.ts#L249-L310) - [License](https://github.com/evloghq/evlog/blob/1b6e1b92531309fec393a210db9494f901190383/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
