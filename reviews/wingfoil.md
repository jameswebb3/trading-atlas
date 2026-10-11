# Wingfoil: give replay logic a clock distinct from wall time

**Decision question:** Can event-time business logic remain separate from wall-clock latency measurement?

| Field | Review |
| --- | --- |
| Upstream | [Wingfoil](https://github.com/wingfoil-io/wingfoil) |
| Primary area | Backtesting & Simulation |
| Source commit | [d8204fbad91672ecbd049391d4ad67661af904e3](https://github.com/wingfoil-io/wingfoil/commit/d8204fbad91672ecbd049391d4ad67661af904e3) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/LICENSE.txt) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Runs streaming calculation graphs with a distinct engine clock and wall-clock measurement path. The inspected kernel exposes both explicitly, giving historical replay and live latency instrumentation a shared interface without treating elapsed runtime as market time. |

## Project overview

A Rust stream-processing engine targets electronic trading and incremental decision systems. [Project documentation](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/README.md#L15-L30).

## Mechanism worth inspecting

The [architecture](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/docs/wingfoil-architecture.md#L28-L54) separates operation semantics from execution strategy. [Kernel clock accessors](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/crates/wingfoil/src/runtime/kernel.rs#L289-L316) expose engine time separately from a cached wall-clock snapshot. [NanoTime](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/crates/wingfoil/src/runtime/time.rs#L17-L35) anchors monotonic readings to an epoch for absolute timestamps.

## Important limit

The [wall-clock offset](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/crates/wingfoil/src/runtime/time.rs#L27-L35) is sampled once, so it is not ongoing clock synchronization. The [documentation index](https://github.com/wingfoil-io/wingfoil/blob/d8204fbad91672ecbd049391d4ad67661af904e3/docs/README.md#L61-L65) also distinguishes unmerged or proposed trading features from code already on main. Compiled-tier parity and production adapters were not validated.

## Questions to take into your own design

- Does strategy logic read the replay clock exclusively?
- Are absolute timestamps, monotonic durations, and exchange event times represented separately?

## Why this score for a trading system

3/5: concrete clock separation applicable to replay/live equivalence, with a major engine transition and unverified adapter/tier guarantees.

**Scope of this review:** README, architecture and documentation status index, time type and kernel clock source.
