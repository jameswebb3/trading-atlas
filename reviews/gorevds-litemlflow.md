# litemlflow — Store dataset artifacts by content digest

**Decision question:** Can a trial retrieve the exact bytes behind a dataset reference?

| Field | Review |
| --- | --- |
| Upstream | [gorevds/litemlflow](https://github.com/gorevds/litemlflow) |
| Primary area | Research & Reproducibility |
| Source commit | [de4c2ddaa7bba4a236f190c035b70858ff5b087d](https://github.com/gorevds/litemlflow/commit/de4c2ddaa7bba4a236f190c035b70858ff5b087d) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The store streams bytes into a temporary file while hashing, derives a SHA-256 path, then places the object under that digest and reuses an existing object on repeat upload. The inspected path does not fsync the file or directory, and a content hash alone says nothing about source arrival time or rights; no need to import the tracker. |

## What this project does

Self-hosted experiment tracker with a filesystem content-addressed dataset store. [README](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/README.md).

## Mechanism inspected

The store streams bytes into a temporary file while hashing, derives a SHA-256 path, then places the object under that digest and reuses an existing object on repeat upload. [Implementation](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/internal/datasets/cas.go#L101-L163).

## Limitation that matters

The inspected path does not fsync the file or directory, and a content hash alone says nothing about source arrival time or rights; no need to import the tracker. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Bind each trial data manifest to immutable content digests and verify bytes on replay, while retaining event-time and receipt-time provenance separately.

## Why this score

The store streams bytes into a temporary file while hashing, derives a SHA-256 path, then places the object under that digest and reuses an existing object on repeat upload. The inspected path does not fsync the file or directory, and a content hash alone says nothing about source arrival time or rights; no need to import the tracker.

## Source trail

[README](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/README.md) · [Implementation](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/internal/datasets/cas.go#L101-L163) · [License](https://github.com/gorevds/litemlflow/blob/de4c2ddaa7bba4a236f190c035b70858ff5b087d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
