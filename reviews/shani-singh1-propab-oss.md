# Propab — A genuine citation can support the wrong subject

**Decision question:** Can evidence about one entity be reused to justify a different claim?

| Field | Review |
| --- | --- |
| Upstream | [shani-singh1/propab-oss](https://github.com/shani-singh1/propab-oss) |
| Primary area | Agents & Decision Systems |
| Source commit | [13d03a81beac97a2c89e8ae616f221b256396ce1](https://github.com/shani-singh1/propab-oss/commit/13d03a81beac97a2c89e8ae616f221b256396ce1) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/LICENSE#L1)) |
| Review depth | 2/3: README and relevant source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The binding check vetoes a citation when both sides name subject entities but share none, before considering generic relationship tags. Entity matching is a heuristic; missing subject terms fall through, and a matching citation still may not prove causality. |

## What this project does

A research-evidence binding library. [Project README](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/README.md#L1).

## Mechanism inspected

The binding check vetoes a citation when both sides name subject entities but share none, before considering generic relationship tags. [Implementation](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/packages/propab-core/propab/evidence_binding.py#L450).

## Limitation that matters

Entity matching is a heuristic; missing subject terms fall through, and a matching citation still may not prove causality. This is a source review, not a runtime or security test.

## Practical check for a trading system

Bind each trading claim to instrument, horizon, population, and intervention before accepting supporting evidence.

## Why this score

A concrete guard against cross-subject evidence laundering in automated research.

## Source trail

[README](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/README.md#L1); [Implementation](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/packages/propab-core/propab/evidence_binding.py#L450) - [License](https://github.com/shani-singh1/propab-oss/blob/13d03a81beac97a2c89e8ae616f221b256396ce1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
