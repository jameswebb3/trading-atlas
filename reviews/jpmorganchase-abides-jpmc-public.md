# ABIDES JPMC — Can a simulated incoming order produce several fills at different prices

**Decision question:** Can a simulated incoming order produce several fills at different prices?

| Field | Review |
| --- | --- |
| Upstream | [ABIDES JPMC](https://github.com/jpmorganchase/abides-jpmc-public) |
| Primary area | Backtesting & Simulation |
| Source commit | [f9cbe51342b7dedd9587e4e069040d68a5c6477f](https://github.com/jpmorganchase/abides-jpmc-public/commit/f9cbe51342b7dedd9587e4e069040d68a5c6477f) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Models a crossing order as successive partial executions against resting prices, then retains the unmatched remainder. A useful fill-accounting oracle, with synthetic-book and integral-unit assumptions. |

## Project overview

A modular ABIDES distribution separating the simulation core, market environment and Gym interfaces. [Project documentation](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/README.md#L35-L46).

## Mechanism worth inspecting

The order book repeatedly executes a best available match, accumulates each quantity and price, and only rests the residual when no match remains. Matching assigns the advertised resting limit price and subtracts the executed quantity from the incoming order. [Partial-match loop](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/abides-markets/abides_markets/order_book.py#L75-L134); [fill price and quantity](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/abides-markets/abides_markets/order_book.py#L271-L304).

## Important limit

The inspected book checks integral positive quantities and integral nonnegative prices. Its synthetic matching environment does not reconstruct a live venue's queue from market-by-price snapshots. [Input checks](https://github.com/jpmorganchase/abides-jpmc-public/blob/f9cbe51342b7dedd9587e4e069040d68a5c6477f/abides-markets/abides_markets/order_book.py#L89-L105).

## Questions to take into your own design

- Does every partial execution retain its own price and quantity?
- Can the final residual and VWAP be reconstructed from those executions?

## Why this score for a trading system

4/5: directly exposes multi-price partial fills and residual quantity accounting, two critical simulation and execution contracts.

**Scope of this review:** The documented interface and the source path cited above; runtime behavior and unrelated project components were not evaluated.
