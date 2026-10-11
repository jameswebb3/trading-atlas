# Pyfolio Reloaded — capacity belongs in the strategy report

**Decision question:** How long would a position take to unwind under a participation limit?

| Field | Review |
| --- | --- |
| Upstream | [Pyfolio Reloaded](https://github.com/stefan-jansen/pyfolio-reloaded) |
| Primary area | Portfolio & Risk |
| Source commit | [6b55da7fce365e325046bb080cb13ced1822de95](https://github.com/stefan-jansen/pyfolio-reloaded/commit/6b55da7fce365e325046bb080cb13ced1822de95) |
| Reviewed | 2026-09-27 |
| Declared license | [Apache-2.0](https://github.com/stefan-jansen/pyfolio-reloaded/blob/6b55da7fce365e325046bb080cb13ced1822de95/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Adds a practical capacity dimension to performance reporting: estimated unwind time under a participation limit. Its daily-volume approximation is useful context, while real execution needs depth and stressed-liquidity evidence. |

## Project overview

Pyfolio Reloaded builds strategy tear sheets covering performance, risk and portfolio analysis. [Project documentation](https://github.com/stefan-jansen/pyfolio-reloaded/blob/6b55da7fce365e325046bb080cb13ced1822de95/README.md#L18-L27).

## Mechanism worth inspecting

The capacity calculation estimates liquidation days from position value, a maximum daily-bar participation and a trailing mean of dollar volume. The mean is shifted, avoiding use of the current day's completed volume in that input. [Capacity calculation](https://github.com/stefan-jansen/pyfolio-reloaded/blob/6b55da7fce365e325046bb080cb13ced1822de95/src/pyfolio/capacity.py#L47-L102).

## Important limit

Daily dollar volume is a coarse liquidity proxy, not executable depth. Equity-style positions and capital assumptions need adaptation for margined contracts. A large daily volume does not promise an acceptable spread, queue position or rapid unwind during stress.

## Questions to take into your own design

- Does a strategy report include participation and unwind assumptions beside returns?
- Can the capacity estimate be reconciled with observed depth, fills and stressed liquidity?

## Why this score for a trading system

3/5: a useful trading-report dimension with visible trailing-volume timing, but daily capacity is too coarse to certify perpetual execution.

**Scope of this review:** Capacity and liquidation-day estimate; chart outputs and intraday execution were not run.
