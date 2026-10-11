# isnad — Separate source trust from transmission quality

**Decision question:** Can two agreeing research agents still share the same bad source?

| Field | Review |
| --- | --- |
| Upstream | [alizahidraja/isnad](https://github.com/alizahidraja/isnad) |
| Primary area | Agents & Decision Systems |
| Source commit | [d2b76cf134a2c6450c382b5c12ed563e904c045d](https://github.com/alizahidraja/isnad/commit/d2b76cf134a2c6450c382b5c12ed563e904c045d) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its schema gives origin strength, chain integrity and corroboration independence separate fields; shared ancestry is explicit rather than silently treated as independent confirmation. The grading names and thresholds are domain-specific and not empirically calibrated for trading. Only the separation of evidence axes transfers. |

## What this project does

Claim provenance schema and corroboration model for multi-step research. [README](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/README.md).

## Mechanism inspected

Its schema gives origin strength, chain integrity and corroboration independence separate fields; shared ancestry is explicit rather than silently treated as independent confirmation. [Implementation](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/src/isnad/trace/schema.py#L54-L93).

## Limitation that matters

The grading names and thresholds are domain-specific and not empirically calibrated for trading. Only the separation of evidence axes transfers. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

When agents corroborate a finding, record common source ancestry and do not count dependent chains as independent evidence.

## Why this score

Its schema gives origin strength, chain integrity and corroboration independence separate fields; shared ancestry is explicit rather than silently treated as independent confirmation. The grading names and thresholds are domain-specific and not empirically calibrated for trading. Only the separation of evidence axes transfers.

## Source trail

[README](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/README.md) · [Implementation](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/src/isnad/trace/schema.py#L54-L93) · [License](https://github.com/alizahidraja/isnad/blob/d2b76cf134a2c6450c382b5c12ed563e904c045d/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
