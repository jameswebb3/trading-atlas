# FitSpec — Mutation reports need their denominators

**Decision question:** Does a high mutation score establish a complete specification?

| Field | Review |
| --- | --- |
| Upstream | [FitSpec](https://github.com/rudymatela/fitspec) |
| Primary area | Testing & Verification |
| Source commit | [250d610c6c5cbebdac415c8c678ec12a686c2495](https://github.com/rudymatela/fitspec/commit/250d610c6c5cbebdac415c8c678ec12a686c2495) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/rudymatela/fitspec/blob/250d610c6c5cbebdac415c8c678ec12a686c2495/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The engine evaluates mutants against property sets and reports survivors, killed mutants, total mutants, requested test count and whether the mutant generator was exhausted. Survivors and apparent implications are bounded by the generated mutants and cases. |

## Project overview

Haskell tool for identifying surviving function mutants and redundant or incomplete property sets. [Documentation](https://github.com/rudymatela/fitspec/blob/250d610c6c5cbebdac415c8c678ec12a686c2495/README.md).

## Mechanism worth inspecting

The engine evaluates mutants against property sets and reports survivors, killed mutants, total mutants, requested test count and whether the mutant generator was exhausted. [Source](https://github.com/rudymatela/fitspec/blob/250d610c6c5cbebdac415c8c678ec12a686c2495/src/Test/FitSpec/Engine.hs#L101-L165).

## Important limit

Survivors and apparent implications are bounded by the generated mutants and cases. A percentage alone omits the fault universe and cannot prove that all economic invariants are specified. [Evidence 1](https://github.com/rudymatela/fitspec/blob/250d610c6c5cbebdac415c8c678ec12a686c2495/src/Test/FitSpec/Engine.hs#L101-L165).

## Questions to take into your own design

- Are critical surviving mutants listed rather than hidden in a score?
- Do cash conservation, fee sign and fill identity have independent properties?

## Why this score for a trading system

A concrete specification-strength report useful for research and execution contracts; no Haskell adoption is needed.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
