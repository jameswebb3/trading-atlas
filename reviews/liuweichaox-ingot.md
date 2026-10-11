# Ingot — Bind a tool result to its limitations

**Decision question:** Can an agent’s stored tool result change without changing the evidence record?

| Field | Review |
| --- | --- |
| Upstream | [liuweichaox/Ingot](https://github.com/liuweichaox/Ingot) |
| Primary area | Agents & Decision Systems |
| Source commit | [901358e8f1fa0b96193f84fd64cb498726424e43](https://github.com/liuweichaox/Ingot/commit/901358e8f1fa0b96193f84fd64cb498726424e43) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The snapshot digest covers tool/version, summary, data, related records, limitations and outcome, and verification recomputes the hash with a constant-time equality check. A stored hash is not authenticated; someone who can edit both content and hash can replace both. It detects accidental or partial alteration, not a malicious writer. |

## What this project does

Agent orchestration system with tool-result snapshots. [README](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/README.md).

## Mechanism inspected

The snapshot digest covers tool/version, summary, data, related records, limitations and outcome, and verification recomputes the hash with a constant-time equality check. [Implementation](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/src/shared/Ingot.Agent.Contracts/AgentToolResultIntegrity.cs#L7-L59).

## Limitation that matters

A stored hash is not authenticated; someone who can edit both content and hash can replace both. It detects accidental or partial alteration, not a malicious writer. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Hash the complete agent evidence envelope, including limitations and outcome, before using it in a report; preserve an external source receipt or signed anchor where adversarial tampering matters.

## Why this score

The snapshot digest covers tool/version, summary, data, related records, limitations and outcome, and verification recomputes the hash with a constant-time equality check. A stored hash is not authenticated; someone who can edit both content and hash can replace both. It detects accidental or partial alteration, not a malicious writer.

## Source trail

[README](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/README.md) · [Implementation](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/src/shared/Ingot.Agent.Contracts/AgentToolResultIntegrity.cs#L7-L59) · [License](https://github.com/liuweichaox/Ingot/blob/901358e8f1fa0b96193f84fd64cb498726424e43/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
