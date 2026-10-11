# A.M.Y - Reject self-reported scientific proof

**Decision question:** When is an agent result evidence instead of just a success flag?

| Field | Review |
| --- | --- |
| Upstream | [Ganador1/A.M.Y](https://github.com/Ganador1/A.M.Y) |
| Primary area | Agents & Decision Systems |
| Source commit | [a7abba9f7d804a8e3bda42608072cc2574e1953a](https://github.com/Ganador1/A.M.Y/commit/a7abba9f7d804a8e3bda42608072cc2574e1953a) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/LICENSE)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Known certificate types are parsed, hashed, bound to expected inputs and passed to domain handlers; legacy outputs with self-reported proof flags remain unsupported A hash authenticates bytes, not the scientific claim. Only the named, independently checked certificate types can be treated as verified |

## What this project does

An autonomous research-agent system with certificate checking [README](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/README.md).

## Mechanism inspected

Known certificate types are parsed, hashed, bound to expected inputs and passed to domain handlers; legacy outputs with self-reported proof flags remain unsupported [Implementation](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/core/scientific_certificate_checks.py#L369-L417). [Related path](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/core/memory_checkpoint.py#L7-L31).

## Limitation that matters

A hash authenticates bytes, not the scientific claim. Only the named, independently checked certificate types can be treated as verified This review covers the pinned source paths, not independent runtime behavior.

## Practical check for a trading system

For each research-agent result, record input binding, verifier identity, unsupported status and raw artifact hash before it can influence a study decision

## Why this score

A precise fail-closed distinction between producer success and checked evidence; domain checkers themselves are outside trading

## Source trail

[README](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/README.md) - [Implementation](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/core/scientific_certificate_checks.py#L369-L417) - [Related path](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/core/memory_checkpoint.py#L7-L31) - [License](https://github.com/Ganador1/A.M.Y/blob/a7abba9f7d804a8e3bda42608072cc2574e1953a/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
