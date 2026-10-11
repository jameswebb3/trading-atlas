# Stock Indicators for .NET: compare batch, buffer, and stream indicators against one baseline

**Decision question:** Can three indicator calculation paths share a checked numerical contract?

| Field | Review |
| --- | --- |
| Upstream | [Stock Indicators for .NET](https://github.com/facioquo/stock-indicators-dotnet) |
| Primary area | Testing & Verification |
| Source commit | [9f0bece51eb45414dd75a02a3cab719ac9f9b12e](https://github.com/facioquo/stock-indicators-dotnet/commit/9f0bece51eb45414dd75a02a3cab719ac9f9b12e) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/LICENSE) |
| Review depth | 3/3: documentation, EMA source, and regression test read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Implements financial indicators in batch, buffered, and streaming forms. The inspected EMA regression suite compares all three against the same stored baseline, while the EMA source and documentation expose warm-up and initialization semantics. |

## Project overview

A C# financial-indicator library includes incremental and observable computation styles. [Project documentation](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/README.md#L8-L20).

## Mechanism worth inspecting

The [dual-track ADR](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/docs/decisions/0001-dual-track-bufferlist-streamhub.md#L13-L27) defines a parity contract and acknowledges shared-kernel maintenance work. [EMA streaming](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/src/Indicators/e-j/Ema/EmaHub.cs#L30-L55) shares incremental arithmetic and uses SMA initialization. [Regression tests](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/tests/Library/Indicators/e-j/Ema/EmaRegressionTests.cs#L3-L15) compare Series, BufferList, and StreamHub with one baseline.

## Important limit

The [EMA documentation](https://github.com/facioquo/stock-indicators-dotnet/blob/9f0bece51eb45414dd75a02a3cab719ac9f9b12e/docs/indicators/ema.md#L27-L46) distinguishes minimum history from numerical convergence. Baseline agreement cannot establish correctness by itself, and the inspected regression fixture does not cover every late-arrival or rollback scenario.

## Questions to take into your own design

- Do batch and streaming paths agree after identical warm-up and initialization?
- Can an independently derived small fixture validate the common baseline?

## Why this score for a trading system

4/5: directly relevant financial parity source with explicit regression fixtures and warm-up documentation; the score is for this testing reference, not guaranteed correctness of every indicator.

**Scope of this review:** README, dual-track ADR, EMA documentation, EMA hub source, and three-path regression tests read.
