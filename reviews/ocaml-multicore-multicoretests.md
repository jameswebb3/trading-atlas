# OCaml Multicore Tests — Check whether concurrent results admit a sequential explanation

**Decision question:** Can observed concurrent results be explained by a valid command order?

| Field | Review |
| --- | --- |
| Upstream | [OCaml Multicore Tests](https://github.com/ocaml-multicore/multicoretests) |
| Primary area | Testing & Verification |
| Source commit | [035edf73c56a9ba5d6e33c660ac6ab3d967c575f](https://github.com/ocaml-multicore/multicoretests/commit/035edf73c56a9ba5d6e33c660ac6ab3d967c575f) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-2-Clause](https://github.com/ocaml-multicore/multicoretests/blob/035edf73c56a9ba5d6e33c660ac6ab3d967c575f/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Lin preserves each branch's command order and searches alternative interleavings against a fresh sequential system. The checker covers generated bounded histories and relies on the reference semantics. |

## Project overview

Property-based tests and reusable concurrency-testing libraries for OCaml runtimes. [Documentation](https://github.com/ocaml-multicore/multicoretests/blob/035edf73c56a9ba5d6e33c660ac6ab3d967c575f/README.md).

## Mechanism worth inspecting

Lin preserves each branch's command order and searches alternative interleavings against a fresh sequential system. Mismatches trigger cleanup; alternative branches reconstruct the tested prefix. [Source](https://github.com/ocaml-multicore/multicoretests/blob/035edf73c56a9ba5d6e33c660ac6ab3d967c575f/lib/lin.ml#L64-L132).

## Important limit

The checker covers generated bounded histories and relies on the reference semantics. It does not prove arbitrary concurrency or establish the timing guarantees of an exchange. [Evidence 1](https://github.com/ocaml-multicore/multicoretests/blob/035edf73c56a9ba5d6e33c660ac6ab3d967c575f/lib/lin.ml#L64-L132).

## Questions to take into your own design

- Which orders of overlapping cancel, fill and replace are legally equivalent?
- Does replay reset state before trying another candidate ordering?

## Why this score for a trading system

A specific portable concurrency-test technique; adopting the OCaml compiler testing stack is outside the useful pattern.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
