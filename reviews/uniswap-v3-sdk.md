# Uniswap V3 SDK — Can a quote model preserve the protocol's rounding rules

**Decision question:** Can a quote model preserve the protocol's rounding rules?

| Field | Review |
| --- | --- |
| Upstream | [Uniswap V3 SDK](https://github.com/Uniswap/v3-sdk) |
| Primary area | Backtesting & Simulation |
| Source commit | [4e16fe8e56c8c26541545f138c89133794c7ce72](https://github.com/Uniswap/v3-sdk/commit/4e16fe8e56c8c26541545f138c89133794c7ce72) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/Uniswap/v3-sdk/blob/4e16fe8e56c8c26541545f138c89133794c7ce72/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A historical reference for exact-input and exact-output swap arithmetic, including fee rounding. Use it to study AMM quote mechanics; newer SDK development lives in the Uniswap monorepo. |

## Project overview

The archived standalone SDK models Uniswap V3 pools and swaps. Its README directs newer versions to the Uniswap SDK monorepo. [Project documentation](https://github.com/Uniswap/v3-sdk/blob/4e16fe8e56c8c26541545f138c89133794c7ce72/README.md#L1-L3).

## Mechanism worth inspecting

SwapMath separates exact-input and exact-output execution, rounds required input upwards and limits delivered output. It handles a partial step and rounds fees explicitly. [Swap step](https://github.com/Uniswap/v3-sdk/blob/4e16fe8e56c8c26541545f138c89133794c7ce72/src/utils/swapMath.ts#L29-L103). Pool documentation makes tick data a distinct input. [Pool contract](https://github.com/Uniswap/v3-sdk/blob/4e16fe8e56c8c26541545f138c89133794c7ce72/src/entities/pool.ts#L60-L77).

## Important limit

This repository is a historical SDK location, and the formula assumes valid pool and tick state. It does not model arbitrary exchange order books, latency or derivatives fees.

## Questions to take into your own design

- Can a quote model preserve the protocol's rounding rules?
- Which pool-state snapshot and tick set identify the quote being reproduced?

## Why this score for a trading system

2/5: precise on-chain arithmetic but an archived source location and a narrow AMM model, unsuitable as a general trading simulator.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
