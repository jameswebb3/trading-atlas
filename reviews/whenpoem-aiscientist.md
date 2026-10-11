# aiscientist - Reserve held-out query budget before running

**Decision question:** How can a reserved evaluation set keep a bounded number of looks?

| Field | Review |
| --- | --- |
| Upstream | [whenpoem/aiscientist](https://github.com/whenpoem/aiscientist) |
| Primary area | Research & Reproducibility |
| Source commit | [15a1e223a05fba45ed59aeaea09678a7eea19587](https://github.com/whenpoem/aiscientist/commit/15a1e223a05fba45ed59aeaea09678a7eea19587) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A held-out query checks the current SHA-256 manifest against registration, then atomically reserves budget in SQLite before launching the model script; failed scripts still consume the reserved look. The repository is archived. Manifest integrity and query accounting do not themselves prove correct split timing, a sound baseline or statistical power. |

## What this project does

ClaudeScientist includes verification tools for experimental claims, provenance and a sequestered evaluation dataset. [README](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/README.md).

## Mechanism inspected

A held-out query checks the current SHA-256 manifest against registration, then atomically reserves budget in SQLite before launching the model script; failed scripts still consume the reserved look. [Implementation](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/src/verify_mcp/tools/heldout.py#L30-L123). [Related path](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/src/claudescientist/heldout.py#L49-L82).

## Limitation that matters

The repository is archived. Manifest integrity and query accounting do not themselves prove correct split timing, a sound baseline or statistical power. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

If a held-out tape is ever used for candidate evaluation, require a frozen hash, an explicit query budget and a monotone ledger of all attempted looks.

## Why this score

A held-out query checks the current SHA-256 manifest against registration, then atomically reserves budget in SQLite before launching the model script; failed scripts still consume the reserved look. The repository is archived. Manifest integrity and query accounting do not themselves prove correct split timing, a sound baseline or statistical power.

## Source trail

[README](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/README.md) - [Implementation](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/src/verify_mcp/tools/heldout.py#L30-L123) - [Related path](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/src/claudescientist/heldout.py#L49-L82) - [License](https://github.com/whenpoem/aiscientist/blob/15a1e223a05fba45ed59aeaea09678a7eea19587/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
