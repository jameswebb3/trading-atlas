# Morpho Blue — Which direction should accounting conversions round

**Decision question:** Which direction should accounting conversions round?

| Field | Review |
| --- | --- |
| Upstream | [Morpho Blue](https://github.com/morpho-org/morpho-blue) |
| Primary area | Portfolio & Risk |
| Source commit | [8e26ca6a8dbc5089edcd67fb576248810fd2870a](https://github.com/morpho-org/morpho-blue/commit/8e26ca6a8dbc5089edcd67fb576248810fd2870a) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-2.0-or-later](https://github.com/morpho-org/morpho-blue/blob/8e26ca6a8dbc5089edcd67fb576248810fd2870a/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A compact reference for asset/share accounting with explicit rounding direction and empty-market behavior. The virtual-share design has documented debt trade-offs and needs its own invariant checks. |

## Project overview

Morpho Blue is an EVM lending protocol with a compact core and explicit asset/share conversion helpers. [Project documentation](https://github.com/morpho-org/morpho-blue/blob/8e26ca6a8dbc5089edcd67fb576248810fd2870a/README.md#L3-L24).

## Mechanism worth inspecting

SharesMathLib exposes separate conversions rounding up or down, using virtual shares and virtual assets to define empty-market behavior. Its comments identify the precision and debt trade-offs. [Conversion contract](https://github.com/morpho-org/morpho-blue/blob/8e26ca6a8dbc5089edcd67fb576248810fd2870a/src/libraries/SharesMathLib.sol#L9-L43).

## Important limit

Virtual borrow shares can represent unrealizable bad debt; the library explicitly warns about that assumption. Its lending-share conventions are not a substitute for exchange position accounting.

## Questions to take into your own design

- Which direction should accounting conversions round?
- Which invariant must hold after each asset-to-share and share-to-asset conversion?

## Why this score for a trading system

3/5: directly relevant monetary arithmetic with precise named rounding operations; lending assumptions limit wider reuse.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
