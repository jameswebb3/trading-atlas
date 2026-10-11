# dry-validation — Cross-field rules need a separate failure channel

**Decision question:** Where should a relation between fields fail after shape validation?

| Field | Review |
| --- | --- |
| Upstream | [dry-validation](https://github.com/dry-rb/dry-validation) |
| Primary area | Data Quality & Lineage |
| Source commit | [192b74a78f5eed474d2c04a887275ee350a7693a](https://github.com/dry-rb/dry-validation/commit/192b74a78f5eed474d2c04a887275ee350a7693a) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and a relevant test read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The evaluator accumulates key and base failures and exposes checks for schema and rule errors; its tests exercise failure paths. Shape success alone does not prove a timestamp is causal or an amount agrees with a contract size. |

## What this project does

A Ruby contract library that layers rule evaluation on top of schema processing. [README](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/README.md).

## Mechanism inspected

The evaluator accumulates key and base failures and exposes checks for schema and rule errors; its tests exercise failure paths. [Implementation](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/lib/dry/validation/evaluator.rb#L92-L196).

## Limitation that matters

Shape success alone does not prove a timestamp is causal or an amount agrees with a contract size. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Add one cross-field fixture: received_at must not precede source event and close size must not exceed position.

## Why this score

Transferable engineering pattern: The evaluator accumulates key and base failures and exposes checks for schema and rule errors; its tests exercise failure paths. Shape success alone does not prove a timestamp is causal or an amount agrees with a contract size.

## Source trail

[README](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/README.md) · [Implementation](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/lib/dry/validation/evaluator.rb#L92-L196) · [Relevant test](https://github.com/dry-rb/dry-validation/blob/192b74a78f5eed474d2c04a887275ee350a7693a/spec/integration/evaluator_spec.rb).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
