# Short-Term Reversal Strategy: read the license before the return chart

**Decision question:** Does a publicly visible trading study permit reuse of its source?

| Field | Review |
| --- | --- |
| Upstream | [Short-Term Reversal Strategy](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy) |
| Primary area | Signals & Models |
| Source commit | [2a835bf7d795bb6fbf332e7a298981fbbb825b73](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/commit/2a835bf7d795bb6fbf332e7a298981fbbb825b73) |
| Reviewed | 2026-09-26 |
| Declared license | [Proprietary / All Rights Reserved](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 1/5 |
| Trading-system fit | Direct |
| Verdict | Publishes an equity-reversal and options research workflow, but explicitly retains all rights. It is a source-visible study to inspect critically, with reported returns unreplicated and no permission to reuse its code as an open-source component. |

## Project overview

A research project studies post-drawdown equity recovery and related call-option trades. [Project documentation](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/README.md#L389-L395).

## Mechanism worth inspecting

The [workflow documentation](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/README.md#L424-L446) separates recovery screening, contract selection, and option simulation. Its [Sharpe helper](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/backtest_metrics.py#L7-L31) exposes a dated fixed risk-free assumption and configurable annualization basis rather than hiding them in a chart.

## Important limit

The [license](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/LICENSE#L1-L14) does not grant reuse rights. The [data layout](https://github.com/randomwalkhan/Short-Term-Reversal-Strategy/blob/2a835bf7d795bb6fbf332e7a298981fbbb825b73/README.md#L452-L471) describes local ticker CSVs; this review does not establish point-in-time universe reconstruction or the validity of the reported option results.

## Questions to take into your own design

- Is a repository licensed for the use you intend?
- Which universe, rate, calendar, and execution assumptions support its return report?

## Why this score for a trading system

1/5: restricted licensing and an unreplicated asset-specific study make this a cautionary catalog entry, not a recommended implementation reference.

**Scope of this review:** README study/data-layout documentation, metric helper, and full license; strategy returns not replicated.
