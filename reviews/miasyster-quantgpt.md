# QuantGPT — A failed factor must count as failed evidence

**Decision question:** Can a factor disappear from research output without an error count?

| Field | Review |
| --- | --- |
| Upstream | [Miasyster/QuantGPT](https://github.com/Miasyster/QuantGPT) |
| Primary area | Signals & Models |
| Source commit | [db5dc445b5fb298a98dd10a571238b2d94e328fc](https://github.com/Miasyster/QuantGPT/commit/db5dc445b5fb298a98dd10a571238b2d94e328fc) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The factor helper catches any evaluation exception and returns a full NaN series; the signal builder then drops missing values and skips templates with fewer than ten valid observations. This inspected signal path can make a broken factor look merely absent. It is stock-oriented; README performance and cloud validation are not evidence for HL perpetual alpha. |

## What this project does

Agent-driven stock-factor research system with factor evaluation, signal cards and independent cloud validation claims. [README](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/README.md).

## Mechanism inspected

The factor helper catches any evaluation exception and returns a full NaN series; the signal builder then drops missing values and skips templates with fewer than ten valid observations. [Implementation](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/quantgpt/factor_signals.py#L62-L70). [Related implementation](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/quantgpt/factor_signals.py#L123-L141).

## Limitation that matters

This inspected signal path can make a broken factor look merely absent. It is stock-oriented; README performance and cloud validation are not evidence for HL perpetual alpha. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Count attempted, failed and ineligible factors separately before ranking research results; fail closed when missingness crosses a declared threshold.

## Why this score

The factor helper catches any evaluation exception and returns a full NaN series; the signal builder then drops missing values and skips templates with fewer than ten valid observations. This inspected signal path can make a broken factor look merely absent. It is stock-oriented; README performance and cloud validation are not evidence for HL perpetual alpha.

## Source trail

[README](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/README.md) · [Implementation](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/quantgpt/factor_signals.py#L62-L70) · [Related implementation](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/quantgpt/factor_signals.py#L123-L141) · [License](https://github.com/Miasyster/QuantGPT/blob/db5dc445b5fb298a98dd10a571238b2d94e328fc/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
