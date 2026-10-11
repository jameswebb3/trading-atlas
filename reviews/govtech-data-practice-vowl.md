# vowl — Validate a contract before using it to validate data

**Decision question:** Can a malformed quality contract make a dataset look checked?

| Field | Review |
| --- | --- |
| Upstream | [govtech-data-practice/vowl](https://github.com/govtech-data-practice/vowl) |
| Primary area | Data Quality & Lineage |
| Source commit | [3e36051283eac4ef9be2aece6be948bf1a422541](https://github.com/govtech-data-practice/vowl/commit/3e36051283eac4ef9be2aece6be948bf1a422541) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Contract construction requires apiVersion and validates the contract object against the corresponding schema before extracting checks. A valid schema cannot prove the checks are sufficient, causal or run on the intended snapshot; remote contract loading adds a supply-chain boundary. |

## What this project does

ODCS-style data contract validator supporting local and referenced contracts. [README](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/README.md).

## Mechanism inspected

Contract construction requires apiVersion and validates the contract object against the corresponding schema before extracting checks. [Implementation](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/src/vowl/contracts/contract.py#L177-L208).

## Limitation that matters

A valid schema cannot prove the checks are sufficient, causal or run on the intended snapshot; remote contract loading adds a supply-chain boundary. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Validate contract version and shape before each source batch, then bind the validated contract hash to the observed data manifest.

## Why this score

Contract construction requires apiVersion and validates the contract object against the corresponding schema before extracting checks. A valid schema cannot prove the checks are sufficient, causal or run on the intended snapshot; remote contract loading adds a supply-chain boundary.

## Source trail

[README](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/README.md) · [Implementation](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/src/vowl/contracts/contract.py#L177-L208) · [License](https://github.com/govtech-data-practice/vowl/blob/3e36051283eac4ef9be2aece6be948bf1a422541/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
