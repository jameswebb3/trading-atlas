# Intelligent Trading Bot: share feature generators across batch and stream paths

**Decision question:** Can offline and online feature computation use the same declared generators?

| Field | Review |
| --- | --- |
| Upstream | [Intelligent Trading Bot](https://github.com/asavinov/intelligent-trading-bot) |
| Primary area | Signals & Models |
| Source commit | [0f8748d21906d37b7d33de9278f4742b8f419456](https://github.com/asavinov/intelligent-trading-bot/commit/0f8748d21906d37b7d33de9278f4742b8f419456) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Uses the same configurable feature generators in batch preparation and online analysis. Its online path tracks overwritten and newly appended rows, making it a concrete reference for incremental recomputation and a useful target for batch-versus-stream parity tests. |

## Project overview

A configurable cryptocurrency research and signaling bot separates offline training from online feature computation. [Project documentation](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/README.md#L15-L21).

## Mechanism worth inspecting

[Feature documentation](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/docs/features.md#L13-L54) declares dependencies and generator configuration. [Batch computation](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/scripts/features.py#L72-L88) and [online computation](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/common/analyzer.py#L184-L191) call the same generator interface. [Dirty-row tracking](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/common/analyzer.py#L134-L176) accounts for overlaps when data is appended.

## Important limit

Online computation retains a [bounded history window](https://github.com/asavinov/intelligent-trading-bot/blob/0f8748d21906d37b7d33de9278f4742b8f419456/common/analyzer.py#L267-L269), while batch computation can process a different input extent. A shared interface does not prove causal feature definitions or parity across those contexts, and the review establishes no predictive profitability.

## Questions to take into your own design

- Do replay and live features agree after a revised or overlapping input bar?
- Is each generator's required history and publication cutoff explicit?

## Why this score for a trading system

3/5: directly relevant shared feature paths and revision handling; output equivalence and causal validity remain unverified.

**Scope of this review:** README, feature documentation, batch feature and online analyzer source.
