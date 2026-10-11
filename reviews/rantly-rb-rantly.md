# Rantly — Rejected examples are not successful checks

**Decision question:** Does a generator that cannot produce valid cases still pass?

| Field | Review |
| --- | --- |
| Upstream | [Rantly](https://github.com/rantly-rb/rantly) |
| Primary area | Testing & Verification |
| Source commit | [208c0047352e86d25d2bec6a700fd100931a0367](https://github.com/rantly-rb/rantly/commit/208c0047352e86d25d2bec6a700fd100931a0367) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/rantly-rb/rantly/blob/208c0047352e86d25d2bec6a700fd100931a0367/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The property runner counts actual evaluations and raises TooManyTries when generation cannot satisfy its limits. The shrinker catches broad exceptions and does not require the same exception identity. |

## Project overview

Ruby random-data generation and property-checking library. [Documentation](https://github.com/rantly-rb/rantly/blob/208c0047352e86d25d2bec6a700fd100931a0367/README.md).

## Mechanism worth inspecting

The property runner counts actual evaluations and raises TooManyTries when generation cannot satisfy its limits. On failure it retains the original input and may search for a smaller failing value. [Source](https://github.com/rantly-rb/rantly/blob/208c0047352e86d25d2bec6a700fd100931a0367/lib/rantly/property.rb#L29-L81).

## Important limit

The shrinker catches broad exceptions and does not require the same exception identity. A smaller example may therefore fail for a different reason unless the assertion separates failure types. [Evidence 1](https://github.com/rantly-rb/rantly/blob/208c0047352e86d25d2bec6a700fd100931a0367/lib/rantly/property.rb#L29-L81).

## Questions to take into your own design

- Are rejected-generation attempts distinct from executed valid cases?
- Does shrinking preserve the intended invariant violation?

## Why this score for a trading system

Helpful receipt and reduction details in a generic Ruby tester; existing Python property tooling already covers most needs.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
