# Scyvera - A declared agent permission still needs a sealed call site

**Decision question:** What can a declared agent permission actually prevent at runtime?

| Field | Review |
| --- | --- |
| Upstream | [Skull-boy/agent-contracts](https://github.com/Skull-boy/agent-contracts) |
| Primary area | Research & Reproducibility |
| Source commit | [1439f6a40d889297e51b648a89cd6caee9a93aa1](https://github.com/Skull-boy/agent-contracts/commit/1439f6a40d889297e51b648a89cd6caee9a93aa1) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 3/3: README, relevant implementation and relevant test source inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | Implements default-deny gates for declared agent actions, rejects wildcard permissions and emits per-action audit decisions. Undecorated call sites bypass the gate, labels do not inspect function bodies, and missing approval on an irreversible action is warned rather than blocked. |

## What this project does

A framework-independent agent-contract specification with a Python runtime enforcer and gateways. The review focuses on permission and side-effect gates.

## Mechanism inspected

Contract loading checks schema and rejects wildcard permissions; the gate decorator checks a declared action before calling a sync or async function and records allowed or denied decisions. Tests read in source cover default denial and audit entries.

## Limitation that matters

The author threat model says a caller can bypass an undecorated function and a decorator label cannot prove what its body does. An irreversible side effect without approval points triggers a warning, not a hard denial. The contract file must also be protected by the deployment environment. This is a source review, not a runtime or security test.

## Practical check for a trading system

Place trading-order credentials only behind a narrow gateway, test every exported effectful call site, and fail closed for undeclared or unapproved order placement. Treat the declaration as audited intent, not proof that arbitrary code is safe.

## Why this score

3/5 because code and tests show a concrete transferable agent-authority boundary, with clearly documented bypass conditions that matter for trading actions.

## Source trail

[README](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/README.md#L104); [Wildcard and approval checks](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/src/scyvera/enforcer.py#L323); [Runtime gate](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/src/scyvera/enforcer.py#L649); [Threat model](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/docs/threat-model-enforcer.md#L23); [Enforcer tests](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/tests/test_enforcer.py#L54); [License](https://github.com/Skull-boy/agent-contracts/blob/1439f6a40d889297e51b648a89cd6caee9a93aa1/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
