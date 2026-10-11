# Financial Machine Learning — Discovery is not validation

**Decision question:** Does a finance ML resource index tell you which projects to trust?

| Field | Review |
| --- | --- |
| Upstream | [firmai/financial-machine-learning](https://github.com/firmai/financial-machine-learning) |
| Primary area | Signals & Models |
| Source commit | [a0fda6ac1f40251b9eb7cc32dd665db59130714e](https://github.com/firmai/financial-machine-learning/commit/a0fda6ac1f40251b9eb7cc32dd665db59130714e) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Executive assessment | Its search script populates categorized repository lists and flags newly discovered entries. The generated tables mix links and ratings without source-level tests of causality, execution, or returns. |

## What this project does

A collection of financial-machine-learning links, generated wiki entries, and discovery scripts. [Project README](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/README.md#L17).

## Mechanism inspected

Its search script populates categorized repository lists and flags newly discovered entries. [Implementation](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/git_search.py#L307). [Related source 1](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/generated_wiki/data.md#L1).

## Limitation that matters

The generated tables mix links and ratings without source-level tests of causality, execution, or returns. The main README also promotes a commercial platform. This is a source review, not a runtime or security test.

## Practical check for a trading system

Treat new links as leads only; inspect code and data timing before rating their trading relevance.

## Why this score

Useful for finding candidates, but it provides little independent evidence about the reliability of those candidates.

## Source trail

[README](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/README.md#L17); [Implementation](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/git_search.py#L307); [Related source 1](https://github.com/firmai/financial-machine-learning/blob/a0fda6ac1f40251b9eb7cc32dd665db59130714e/generated_wiki/data.md#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
