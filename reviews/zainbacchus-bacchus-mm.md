# Bacchus MM - How can fill-day performance be revised when settlement arrives later?

**Decision question:** How can fill-day performance be revised when settlement arrives later?

| Field | Review |
| --- | --- |
| Upstream | [zainbacchus/bacchus-mm](https://github.com/zainbacchus/bacchus-mm) |
| Primary area | Portfolio Risk |
| Source commit | [3f4ad577d337277f892138f6064f01c38973d70e](https://github.com/zainbacchus/bacchus-mm/commit/3f4ad577d337277f892138f6064f01c38973d70e) |
| Reviewed | 2026-10-10 |
| Declared license | MIT |
| Review depth | 2/3: README and relevant implementation inspected; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Executive assessment | Rebuilds a daily fill ledger with contracts, volume, fees and settled-outcome PnL, attributing late settlement back to the fill day. Only the configured rebuild window is recalculated; older rows are preserved, and the public retrospective is not an independently reproducible fill tape. |

## What this project does

An open-source prediction-market market-making lab with order execution, event logs and public trading retrospectives. This review focuses on how its daily report distinguishes fills, fees and settlement.

## Mechanism inspected

The daily ledger counts every fill and its fee immediately. It computes gross outcome PnL only when the market result is known, assigns that value to the UTC day of the fill, and rebuilds recent rows so late results revise earlier days. It also keeps settled-contract count separate from total contracts and accumulates net PnL after fees.

## Limitation that matters

The rebuild keeps older CSV rows verbatim after the configured horizon. A later correction to an older fill or settlement would not flow into those rows without a wider rebuild. The public retrospective reports its own losses and selected diagnostics, but does not expose the complete private fill tape needed for independent replication. Its Kalshi contracts and fills do not establish executable returns on Hyperliquid perpetuals.

## Practical check for a trading system

For any realized-performance report, state whether a daily row is by fill time or settlement time, mark unsettled exposure separately, and give corrections an explicit replay horizon. Compare the report against account equity with a separate reconciliation, not by treating the ledger as the account balance.

## Why this score

3/5 because the inspected code gives a directly useful ledger timing and fee-accounting reference, but its results and venue are not transferable alpha evidence.

## Source trail

[README](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/README.md#L3); [Ledger contract](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/research/daily_review.py#L135); [Fill and settlement calculation](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/research/daily_review.py#L190); [Rebuild horizon](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/research/daily_review.py#L214); [Public retrospective](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/research/RETRO-15M-2026-08-18.md#L9); [License](https://github.com/zainbacchus/bacchus-mm/blob/3f4ad577d337277f892138f6064f01c38973d70e/LICENSE#L1).

**Scope:** Source reading only; no upstream installation, execution, security audit, or claim of trading profitability.
