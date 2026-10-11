# minish - Shrink a failing state sequence under a fixed budget

**Decision question:** Can a large generated failure be reduced without hiding its cause?

| Field | Review |
| --- | --- |
| Upstream | [CogitatorTech/minish](https://github.com/CogitatorTech/minish) |
| Primary area | Testing & Verification |
| Source commit | [61ac1da11cdc6e30ee3bb5ad630af459113de88b](https://github.com/CogitatorTech/minish/commit/61ac1da11cdc6e30ee3bb5ad630af459113de88b) |
| Reviewed | 2026-10-10 |
| Declared license | Apache-2.0 ([source](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/LICENSE)) |
| Review depth | 2/3: README, relevant documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Its integer shrinker searches between a safe and a failing bound, while the runner counts and caps shrink attempts and retains a smaller failing input. A failed allocation can leave no shrink iterator. Shrinking helps only when replaying the candidate gives a stable result; it does not validate the trading model. |

## What this project does

minish is a Zig property-testing library with generators and shrinkers. [README](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/README.md).

## Mechanism inspected

Its integer shrinker searches between a safe and a failing bound, while the runner counts and caps shrink attempts and retains a smaller failing input. [Implementation](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/src/minish/shrink.zig#L75-L141). [Related path](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/src/minish/runner.zig#L160-L209).

## Limitation that matters

A failed allocation can leave no shrink iterator. Shrinking helps only when replaying the candidate gives a stable result; it does not validate the trading model. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Generate order or ledger event sequences, freeze the failing seed, and minimize only when the same violation reproduces.

## Why this score

Concrete debugging mechanism with a bounded budget, though the upstream library and language are not a direct fit.

## Source trail

[README](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/README.md) - [Implementation](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/src/minish/shrink.zig#L75-L141) - [Related path](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/src/minish/runner.zig#L160-L209) - [License](https://github.com/CogitatorTech/minish/blob/61ac1da11cdc6e30ee3bb5ad630af459113de88b/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
