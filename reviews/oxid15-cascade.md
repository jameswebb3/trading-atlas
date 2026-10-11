# cascade — Input validation does not validate the output

**Decision question:** Does a function decorator check its returned data too?

| Field | Review |
| --- | --- |
| Upstream | [cascade](https://github.com/Oxid15/cascade) |
| Primary area | Data Quality & Lineage |
| Source commit | [ea06d67a5530c2a4e23bca73c3f18030ead5844f](https://github.com/Oxid15/cascade/commit/ea06d67a5530c2a4e23bca73c3f18030ead5844f) |
| Reviewed | 2026-10-06 |
| Declared license | [Apache-2.0](https://github.com/Oxid15/cascade/blob/ea06d67a5530c2a4e23bca73c3f18030ead5844f/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Its validate_in decorator inspects input annotations and validates arguments before invoking the wrapped function. The documented path explicitly does not check return values; a successful call can emit an invalid feature table. |

## What this project does

A small local-first MLOps library with data validators and artifact tracking. [README](https://github.com/Oxid15/cascade/blob/ea06d67a5530c2a4e23bca73c3f18030ead5844f/README.md).

## Mechanism inspected

Its validate_in decorator inspects input annotations and validates arguments before invoking the wrapped function. [Implementation](https://github.com/Oxid15/cascade/blob/ea06d67a5530c2a4e23bca73c3f18030ead5844f/cascade/data/validation.py#L166-L236).

## Limitation that matters

The documented path explicitly does not check return values; a successful call can emit an invalid feature table. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Test both ingress and egress schemas for feature builders, with available_at checked after transformation.

## Why this score

Transferable engineering pattern: Its validate_in decorator inspects input annotations and validates arguments before invoking the wrapped function. The documented path explicitly does not check return values; a successful call can emit an invalid feature table.

## Source trail

[README](https://github.com/Oxid15/cascade/blob/ea06d67a5530c2a4e23bca73c3f18030ead5844f/README.md) · [Implementation](https://github.com/Oxid15/cascade/blob/ea06d67a5530c2a4e23bca73c3f18030ead5844f/cascade/data/validation.py#L166-L236).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
