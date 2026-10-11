# A merged trade report can change the unit counted as a trade

**Decision question:** Are reported trades fills, lots, or date-grouped summaries?

| Field | Review |
| --- | --- |
| Upstream | [Pinkfish](https://github.com/fja05680/pinkfish) |
| Primary area | Backtesting & Simulation |
| Source commit | [18a0d557ead25e0e82de3ece86bcab6c325a59ed](https://github.com/fja05680/pinkfish/commit/18a0d557ead25e0e82de3ece86bcab6c325a59ed) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/fja05680/pinkfish/blob/18a0d557ead25e0e82de3ece86bcab6c325a59ed/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | Pinkfish keeps a raw trade log and can merge completed trades by entry and exit dates using quantity-weighted prices. That is useful for reporting, but the grouped view can change trade counts and averages. Preserve the original event unit when estimating sample size or execution quality. |

## Mechanism worth inspecting

The [README](https://github.com/fja05680/pinkfish/blob/18a0d557ead25e0e82de3ece86bcab6c325a59ed/README.md#L15-L26) explains caller-selected prices and lack of order matching. The [example guide](https://github.com/fja05680/pinkfish/blob/18a0d557ead25e0e82de3ece86bcab6c325a59ed/examples/README.md#L18-L27) separates strategies and reports. The [merge routine](https://github.com/fja05680/pinkfish/blob/18a0d557ead25e0e82de3ece86bcab6c325a59ed/pinkfish/trade.py#L617-L651) groups by entry then exit date, while [get_log](https://github.com/fja05680/pinkfish/blob/18a0d557ead25e0e82de3ece86bcab6c325a59ed/pinkfish/trade.py#L654-L680) makes merging optional.

## Important limit

Date grouping is a presentation choice, not evidence that executions or outcomes are independent. This equity daily-bar tool does not settle venue fills, intrabar order sequence, or perpetual funding.

## Questions to take into your own design

- Does every metric state whether it uses fills, closed lots, or grouped trades?
- Can the report always be reconciled to the unmerged event ledger?

## Why this score for a trading system

2/5: The raw-versus-summary distinction is a useful reporting caution, but the simulator's equity and caller-price assumptions limit its direct execution value.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
