# runtypes-generate — Unsupported schema types should fail explicitly

**Decision question:** What should a generator do when it cannot produce a valid value for a type?

| Field | Review |
| --- | --- |
| Upstream | [typeetfunc/runtypes-generate](https://github.com/typeetfunc/runtypes-generate) |
| Primary area | Testing & Verification |
| Source commit | [a413f695d2e9e9aa4c824d20d15cb07bab868de1](https://github.com/typeetfunc/runtypes-generate/commit/a413f695d2e9e9aa4c824d20d15cb07bab868de1) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | It dispatches by registered type tag and throws on an unsupported tag instead of silently generating a fallback value. A generated value meeting type shape may still violate trading units, time availability, or venue increments. |

## What this project does

A TypeScript generator adapter for runtime type definitions. [Project README](https://github.com/typeetfunc/runtypes-generate/blob/a413f695d2e9e9aa4c824d20d15cb07bab868de1/README.md#L1).

## Mechanism inspected

It dispatches by registered type tag and throws on an unsupported tag instead of silently generating a fallback value. [Implementation](https://github.com/typeetfunc/runtypes-generate/blob/a413f695d2e9e9aa4c824d20d15cb07bab868de1/src/index.ts#L141).

## Limitation that matters

A generated value meeting type shape may still violate trading units, time availability, or venue increments. This is a source review, not a runtime or security test.

## Practical check for a trading system

Fail test setup when a market-event field lacks a generator; add domain constraints for tick, lot, and timestamp.

## Why this score

Its explicit unsupported-type path is useful for trustworthy property tests.

## Source trail

[README](https://github.com/typeetfunc/runtypes-generate/blob/a413f695d2e9e9aa4c824d20d15cb07bab868de1/README.md#L1); [Implementation](https://github.com/typeetfunc/runtypes-generate/blob/a413f695d2e9e9aa4c824d20d15cb07bab868de1/src/index.ts#L141).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
