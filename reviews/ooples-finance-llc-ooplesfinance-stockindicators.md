# OoplesFinance.StockIndicators — Preview a bar without committing indicator state

**Decision question:** Can provisional candle updates leave the final indicator state unchanged?

| Field | Review |
| --- | --- |
| Upstream | [Ooples-Finance-LLC/OoplesFinance.StockIndicators](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators) |
| Primary area | Testing & Verification |
| Source commit | [c5a64bf5e6fa6b26894a97f8b2286740c803ffdb](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/commit/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/LICENSE.txt)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | The rolling-deviation state evaluates a provisional value without storing it until isFinal; a source test compares preview, final and clean paths across more than 700 public streaming states. The source test is not a runtime result from our review; the test bars are stock fixtures and cannot prove HL feed timing or every custom indicator. |

## What this project does

High-precision C# indicator library with incremental streaming states. [README](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/README.md).

## Mechanism inspected

The rolling-deviation state evaluates a provisional value without storing it until isFinal; a source test compares preview, final and clean paths across more than 700 public streaming states. [Implementation](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/src/Streaming/RollingStandardDeviationState.cs#L58-L101). [Test source](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/tests/StreamingTests/StreamingPreviewTests.cs#L29-L83).

## Limitation that matters

The source test is not a runtime result from our review; the test bars are stock fixtures and cannot prove HL feed timing or every custom indicator. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For each in-house indicator, compare clean finalized bars with preview-then-final bars and fail on either output or state divergence.

## Why this score

The rolling-deviation state evaluates a provisional value without storing it until isFinal; a source test compares preview, final and clean paths across more than 700 public streaming states. The source test is not a runtime result from our review; the test bars are stock fixtures and cannot prove HL feed timing or every custom indicator.

## Source trail

[README](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/README.md) · [Implementation](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/src/Streaming/RollingStandardDeviationState.cs#L58-L101) · [Test source](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/tests/StreamingTests/StreamingPreviewTests.cs#L29-L83) · [License](https://github.com/Ooples-Finance-LLC/OoplesFinance.StockIndicators/blob/c5a64bf5e6fa6b26894a97f8b2286740c803ffdb/LICENSE.txt).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
