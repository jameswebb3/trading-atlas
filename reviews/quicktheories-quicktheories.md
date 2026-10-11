# QuickTheories — What evidence survives when shrinking reaches its budget

**Decision question:** What evidence survives when shrinking reaches its budget?

| Field | Review |
| --- | --- |
| Upstream | [QuickTheories](https://github.com/quicktheories/QuickTheories) |
| Primary area | Testing & Verification |
| Source commit | [a963eded0604ab9fe1950611a64807851d790c1c](https://github.com/quicktheories/QuickTheories/commit/a963eded0604ab9fe1950611a64807851d790c1c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/quicktheories/QuickTheories/blob/a963eded0604ab9fe1950611a64807851d790c1c/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful property-testing reference for bounded shrinking and visible assumption exhaustion. Keep both the original failing input and the reduced example; the reported minimum depends on the generator and search budget. |

## Project overview

QuickTheories is a Java property-testing library with composable generators, fixed seeds and automatic shrinking. [Project documentation](https://github.com/quicktheories/QuickTheories/blob/a963eded0604ab9fe1950611a64807851d790c1c/README.md#L1-L23).

## Mechanism worth inspecting

The shrink loop limits cycles, rejects duplicate candidates or candidates with more failed assumptions, and preserves discovered counterexamples if generation attempts are exhausted. [Shrink loop](https://github.com/quicktheories/QuickTheories/blob/a963eded0604ab9fe1950611a64807851d790c1c/core/src/main/java/org/quicktheories/impl/Core.java#L96-L130). Documentation makes low acceptance of assumptions an explicit error. [Assumption policy](https://github.com/quicktheories/QuickTheories/blob/a963eded0604ab9fe1950611a64807851d790c1c/README.md#L203-L223).

## Important limit

A smallest found example is relative to this search and budget, not proof of a globally minimal failure. A seed also needs the generator, code and configuration version to remain reproducible.

## Questions to take into your own design

- What evidence survives when shrinking reaches its budget?
- Are original inputs, reduced counterexamples and generator versions stored together?

## Why this score for a trading system

3/5: concrete transferable counterexample handling; it does not provide trading invariants or event coverage by itself.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
