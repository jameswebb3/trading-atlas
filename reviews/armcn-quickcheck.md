# quickcheck - Put undefined numeric values into test generators

**Decision question:** Will data validation fail clearly on null, NaN and infinity?

| Field | Review |
| --- | --- |
| Upstream | [armcn/quickcheck](https://github.com/armcn/quickcheck) |
| Primary area | Testing & Verification |
| Source commit | [96178bcf8034130f982bfb36c4293ec133f95c79](https://github.com/armcn/quickcheck/commit/96178bcf8034130f982bfb36c4293ec133f95c79) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/LICENSE.md)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its any_undefined generator deliberately samples NULL, multiple NA types, positive and negative infinity, and NaN as scalar values. This generator does not itself prove that a market-data pipeline rejects or quarantines these values; the trading invariant must be written separately. |

## What this project does

quickcheck is an R property-testing library with combinable data generators. [README](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/README.md).

## Mechanism inspected

Its any_undefined generator deliberately samples NULL, multiple NA types, positive and negative infinity, and NaN as scalar values. [Implementation](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/R/any.R#L269-L291).

## Limitation that matters

This generator does not itself prove that a market-data pipeline rejects or quarantines these values; the trading invariant must be written separately. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

Exercise each undefined numeric class at collection, feature, risk and report boundaries, preserving missingness rather than coercing to zero.

## Why this score

Its any_undefined generator deliberately samples NULL, multiple NA types, positive and negative infinity, and NaN as scalar values. This generator does not itself prove that a market-data pipeline rejects or quarantines these values; the trading invariant must be written separately.

## Source trail

[README](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/README.md) - [Implementation](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/R/any.R#L269-L291) - [License](https://github.com/armcn/quickcheck/blob/96178bcf8034130f982bfb36c4293ec133f95c79/LICENSE.md).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
