# Valthree — A failed write can have taken effect

**Decision question:** Can consistency checks model a write with an uncertain outcome?

| Field | Review |
| --- | --- |
| Upstream | [Valthree](https://github.com/antithesishq/valthree) |
| Primary area | Testing & Verification |
| Source commit | [eac10247e308270f316259e50c0bfc9e992137d1](https://github.com/antithesishq/valthree/commit/eac10247e308270f316259e50c0bfc9e992137d1) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The property-test model allows both unchanged and changed state after a failed write. Partitioning works here because the model is per key; financial transfers or cross-order constraints may couple keys. |

## Project overview

Demonstration of a strongly consistent Valkey-compatible database using object storage; its README advises against production reliance. [Documentation](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/README.md).

## Mechanism worth inspecting

The property-test model allows both unchanged and changed state after a failed write. The checker partitions histories by key and distinguishes a consistency violation from verification timeout. [Source](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/internal/proptest/proptest.go#L121-L156).

## Important limit

Partitioning works here because the model is per key; financial transfers or cross-order constraints may couple keys. The repository is explicitly a testing demonstration, not a production database recommendation. [Evidence 1](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/internal/proptest/proptest.go#L121-L156). [Evidence 2](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/internal/proptest/proptest.go#L159-L210). [Evidence 3](https://github.com/antithesishq/valthree/blob/eac10247e308270f316259e50c0bfc9e992137d1/README.md#L9-L12).

## Questions to take into your own design

- Does a failed write leave both outcomes possible until evidence resolves it?
- Can histories be partitioned without discarding shared cash or position constraints?

## Why this score for a trading system

A strong transferable reference for uncertainty and bounded consistency checking; its database and commercial testing platform are not needed for local fixtures.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
