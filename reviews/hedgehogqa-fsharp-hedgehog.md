# fsharp-hedgehog — Shrink failures without erasing the cause

**Decision question:** Will a reduced counterexample still satisfy its preconditions?

| Field | Review |
| --- | --- |
| Upstream | [fsharp-hedgehog](https://github.com/hedgehogqa/fsharp-hedgehog) |
| Primary area | Testing & Verification |
| Source commit | [a46977278db9a60542e3df3fe0fcd74b90f38ee3](https://github.com/hedgehogqa/fsharp-hedgehog/commit/a46977278db9a60542e3df3fe0fcd74b90f38ee3) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The property runner searches a tree of shrunk outcomes, retains failure status and exposes a shrink path for rechecking. A minimal input is only useful if the economic and order-state preconditions survive reduction. |

## What this project does

A .NET property-testing library with integrated generation and shrinking. [README](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/README.md).

## Mechanism inspected

The property runner searches a tree of shrunk outcomes, retains failure status and exposes a shrink path for rechecking. [Implementation](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/src/Hedgehog/Property.fs#L340-L385).

## Limitation that matters

A minimal input is only useful if the economic and order-state preconditions survive reduction. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep balance, order identity and causal timestamps fixed while shrinking a failing order trace.

## Why this score

Transferable engineering pattern: The property runner searches a tree of shrunk outcomes, retains failure status and exposes a shrink path for rechecking. A minimal input is only useful if the economic and order-state preconditions survive reduction.

## Source trail

[README](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/README.md) · [Documentation](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/docs/articles/getting-started.md) · [Implementation](https://github.com/hedgehogqa/fsharp-hedgehog/blob/a46977278db9a60542e3df3fe0fcd74b90f38ee3/src/Hedgehog/Property.fs#L340-L385).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
