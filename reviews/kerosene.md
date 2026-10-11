# Kerosene: complete snapshots before closing a chase order

**Decision question:** What evidence is needed to mark a repriced order complete and report its execution price?

| Field | Review |
| --- | --- |
| Upstream | [nilesjarvis/kerosene](https://github.com/nilesjarvis/kerosene) |
| Primary area | Execution & Exchange Integration |
| Source commit | [2c193855c7223c3842de068ebe5d23b73252ca31](https://github.com/nilesjarvis/kerosene/commit/2c193855c7223c3842de068ebe5d23b73252ca31) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Kerosene waits for complete account evidence before closing a repriced order. Its history can report the last limit as average execution price, so fill-based reporting requires separate verification. |

## Project overview

Rust desktop terminal for Hyperliquid with charts, order entry, and client-side Chase and TWAP automation. Its execution code is a useful reference for order repricing and fill reconciliation.

[Project documentation](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/README.md#L5-L7).

## Mechanism worth inspecting

Kerosene's chase-order reconciliation requires a [complete fills section](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/src/account_update/stream/chase/fill_reconciliation.rs#L15-L31) before using account fills. When the target size appears filled, the order is removed only if the open-order snapshot is authoritative and shows no remaining chase order. Otherwise, the lifecycle moves to verification and requests another account refresh. The relevant [branch is explicit](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/src/account_update/stream/chase/fill_reconciliation.rs#L63-L106).

This is a useful state distinction: an incomplete or absent open-order view is not evidence that an order is gone.

## Important limitation in the same repository

The project's own [metrics audit](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/docs/advanced-orders/chase-metrics-audit.md#L25-L49) says its archived "average price" can come from the last working limit price rather than fill-weighted execution price. It also identifies missing fee, closed-PnL, and per-child-order records in the [history path](https://github.com/nilesjarvis/kerosene/blob/2c193855c7223c3842de068ebe5d23b73252ca31/docs/advanced-orders/chase-metrics-audit.md#L51-L82). A correct terminal state and a correct execution report are separate requirements.

## Questions to take into your own design

- Which snapshot sections are complete and authoritative?
- Can a missing order mean "unknown" rather than "closed"?
- Is average execution price computed from fills, not the latest quote or limit?
- Is every child order ID, fill, fee, and terminal transition retained?

## Why this score for a trading system

Its reconciliation gate addresses live order closure and fill-price evidence, both direct execution risks; the archived price caveat remains material.

**Scope of this review:** We inspected the pinned reconciliation code and audit document. We did not run Kerosene, inspect every exchange path, or verify whether a later commit has fixed the documented history gaps.
