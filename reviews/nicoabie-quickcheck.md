# QuickCheck for Prolog - When can a shrinker stop before finding the smallest counterexample?

**Decision question:** When can a shrinker stop before finding the smallest counterexample?

| Field | Review |
| --- | --- |
| Upstream | [nicoabie/quickcheck](https://github.com/nicoabie/quickcheck) |
| Primary area | Testing & Verification |
| Source commit | [87dddf9ea75842b2534a7743b6340cd91235d5f5](https://github.com/nicoabie/quickcheck/commit/87dddf9ea75842b2534a7743b6340cd91235d5f5) |
| Reviewed | 2026-10-11 |
| Declared license | Unlicense |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | A failed example is recursively shrunk while the property still fails, with a depth cap of 32. The depth cap and local reduction do not guarantee a globally minimal example or replay of an exchange event sequence. |

## What this project does

A property-testing implementation in Prolog.

## Mechanism inspected

A failed example is recursively shrunk while the property still fails, with a depth cap of 32.

## Limitation that matters

The depth cap and local reduction do not guarantee a globally minimal example or replay of an exchange event sequence.

## Practical check for a trading system

Preserve the original failing tape as well as the simplified case.

## Why this score

2/5. The bounded shrinking mechanism is a useful testing reference, not a trading test suite.

## Source trail

[README](https://github.com/nicoabie/quickcheck/blob/87dddf9ea75842b2534a7743b6340cd91235d5f5/README.md#L1); [prolog/quickcheck.pl](https://github.com/nicoabie/quickcheck/blob/87dddf9ea75842b2534a7743b6340cd91235d5f5/prolog/quickcheck.pl#L110); [prolog/quickcheck.pl](https://github.com/nicoabie/quickcheck/blob/87dddf9ea75842b2534a7743b6340cd91235d5f5/prolog/quickcheck.pl#L170); [Root license](https://github.com/nicoabie/quickcheck/blob/87dddf9ea75842b2534a7743b6340cd91235d5f5/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
