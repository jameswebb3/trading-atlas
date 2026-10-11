# SmallCheck — Exhaustive means exhaustive within a bound

**Decision question:** What does checking every small case leave out?

| Field | Review |
| --- | --- |
| Upstream | [SmallCheck](https://github.com/Bodigrim/smallcheck) |
| Primary area | Testing & Verification |
| Source commit | [433ada587bf4ff898031aaa5530c0b7aaab10e3a](https://github.com/Bodigrim/smallcheck/commit/433ada587bf4ff898031aaa5530c0b7aaab10e3a) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Series constructors consume a depth budget, while limit truncates the generated series to its first n values. Depth, constructor definitions, filters and element limits determine the universe checked. |

## Project overview

Haskell property testing through bounded enumeration; its README describes the library as largely obsolete. [Documentation](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/README.md).

## Mechanism worth inspecting

Series constructors consume a depth budget, while limit truncates the generated series to its first n values. Filtering removes cases that do not satisfy a predicate. [Source](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/Test/SmallCheck/Series.hs#L284-L298).

## Important limit

Depth, constructor definitions, filters and element limits determine the universe checked. Exhaustive small cases are not exhaustive program states, and a zero depth can yield no generated values. [Evidence 1](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/Test/SmallCheck/Series.hs#L284-L298). [Evidence 2](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/Test/SmallCheck/Series.hs#L379-L434). [Evidence 3](https://github.com/Bodigrim/smallcheck/blob/433ada587bf4ff898031aaa5530c0b7aaab10e3a/README.md#L4-L10).

## Questions to take into your own design

- Are both enumeration depth and generated-case count in the receipt?
- Which important cases do filtering and truncation remove?

## Why this score for a trading system

A useful bounded-exploration idea in a library its own maintainers now regard as obsolete; there is no reason to adopt it for new infrastructure.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
