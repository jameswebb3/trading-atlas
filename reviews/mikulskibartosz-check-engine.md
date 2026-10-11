# check-engine — Set subtraction can erase rejected-row multiplicity

**Decision question:** Does a validation report preserve how many records failed?

| Field | Review |
| --- | --- |
| Upstream | [mikulskibartosz/check-engine](https://github.com/mikulskibartosz/check-engine) |
| Primary area | Data Quality & Lineage |
| Source commit | [383cf4106605cc6f94e800bdc707789c0cedbe95](https://github.com/mikulskibartosz/check-engine/commit/383cf4106605cc6f94e800bdc707789c0cedbe95) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator runs constraints, counts failures and derives rejected rows using DataFrame.subtract on the accepted output. Subtract uses set semantics; identical rejected rows can collapse, so rejected-row counts may not equal the original sample multiplicity. |

## What this project does

DataFrame validation utility that returns accepted rows, rejected rows and violation counts. [README](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/README.md).

## Mechanism inspected

The validator runs constraints, counts failures and derives rejected rows using DataFrame.subtract on the accepted output. [Implementation](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/check-engine-lib/checkengine/validate_df.py#L223-L255).

## Limitation that matters

Subtract uses set semantics; identical rejected rows can collapse, so rejected-row counts may not equal the original sample multiplicity. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Test duplicate invalid market rows and assert input = accepted + rejected by row identity, not distinct values.

## Why this score

The validator runs constraints, counts failures and derives rejected rows using DataFrame.subtract on the accepted output. Subtract uses set semantics; identical rejected rows can collapse, so rejected-row counts may not equal the original sample multiplicity.

## Source trail

[README](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/README.md) · [Implementation](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/check-engine-lib/checkengine/validate_df.py#L223-L255) · [License](https://github.com/mikulskibartosz/check-engine/blob/383cf4106605cc6f94e800bdc707789c0cedbe95/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
