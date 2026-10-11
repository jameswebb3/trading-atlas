# Curve StableSwap NG — What does an on-chain oracle price actually represent

**Decision question:** What does an on-chain oracle price actually represent?

| Field | Review |
| --- | --- |
| Upstream | [Curve StableSwap NG](https://github.com/curvefi/stableswap-ng) |
| Primary area | Market Data & Ingestion |
| Source commit | [911b5b45e4edafda96a74ec5f464a673c380456c](https://github.com/curvefi/stableswap-ng/commit/911b5b45e4edafda96a74ec5f464a673c380456c) |
| Reviewed | 2026-09-26 |
| Declared license | [Mixed: restrictive root notice; inspected LP oracle declares MIT](https://github.com/curvefi/stableswap-ng/blob/911b5b45e4edafda96a74ec5f464a673c380456c/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A useful on-chain valuation reference with unusually explicit unit and oracle caveats. Its LP price depends on virtual price, underlying-asset conversion and a capped oracle, so it must not be presented as a directly tradable quote. |

## Project overview

StableSwap NG contains Curve pool contracts and pricing oracles. This focused review examines the two-coin LP oracle and its declared valuation assumptions. [Project documentation](https://github.com/curvefi/stableswap-ng/blob/911b5b45e4edafda96a74ec5f464a673c380456c/README.md).

## Mechanism worth inspecting

The LP oracle validates positive inputs and the supported pool shape, then combines portfolio value with the pool's virtual price. Its API documents the numeraire and 1e18 scaling. [Sanity gate](https://github.com/curvefi/stableswap-ng/blob/911b5b45e4edafda96a74ec5f464a673c380456c/contracts/main/StableSwapNGLPOracle.vy#L27-L56), [valuation](https://github.com/curvefi/stableswap-ng/blob/911b5b45e4edafda96a74ec5f464a673c380456c/contracts/main/StableSwapNGLPOracle.vy#L75-L111).

## Important limit

The file warns that virtual-price increases, wash trading and rate oracles can inflate LP valuation. Yield-bearing token quotes use the underlying base asset, and the underlying price oracle is capped. This is not an executable bid or ask.

## Questions to take into your own design

- What does an on-chain oracle price actually represent?
- Is the quote denominated in the pool token, its underlying asset or an executable market?

## Why this score for a trading system

3/5: concrete market-data interpretation and failure boundaries. The root license is restrictive, with an MIT declaration on the inspected oracle file; adoption requires file-specific review.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
