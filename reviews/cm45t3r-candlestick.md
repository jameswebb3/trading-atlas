# candlestick — Missing trend context is scored as full fit

**Decision question:** How does a candlestick classifier treat absent prior trend?

| Field | Review |
| --- | --- |
| Upstream | [cm45t3r/candlestick](https://github.com/cm45t3r/candlestick) |
| Primary area | Signals & Models |
| Source commit | [7b7c45708c8366c0cb9c256044cf24e13cfb16fb](https://github.com/cm45t3r/candlestick/commit/7b7c45708c8366c0cb9c256044cf24e13cfb16fb) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | It derives expected prior trend from reversal versus continuation metadata, then returns context-fit 1 when measured trend is absent or NaN; a test asserts that behavior. Missing context is treated as no penalty, not unknown; a pattern label or fit score is not evidence of HL-perp predictiveness. |

## What this project does

JavaScript candlestick pattern detector with trend-context scoring. [README](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/README.md).

## Mechanism inspected

It derives expected prior trend from reversal versus continuation metadata, then returns context-fit 1 when measured trend is absent or NaN; a test asserts that behavior. [Implementation](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/src/contextFit.js#L25-L64). [Test source](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/test/contextFit.test.js#L72-L82).

## Limitation that matters

Missing context is treated as no penalty, not unknown; a pattern label or fit score is not evidence of HL-perp predictiveness. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Keep insufficient history as an explicit unavailable state when testing pattern features; do not equate shape detection with alpha.

## Why this score

It derives expected prior trend from reversal versus continuation metadata, then returns context-fit 1 when measured trend is absent or NaN; a test asserts that behavior. Missing context is treated as no penalty, not unknown; a pattern label or fit score is not evidence of HL-perp predictiveness.

## Source trail

[README](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/README.md) · [Implementation](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/src/contextFit.js#L25-L64) · [Test source](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/test/contextFit.test.js#L72-L82) · [License](https://github.com/cm45t3r/candlestick/blob/7b7c45708c8366c0cb9c256044cf24e13cfb16fb/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
