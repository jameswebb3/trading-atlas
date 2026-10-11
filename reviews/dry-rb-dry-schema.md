# dry-schema — Validation output and errors are separate

**Decision question:** Can a parsed record carry errors without becoming an accepted observation?

| Field | Review |
| --- | --- |
| Upstream | [dry-schema](https://github.com/dry-rb/dry-schema) |
| Primary area | Data Quality & Lineage |
| Source commit | [4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646](https://github.com/dry-rb/dry-schema/commit/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/dry-rb/dry-schema/blob/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The Result object exposes processed output, a scoped path and separate success/failure/error accessors. A caller that reads output alone could ignore the error set; schema validity does not establish timing, publication or measurement units. |

## What this project does

A Ruby schema library that returns processed output together with path-scoped errors. [README](https://github.com/dry-rb/dry-schema/blob/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646/README.md).

## Mechanism inspected

The Result object exposes processed output, a scoped path and separate success/failure/error accessors. [Implementation](https://github.com/dry-rb/dry-schema/blob/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646/lib/dry/schema/result.rb#L72-L175).

## Limitation that matters

A caller that reads output alone could ignore the error set; schema validity does not establish timing, publication or measurement units. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Require data admission to check both transformed value and error status, then attach the source receipt.

## Why this score

Transferable engineering pattern: The Result object exposes processed output, a scoped path and separate success/failure/error accessors. A caller that reads output alone could ignore the error set; schema validity does not establish timing, publication or measurement units.

## Source trail

[README](https://github.com/dry-rb/dry-schema/blob/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646/README.md) · [Implementation](https://github.com/dry-rb/dry-schema/blob/4e19e0fbad4b32ae716a9d7d1c3cb45d1f6b9646/lib/dry/schema/result.rb#L72-L175).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
