# dagron — Keep bounded evidence from failed attempts

**Decision question:** When a retry succeeds, can the reviewer still see why earlier attempts failed?

| Field | Review |
| --- | --- |
| Upstream | [lucheeseng827/dagron](https://github.com/lucheeseng827/dagron) |
| Primary area | Research & Reproducibility |
| Source commit | [fb181f13ba89dfa58207993e4eca073a4805326a](https://github.com/lucheeseng827/dagron/commit/fb181f13ba89dfa58207993e4eca073a4805326a) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The attempt log stores a bounded UTF-8 tail per failed or repeated attempt, distinguishes a normal repeat from a failure, caps read size, and evicts old attempts by sequence. A tail can omit the first causal error, and the default retention is finite. This is diagnostic evidence, not a complete immutable record or a source of truth for trial results. |

## What this project does

Small durable DAG runner with a separate log of superseded task attempts. [README](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/README.md).

## Mechanism inspected

The attempt log stores a bounded UTF-8 tail per failed or repeated attempt, distinguishes a normal repeat from a failure, caps read size, and evicts old attempts by sequence. [Implementation](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/crates/dagron-core/src/attempt_log.rs#L1-L145).

## Limitation that matters

A tail can omit the first causal error, and the default retention is finite. This is diagnostic evidence, not a complete immutable record or a source of truth for trial results. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Where research or collection jobs retry, retain attempt number, end reason, timestamps and bounded diagnostic tail separately from final status; keep full immutable evidence where needed.

## Why this score

The attempt log stores a bounded UTF-8 tail per failed or repeated attempt, distinguishes a normal repeat from a failure, caps read size, and evicts old attempts by sequence. A tail can omit the first causal error, and the default retention is finite. This is diagnostic evidence, not a complete immutable record or a source of truth for trial results.

## Source trail

[README](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/README.md) · [Implementation](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/crates/dagron-core/src/attempt_log.rs#L1-L145) · [License](https://github.com/lucheeseng827/dagron/blob/fb181f13ba89dfa58207993e4eca073a4805326a/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
