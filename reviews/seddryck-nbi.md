# NBi — Tolerances express a comparison contract

**Decision question:** Does a relative tolerance behave sensibly near zero?

| Field | Review |
| --- | --- |
| Upstream | [NBi](https://github.com/Seddryck/NBi) |
| Primary area | Testing & Verification |
| Source commit | [5946c75702320267339d6f9d61a821d1f34435f7](https://github.com/Seddryck/NBi/commit/5946c75702320267339d6f9d61a821d1f34435f7) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/Seddryck/NBi/blob/5946c75702320267339d6f9d61a821d1f34435f7/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | NumericComparer distinguishes absolute, percentage and bounded-percentage tolerances. A percentage tolerance with expected value zero becomes exact equality. |

## Project overview

Declarative testing framework for relational data, business-intelligence and ETL systems. [Documentation](https://github.com/Seddryck/NBi/blob/5946c75702320267339d6f9d61a821d1f34435f7/Readme.md).

## Mechanism worth inspecting

NumericComparer distinguishes absolute, percentage and bounded-percentage tolerances. Percentage tolerance scales by the expected value, while the comparison can enforce either or both sides. [Source](https://github.com/Seddryck/NBi/blob/5946c75702320267339d6f9d61a821d1f34435f7/NBi.Core/Scalar/Comparer/NumericComparer.cs#L114-L180).

## Important limit

A percentage tolerance with expected value zero becomes exact equality. A tolerance that ignores monetary units or permitted direction can conceal meaningful reconciliation differences. [Evidence 1](https://github.com/Seddryck/NBi/blob/5946c75702320267339d6f9d61a821d1f34435f7/NBi.Core/Scalar/Comparer/NumericComparer.cs#L114-L180).

## Questions to take into your own design

- Are quantity, cash and price compared using their own units?
- Are zero baselines and one-sided tolerances explicit in the test?

## Why this score for a trading system

A portable comparison contract for financial replay tests; adopting the XML/.NET testing stack is unnecessary.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
