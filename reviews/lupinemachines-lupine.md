# Lupine — Verify bundle bytes before loading

**Decision question:** How can a cached execution bundle be tied to the manifest that named it?

| Field | Review |
| --- | --- |
| Upstream | [lupinemachines/lupine](https://github.com/lupinemachines/lupine) |
| Primary area | Research & Reproducibility |
| Source commit | [f1dfab1e5bb4cfec6a093030b91f2d504ca792f1](https://github.com/lupinemachines/lupine/commit/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The directory validator checks an ETag, schema version, platform key, required file names, and SHA-256 of every listed file before accepting a cache. Byte integrity does not prove the model or trading logic is correct; the manifest also needs trusted origin and data provenance. |

## What this project does

A runtime bundle loader with manifest and integrity checks. [Project README](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/README.md#L1).

## Mechanism inspected

The directory validator checks an ETag, schema version, platform key, required file names, and SHA-256 of every listed file before accepting a cache. [Implementation](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/python/lupine/_bundles.py#L151).

## Limitation that matters

Byte integrity does not prove the model or trading logic is correct; the manifest also needs trusted origin and data provenance. This is a source review, not a runtime or security test.

## Practical check for a trading system

Verify every model artifact and executable config against a pinned manifest before an experiment or deploy.

## Why this score

A strong reusable artifact-integrity pattern with explicit limits.

## Source trail

[README](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/README.md#L1); [Implementation](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/python/lupine/_bundles.py#L151) - [License](https://github.com/lupinemachines/lupine/blob/f1dfab1e5bb4cfec6a093030b91f2d504ca792f1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
