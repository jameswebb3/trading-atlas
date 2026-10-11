# Moon-Dev-AI-Trading-Battles - Can a 200 OK account response still be stale?

**Decision question:** Can a 200 OK account response still be stale?

| Field | Review |
| --- | --- |
| Upstream | [moondevonyt/Moon-Dev-AI-Trading-Battles](https://github.com/moondevonyt/Moon-Dev-AI-Trading-Battles) |
| Primary area | Portfolio & Risk |
| Source commit | [fd25e092f57e2616be4cf354d9606fd88b42f5e2](https://github.com/moondevonyt/Moon-Dev-AI-Trading-Battles/commit/fd25e092f57e2616be4cf354d9606fd88b42f5e2) |
| Reviewed | 2026-10-11 |
| Declared license | No root license text verified at this commit |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | It checks account fields and re-reads the public Hyperliquid endpoint when the proxy fails or returns exactly zero equity. A nonzero stale value passes, and the hosted proxy remains a dependency. |

## What this project does

A Hyperliquid trading-battle harness using a hosted account proxy and public fallback.

## Mechanism inspected

It checks account fields and re-reads the public Hyperliquid endpoint when the proxy fails or returns exactly zero equity.

## Limitation that matters

A nonzero stale value passes, and the hosted proxy remains a dependency.

## Practical check for a trading system

Use source timestamps and account invariants, not just a zero-value alarm.

## Why this score

3/5. The stale-zero recovery is concrete but not complete freshness proof.

## Source trail

[README](https://github.com/moondevonyt/Moon-Dev-AI-Trading-Battles/blob/fd25e092f57e2616be4cf354d9606fd88b42f5e2/README.md#L1); [battle_core.py](https://github.com/moondevonyt/Moon-Dev-AI-Trading-Battles/blob/fd25e092f57e2616be4cf354d9606fd88b42f5e2/battle_core.py#L219).

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
