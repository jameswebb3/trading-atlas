# SIE - Can a dependency fingerprint collapse distinct runtime environments?

**Decision question:** Can a dependency fingerprint collapse distinct runtime environments?

| Field | Review |
| --- | --- |
| Upstream | [superlinked/sie](https://github.com/superlinked/sie) |
| Primary area | Research & Reproducibility |
| Source commit | [d8053bd4deb3c9c062ce319415d2ce5ee9de1369](https://github.com/superlinked/sie/commit/d8053bd4deb3c9c062ce319415d2ce5ee9de1369) |
| Reviewed | 2026-10-11 |
| Declared license | Apache-2.0 |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The requirement helper strips environment markers, sorts dependencies and hashes the normalized payload. Removing markers can make materially different platform dependency sets appear identical. |

## What this project does

A server that hashes normalized bundle requirements.

## Mechanism inspected

The requirement helper strips environment markers, sorts dependencies and hashes the normalized payload.

## Limitation that matters

Removing markers can make materially different platform dependency sets appear identical.

## Practical check for a trading system

Fingerprint the exact resolved runtime environment in experiment manifests.

## Why this score

2/5. The deterministic hash pattern helps comparison; normalization must preserve semantics.

## Source trail

[README](https://github.com/superlinked/sie/blob/d8053bd4deb3c9c062ce319415d2ce5ee9de1369/README.md#L1); [packages/sie_server/src/sie_server/bundle_requirements.py](https://github.com/superlinked/sie/blob/d8053bd4deb3c9c062ce319415d2ce5ee9de1369/packages/sie_server/src/sie_server/bundle_requirements.py#L50); [packages/sie_server/src/sie_server/bundle_requirements.py](https://github.com/superlinked/sie/blob/d8053bd4deb3c9c062ce319415d2ce5ee9de1369/packages/sie_server/src/sie_server/bundle_requirements.py#L60).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
