# AVA Fast Check — Put the random seed in the test name

**Decision question:** Can a probabilistic failure be replayed after CI has moved on?

| Field | Review |
| --- | --- |
| Upstream | [dubzzz/ava-fast-check](https://github.com/dubzzz/ava-fast-check) |
| Primary area | Testing & Verification |
| Source commit | [e37f5a65dd0dcbd6a9ae6582c02327635c8f328f](https://github.com/dubzzz/ava-fast-check/commit/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | When a seed is absent, the wrapper chooses one and places it in the test label shown on failure. A seed alone does not preserve external data, dependency versions, or the smallest failing event sequence. |

## What this project does

An adapter joining AVA tests with fast-check property generation. [Project README](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/README.md#L1).

## Mechanism inspected

When a seed is absent, the wrapper chooses one and places it in the test label shown on failure. [Implementation](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/src/ava-fast-check.ts#L62).

## Limitation that matters

A seed alone does not preserve external data, dependency versions, or the smallest failing event sequence. The adapter is specific to TypeScript test tooling. This is a source review, not a runtime or security test.

## Practical check for a trading system

Save seed, shrunk event trace, source revision, and input fixture together for randomized execution tests.

## Why this score

The seed-in-report pattern is directly useful for reproducing intermittent order-state failures.

## Source trail

[README](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/README.md#L1); [Implementation](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/src/ava-fast-check.ts#L62) - [License](https://github.com/dubzzz/ava-fast-check/blob/e37f5a65dd0dcbd6a9ae6582c02327635c8f328f/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
