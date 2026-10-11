# Bombadil — Generate hostile inputs from the interface contract

**Decision question:** How can a command surface be probed for unexpected accepted inputs?

| Field | Review |
| --- | --- |
| Upstream | [antithesishq/bombadil](https://github.com/antithesishq/bombadil) |
| Primary area | Testing & Verification |
| Source commit | [26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c](https://github.com/antithesishq/bombadil/commit/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/LICENCE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The generator samples typed strings, including constrained formats such as email-like input, and explores what the target accepts. Acceptance of generated input is not correctness. |

## What this project does

A specification-driven generator for interface and terminal testing. [Project README](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/README.md#L3).

## Mechanism inspected

The generator samples typed strings, including constrained formats such as email-like input, and explores what the target accepts. [Implementation](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/lib/bombadil/src/specification/generators.rs#L99).

## Limitation that matters

Acceptance of generated input is not correctness. The generator must be paired with an oracle for order size, symbol namespace, and risk-state semantics. This is a source review, not a runtime or security test.

## Practical check for a trading system

Fuzz order commands with malformed symbols, identifiers, decimal formats, and stale timestamps, then assert rejection or canonicalization.

## Why this score

Useful as a test-design reference, but the project is experimental and does not supply a trading oracle.

## Source trail

[README](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/README.md#L3); [Implementation](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/lib/bombadil/src/specification/generators.rs#L99) - [License](https://github.com/antithesishq/bombadil/blob/26bdbb53cc3a32a5e9092baa13c1fb234ab95c7c/LICENCE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
