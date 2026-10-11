# Awesome Quant — Audit the directory as well as its entries

**Decision question:** How can a large quant directory avoid quietly accumulating dead or misleading links?

| Field | Review |
| --- | --- |
| Upstream | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) |
| Primary area | Signals & Models |
| Source commit | [48e48a76b2054b5fe6eede6852ffef7783b992ce](https://github.com/wilsonfreitas/awesome-quant/commit/48e48a76b2054b5fe6eede6852ffef7783b992ce) |
| Reviewed | 2026-10-10 |
| Declared license | No root license found |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its README auditor deduplicates URLs, probes destinations, and records findings for broken links and repository state. An audited link says nothing about whether a linked strategy is causal or a package is safe. |

## What this project does

A long-running directory of quantitative-finance libraries and learning resources, rather than a trading engine. [Project README](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/README.md#L171).

## Mechanism inspected

Its README auditor deduplicates URLs, probes destinations, and records findings for broken links and repository state. That is a useful maintenance pattern for any public software catalog. [Implementation](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/scripts/audit_readme.py#L448). [Related source 1](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/README.md#L761).

## Limitation that matters

An audited link says nothing about whether a linked strategy is causal or a package is safe. The directory is broad and does not supply a common evidence standard for trading results. This is a source review, not a runtime or security test.

## Practical check for a trading system

Keep URL health, repository activity, and source-backed trading assessment as separate fields.

## Why this score

The repository is useful as a discovery and catalog-maintenance reference, but it cannot validate trading claims.

## Source trail

[README](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/README.md#L171); [Implementation](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/scripts/audit_readme.py#L448); [Related source 1](https://github.com/wilsonfreitas/awesome-quant/blob/48e48a76b2054b5fe6eede6852ffef7783b992ce/README.md#L761).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
