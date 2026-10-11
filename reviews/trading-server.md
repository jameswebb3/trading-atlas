# trading-server: keep ambiguous batch submission in a reconciliation state

**Decision question:** Does an uncertain bulk-order response preserve enough state to reconcile the batch?

| Field | Review |
| --- | --- |
| Upstream | [trading-server](https://github.com/s-brez/trading-server) |
| Primary area | Execution & Exchange Integration |
| Source commit | [d3b0405c62cfa28b48cca0f3e71b66fba1db4533](https://github.com/s-brez/trading-server/commit/d3b0405c62cfa28b48cca0f3e71b66fba1db4533) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0-or-later](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Groups strategy orders into consented trade batches before submission. Its broker source also removes batches after an ambiguous response and leaves crash recovery unfinished, making it a useful example of the distinction between approval, submission, and confirmed execution. |

## Project overview

An event-driven execution server groups multiple strategies and venues under portfolio risk and reporting. [Project documentation](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/README.md#L1-L4).

## Mechanism worth inspecting

[Batch handling](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/broker.py#L59-L107) groups orders by trade ID, checks consent and expected order count, then submits the batch. [Submission handling](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/broker.py#L109-L138) distinguishes returned confirmations from possible failure in its log.

## Important limit

Both outcomes reach batch removal in the [same path](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/broker.py#L109-L138). [Overdue-trade recovery](https://github.com/s-brez/trading-server/blob/d3b0405c62cfa28b48cca0f3e71b66fba1db4533/broker.py#L144-L158) is unimplemented. This is not a complete example of safe retry or restart after partial venue acceptance.

## Questions to take into your own design

- Does an ambiguous submission remain pending reconciliation rather than disappear?
- Is consent bound to the exact order payload and its expiry?

## Why this score for a trading system

2/5: useful batch-consent structure and visible incomplete-state examples, with substantial submission and restart limitations.

**Scope of this review:** README features/market-data documentation, broker batch, consent, and overdue-trade source.
