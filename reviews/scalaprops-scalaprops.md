# scalaprops — Property tests need reproducible randomness

**Decision question:** Can a failing generated case be repeated from the same seed and size?

| Field | Review |
| --- | --- |
| Upstream | [scalaprops](https://github.com/scalaprops/scalaprops) |
| Primary area | Testing & Verification |
| Source commit | [6fe57994f3f243b8fd1559f50e1f796fcf263459](https://github.com/scalaprops/scalaprops/commit/6fe57994f3f243b8fd1559f50e1f796fcf263459) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/scalaprops/scalaprops/blob/6fe57994f3f243b8fd1559f50e1f796fcf263459/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The property receives size and Rand, threads the next random state and records falsified or exceptional results. A stable seed reproduces a test input, not the venue's external event order or data snapshot. |

## What this project does

A Scala property-testing library with explicit random state in Property. [README](https://github.com/scalaprops/scalaprops/blob/6fe57994f3f243b8fd1559f50e1f796fcf263459/README.md).

## Mechanism inspected

The property receives size and Rand, threads the next random state and records falsified or exceptional results. [Implementation](https://github.com/scalaprops/scalaprops/blob/6fe57994f3f243b8fd1559f50e1f796fcf263459/core/src/main/scala/scalaprops/Property.scala#L5-L35).

## Limitation that matters

A stable seed reproduces a test input, not the venue's external event order or data snapshot. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Store seed, generator version and event trace in a local failure receipt.

## Why this score

Transferable engineering pattern: The property receives size and Rand, threads the next random state and records falsified or exceptional results. A stable seed reproduces a test input, not the venue's external event order or data snapshot.

## Source trail

[README](https://github.com/scalaprops/scalaprops/blob/6fe57994f3f243b8fd1559f50e1f796fcf263459/README.md) · [Implementation](https://github.com/scalaprops/scalaprops/blob/6fe57994f3f243b8fd1559f50e1f796fcf263459/core/src/main/scala/scalaprops/Property.scala#L5-L35).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
