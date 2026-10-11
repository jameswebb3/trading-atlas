# Amber: Does an absent model-quality score trigger a failed release gate?

**Decision question:** Does an absent model-quality score trigger a failed release gate?

| Field | Review |
| --- | --- |
| Upstream | [Th3-Watcher/Amber](https://github.com/Th3-Watcher/Amber) |
| Primary area | Research & Reproducibility |
| Source commit | [2163e2f082791ee81b792afce511887560e4d4d1](https://github.com/Th3-Watcher/Amber/commit/2163e2f082791ee81b792afce511887560e4d4d1) |
| Reviewed | 2026-10-11 |
| Declared license | [MIT](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/LICENSE) |
| Review depth | 2/3: README, relevant documentation and implementation inspected; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Executive assessment | The gate parses fractional or numeric score strings, compares a version's score with a configured minimum, and locates the most recent passing version when auto-rollback is enabled. The decision type separates Pass, Fail with optional target, and NoGate. NoGate covers both an intentionally disabled gate and absent or invalid score metadata. Thus the gate alone does not stop promotion when evidence is missing. Source review did not verify the ledger's crash consistency or end-to-end rollback behavior. |

## What this project does

Stores versioned ML artifacts and selects a prior passing version for score-gated rollback. Its gate returns NoGate when score metadata is absent or unparsable, so a missing quality signal requires a separate fail-closed rule.

## Mechanism inspected

The gate parses fractional or numeric score strings, compares a version's score with a configured minimum, and locates the most recent passing version when auto-rollback is enabled. The decision type separates Pass, Fail with optional target, and NoGate.

## Limitation that matters

NoGate covers both an intentionally disabled gate and absent or invalid score metadata. Thus the gate alone does not stop promotion when evidence is missing. Source review did not verify the ledger's crash consistency or end-to-end rollback behavior.

## Practical check for a trading system

Test missing metadata, unknown score key, malformed fraction and no passing predecessor. An agent or model promotion must reject absent evidence and report a distinct reason rather than interpreting NoGate as acceptance.

## Why this score

2/5 transferable: versioned checkpoints and rollback are useful, but the missing-score semantics are a concrete caution and the tool is not a trading validation system.

## Source trail

[README.md](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/README.md#L31); [README.md](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/README.md#L80); [amber-core/src/gate.rs](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/amber-core/src/gate.rs#L4); [amber-core/src/gate.rs](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/amber-core/src/gate.rs#L17); [amber-core/src/gate.rs](https://github.com/Th3-Watcher/Amber/blob/2163e2f082791ee81b792afce511887560e4d4d1/amber-core/src/gate.rs#L40)

**Scope:** Source reading only; no upstream installation, execution, security audit, or replication of reported returns.
