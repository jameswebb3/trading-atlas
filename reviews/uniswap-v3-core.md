# Uniswap V3 Core — How does an oracle distinguish allocated capacity from usable history

**Decision question:** How does an oracle distinguish allocated capacity from usable history?

| Field | Review |
| --- | --- |
| Upstream | [Uniswap V3 Core](https://github.com/Uniswap/v3-core) |
| Primary area | Market Data & Ingestion |
| Source commit | [d0831dc6b8a318df3872b6d68f6de135c9f3ec29](https://github.com/Uniswap/v3-core/commit/d0831dc6b8a318df3872b6d68f6de135c9f3ec29) |
| Reviewed | 2026-09-26 |
| Declared license | [BUSL-1.1 text; GPL-2.0-or-later change license dated 2023-04-01](https://github.com/Uniswap/v3-core/blob/d0831dc6b8a318df3872b6d68f6de135c9f3ec29/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A precise reference for bounded on-chain price history. Its oracle rejects queries beyond retained observations and distinguishes storage capacity from populated history; finality and off-chain availability remain separate concerns. |

## Project overview

Uniswap V3 Core implements concentrated-liquidity pools and an on-chain observation oracle. This review concerns historical-data coverage rather than a trading strategy. [Project documentation](https://github.com/Uniswap/v3-core/blob/d0831dc6b8a318df3872b6d68f6de135c9f3ec29/README.md#L9-L11).

## Mechanism worth inspecting

The oracle stores observations in a bounded ring; newly allocated slots are not necessarily initialized. Its surrounding-observation lookup rejects a target older than the oldest usable observation. [Storage contract](https://github.com/Uniswap/v3-core/blob/d0831dc6b8a318df3872b6d68f6de135c9f3ec29/contracts/libraries/Oracle.sol#L4-L20), [coverage gate](https://github.com/Uniswap/v3-core/blob/d0831dc6b8a318df3872b6d68f6de135c9f3ec29/contracts/libraries/Oracle.sol#L197-L229).

## Important limit

The latest accumulator can be transformed forward from the newest observation using current tick and liquidity; it is not a new independently observed trade. Chain finality and collector receipt times require separate handling.

## Questions to take into your own design

- How does an oracle distinguish allocated capacity from usable history?
- How is the oldest usable observation exposed to the feature consumer?

## Why this score for a trading system

3/5: directly relevant to interpreting on-chain market data, but the reviewed AMM oracle is not an execution or price model for other venues.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
