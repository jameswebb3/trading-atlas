# legacy-validator — A sidecar dictionary makes custom columns accountable

**Decision question:** How can a dataset accept custom fields without silently losing its schema?

| Field | Review |
| --- | --- |
| Upstream | [bids-standard/legacy-validator](https://github.com/bids-standard/legacy-validator) |
| Primary area | Data Quality & Lineage |
| Source commit | [5388fbf3367afdaa2c12ae5928145ca5674cef26](https://github.com/bids-standard/legacy-validator/commit/5388fbf3367afdaa2c12ae5928145ca5674cef26) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The TSV validator checks each nonstandard column against merged JSON sidecar keys and reports a missing description; a test accepts a custom column once described. This is a domain schema convention, not an availability-time or market-data validity test. |

## What this project does

Legacy validator for BIDS neuroimaging datasets and their metadata sidecars. [README](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/README.md).

## Mechanism inspected

The TSV validator checks each nonstandard column against merged JSON sidecar keys and reports a missing description; a test accepts a custom column once described. [Implementation](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/bids-validator/validators/tsv/validateTsvColumns.js#L84-L112). [Related implementation](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/bids-validator/validators/tsv/__tests__/validateTsvColumns.spec.js#L37-L44).

## Limitation that matters

This is a domain schema convention, not an availability-time or market-data validity test. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require a definition, units, origin and available_at for every nonstandard research column before it enters a feature table.

## Why this score

The TSV validator checks each nonstandard column against merged JSON sidecar keys and reports a missing description; a test accepts a custom column once described. This is a domain schema convention, not an availability-time or market-data validity test.

## Source trail

[README](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/README.md) · [Implementation](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/bids-validator/validators/tsv/validateTsvColumns.js#L84-L112) · [Related implementation](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/bids-validator/validators/tsv/__tests__/validateTsvColumns.spec.js#L37-L44) · [License](https://github.com/bids-standard/legacy-validator/blob/5388fbf3367afdaa2c12ae5928145ca5674cef26/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
