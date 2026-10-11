# tradingcodex — Reserve the approved order before provider submission

**Decision question:** Can an agent retry an uncertain broker submission without duplicate orders?

| Field | Review |
| --- | --- |
| Upstream | [monarchjuno/tradingcodex](https://github.com/monarchjuno/tradingcodex) |
| Primary area | Agents & Decision Systems |
| Source commit | [721f3c1e9dab2c8a4280ce094cca33d506dcfe33](https://github.com/monarchjuno/tradingcodex/commit/721f3c1e9dab2c8a4280ce094cca33d506dcfe33) |
| Reviewed | 2026-10-09 |
| Declared license | Apache-2.0 ([source](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/LICENSE)) |
| Review depth | 3/3: documentation and relevant implementation read; relevant test source also read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | A database transaction binds an approval receipt and exact order hash to one idempotent reservation before provider submission; uncertain outcomes become `needs_review` and a test asserts retry is blocked. The test uses a fake broker and does not prove HL-specific ACK, fill or restart behavior; this is an authorization-and-uncertainty pattern, not a trading signal. |

## What this project does

Local-first multi-agent investment system with an explicit paper/live order boundary. [README](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/README.md).

## Mechanism inspected

A database transaction binds an approval receipt and exact order hash to one idempotent reservation before provider submission; uncertain outcomes become `needs_review` and a test asserts retry is blocked. [Implementation](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/apps/orders/services.py#L60-L154). [Test source](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/tests/test_broker_center_prd.py#L955-L981).

## Limitation that matters

The test uses a fake broker and does not prove HL-specific ACK, fill or restart behavior; this is an authorization-and-uncertainty pattern, not a trading signal. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Require an exact approved intent and durable reservation before external submission; block replay of an uncertain result until venue reconciliation.

## Why this score

A database transaction binds an approval receipt and exact order hash to one idempotent reservation before provider submission; uncertain outcomes become `needs_review` and a test asserts retry is blocked. The test uses a fake broker and does not prove HL-specific ACK, fill or restart behavior; this is an authorization-and-uncertainty pattern, not a trading signal.

## Source trail

[README](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/README.md) · [Implementation](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/apps/orders/services.py#L60-L154) · [Test source](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/tests/test_broker_center_prd.py#L955-L981) · [License](https://github.com/monarchjuno/tradingcodex/blob/721f3c1e9dab2c8a4280ce094cca33d506dcfe33/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
