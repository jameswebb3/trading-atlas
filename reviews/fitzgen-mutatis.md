# mutatis — Successful checks can stop before their requested count

**Decision question:** What does success after exhausting a mutation corpus mean?

| Field | Review |
| --- | --- |
| Upstream | [mutatis](https://github.com/fitzgen/mutatis) |
| Primary area | Testing & Verification |
| Source commit | [5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9](https://github.com/fitzgen/mutatis/commit/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT OR Apache-2.0](https://github.com/fitzgen/mutatis/blob/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9/LICENSE-APACHE) |
| Review depth | 3/3: documentation, relevant implementation, and relevant test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The check rejects an initially empty corpus, validates its seeds, then mutates them. This is bounded reachable-input exploration, not a guarantee of the requested mutation count. |

## Project overview

Rust tools for structured input mutation and bounded property checks. [Documentation](https://github.com/fitzgen/mutatis/blob/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9/README.md).

## Mechanism worth inspecting

The check rejects an initially empty corpus, validates its seeds, then mutates them. When all mutators become exhausted, it returns success even if the requested minimum iterations have not been reached. [Source](https://github.com/fitzgen/mutatis/blob/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9/src/check.rs#L527-L595).

## Important limit

This is bounded reachable-input exploration, not a guarantee of the requested mutation count. Minimum bounds otherwise take priority over maximum duration, so a time cap is not always a strict deadline. [Evidence 1](https://github.com/fitzgen/mutatis/blob/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9/src/check.rs#L527-L595). [Evidence 2](https://github.com/fitzgen/mutatis/blob/5bde4ef51e7c1e61a6a595f63bbedf7c68ba13d9/src/check.rs#L722-L757).

## Questions to take into your own design

- Does the receipt record actual mutations, seed checks and exhaustion separately?
- Are deadlines and coverage requirements checked by the admission layer?

## Why this score for a trading system

A precise test-budget implementation and relevant range-preserving shrink tests; it does not establish complete state-space coverage.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. Relevant tests were read, not executed.
