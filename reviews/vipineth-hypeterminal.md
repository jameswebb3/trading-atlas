# hypeterminal — Approval is a distinct preflight outcome

**Decision question:** Can order approval be pending without calling it a validation error?

| Field | Review |
| --- | --- |
| Upstream | [hypeterminal](https://github.com/vipineth/hypeterminal) |
| Primary area | Execution & Exchange Integration |
| Source commit | [a61992eda0fa269ea38d64dd50ed133db1236052](https://github.com/vipineth/hypeterminal/commit/a61992eda0fa269ea38d64dd50ed133db1236052) |
| Reviewed | 2026-10-06 |
| Declared license | [MIT](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The perp validator returns needsApproval with canSubmit false before running balance, market, signer, size and trigger checks. This is a client-side form boundary; passing it does not certify server acceptance, margin or final fill. |

## What this project does

An open-source Hyperliquid terminal covering perpetuals, spot and builder markets. [README](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/README.md).

## Mechanism inspected

The perp validator returns needsApproval with canSubmit false before running balance, market, signer, size and trigger checks. [Implementation](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/apps/terminal/src/lib/errors/stacks/perp-order.ts#L52-L93).

## Limitation that matters

This is a client-side form boundary; passing it does not certify server acceptance, margin or final fill. The conclusion is limited to the inspected path and commit.

## Practical check for a trading system

Keep APPROVAL_REQUIRED separate from INVALID and SUBMITTED in offline actuator/operator acceptance tests.

## Why this score

Direct trading-system relevance: The perp validator returns needsApproval with canSubmit false before running balance, market, signer, size and trigger checks. This is a client-side form boundary; passing it does not certify server acceptance, margin or final fill.

## Source trail

[README](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/README.md) · [Documentation](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/docs/ui-ux-guidelines.md) · [Implementation](https://github.com/vipineth/hypeterminal/blob/a61992eda0fa269ea38d64dd50ed133db1236052/apps/terminal/src/lib/errors/stacks/perp-order.ts#L52-L93).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
