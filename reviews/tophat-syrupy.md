# Syrupy — updating a snapshot is accepting a new baseline

**Decision question:** Can snapshot update mode turn a changed trading report into a passing test?

| Field | Review |
| --- | --- |
| Upstream | [Syrupy](https://github.com/tophat/syrupy) |
| Primary area | Testing & Verification |
| Source commit | [45aaa13005879bfd80e5fbeb90fad7ba65d6c853](https://github.com/tophat/syrupy/commit/45aaa13005879bfd80e5fbeb90fad7ba65d6c853) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/tophat/syrupy/blob/45aaa13005879bfd80e5fbeb90fad7ba65d6c853/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A practical structured-output comparison tool with a clear acceptance boundary. Update mode makes changed snapshots pass after queuing a replacement, so financial invariants and baseline approval need separate checks. |

## Project overview

Syrupy is a pytest snapshot plugin for serialized result comparisons, with filtering and matching extensions. [Project documentation](https://github.com/tophat/syrupy/blob/45aaa13005879bfd80e5fbeb90fad7ba65d6c853/README.md#L11-L22).

## Mechanism worth inspecting

An assertion recalls and compares a serialized baseline. When they differ and update mode is active, it queues the new snapshot and marks the assertion successful. Serialization can include property filters and matchers. [Comparison/update path](https://github.com/tophat/syrupy/blob/45aaa13005879bfd80e5fbeb90fad7ba65d6c853/src/syrupy/assertion.py#L319-L356); [serialization options](https://github.com/tophat/syrupy/blob/45aaa13005879bfd80e5fbeb90fad7ba65d6c853/src/syrupy/assertion.py#L217-L220).

## Important limit

Update mode is a baseline-writing workflow, not independent validation of a changed output. Excluding volatile fields can be useful, but excluding cash, fill prices or timing can hide material changes. Baseline review and financial invariants must remain explicit.

## Questions to take into your own design

- Is snapshot update mode impossible in the ordinary acceptance gate?
- Which excluded fields could change trading semantics despite an unchanged snapshot?

## Why this score for a trading system

3/5: a concrete baseline-acceptance and filtering boundary, useful alongside explicit accounting and causal invariants.

**Scope of this review:** Snapshot assertion, serialization filtering and update behavior; no snapshot suite was executed.
