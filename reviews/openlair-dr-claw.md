# dr-claw — Compute availability is not research validity

**Decision question:** Can an agent distinguish local from remote compute availability?

| Field | Review |
| --- | --- |
| Upstream | [dr-claw](https://github.com/OpenLAIR/dr-claw) |
| Primary area | Agents & Decision Systems |
| Source commit | [d51b64e13bae8247d41efc9e631b81ee76b9cb9f](https://github.com/OpenLAIR/dr-claw/commit/d51b64e13bae8247d41efc9e631b81ee76b9cb9f) |
| Reviewed | 2026-10-06 |
| Declared license | [Mixed GPL-3.0 / AGPL-3.0](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Adjacent |
| Verdict | Its compute check reports local and remote availability and a reason when no provider is ready. A reachable GPU or cloud instance does not mean an experiment is safe, preregistered or causally valid; the repository also has mixed GPL/AGPL licensing. |

## What this project does

A full-stack research-agent workspace with several compute backends. [README](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/README.md).

## Mechanism inspected

Its compute check reports local and remote availability and a reason when no provider is ready. [Implementation](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/server/utils/computeCheck.js#L154-L286).

## Limitation that matters

A reachable GPU or cloud instance does not mean an experiment is safe, preregistered or causally valid; the repository also has mixed GPL/AGPL licensing. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Do not treat compute readiness as evidence approval; no adoption of its multi-backend stack.

## Why this score

Indirect relevance only: Its compute check reports local and remote availability and a reason when no provider is ready. A reachable GPU or cloud instance does not mean an experiment is safe, preregistered or causally valid; the repository also has mixed GPL/AGPL licensing.

## Source trail

[README](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/README.md) · [Documentation](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/docs/superpowers/specs/2026-04-09-architecture-perf-multidevice-brainstorm.md) · [Implementation](https://github.com/OpenLAIR/dr-claw/blob/d51b64e13bae8247d41efc9e631b81ee76b9cb9f/server/utils/computeCheck.js#L154-L286).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
