# Portarium — Gate agent tool calls at the side-effect boundary

**Decision question:** Can a tool run after a proposal was denied by authority or blast-radius policy?

| Field | Review |
| --- | --- |
| Upstream | [45ck/Portarium](https://github.com/45ck/Portarium) |
| Primary area | Agents & Decision Systems |
| Source commit | [5641e1fb67d31ecc718da13408d064e500a849c2](https://github.com/45ck/Portarium/commit/5641e1fb67d31ecc718da13408d064e500a849c2) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The service checks actor permission, then a tool/tier policy, and calls the underlying invoker only after both pass; denials return distinct authorization and policy reasons. The guarantee only holds if every side-effect path uses this service. A policy tier supplied by an untrusted caller must be derived or checked against authoritative context. |

## What this project does

Agent action service with authorization and policy checks before a tool invoker. [README](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/README.md).

## Mechanism inspected

The service checks actor permission, then a tool/tier policy, and calls the underlying invoker only after both pass; denials return distinct authorization and policy reasons. [Implementation](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/src/application/services/action-gated-tool-invoker.ts#L70-L139).

## Limitation that matters

The guarantee only holds if every side-effect path uses this service. A policy tier supplied by an untrusted caller must be derived or checked against authoritative context. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

For agents allowed to change research or operations, place the authority check immediately before each real write/action and audit bypass routes in tests.

## Why this score

The service checks actor permission, then a tool/tier policy, and calls the underlying invoker only after both pass; denials return distinct authorization and policy reasons. The guarantee only holds if every side-effect path uses this service. A policy tier supplied by an untrusted caller must be derived or checked against authoritative context.

## Source trail

[README](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/README.md) · [Implementation](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/src/application/services/action-gated-tool-invoker.ts#L70-L139) · [License](https://github.com/45ck/Portarium/blob/5641e1fb67d31ecc718da13408d064e500a849c2/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
