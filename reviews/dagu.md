# Dagu: make catch-up windows and dropped schedule intervals visible

**Decision question:** After a scheduler outage, which missed runs are actually replayed?

| Field | Review |
| --- | --- |
| Upstream | [Dagu](https://github.com/dagucloud/dagu) |
| Primary area | Operations & Observability |
| Source commit | [1a76b62f62e632d5ed2371a89ab3df90da2e1da7](https://github.com/dagucloud/dagu/commit/1a76b62f62e632d5ed2371a89ab3df90da2e1da7) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0-or-later](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Calculates bounded schedule catch-up from a replay window and previous scheduling state. Useful for data and research jobs; the implementation retains only the most recent 1,000 missed intervals, so catch-up must not be mistaken for complete recovery. |

## Project overview

Self-hosted workflow engine for scheduling existing scripts with dependencies, retries, and run history. Its single-binary, file-backed design needs no external database or message broker.

[Project documentation](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/README.md#L18-L31).

## Mechanism worth inspecting

The [README](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/README.md#L18-L31) describes a local workflow scheduler, and the [schema guide](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/README_SCHEMA.md#L63-L91) separates workflow controls from steps. The [catch-up implementation](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/internal/service/scheduler/catchup.go#L13-L34) begins at the latest of window start, last tick, and last scheduled time. It [enumerates and deduplicates intervals](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/internal/service/scheduler/catchup.go#L54-L77), then [sorts and retains the most recent 1,000](https://github.com/dagucloud/dagu/blob/1a76b62f62e632d5ed2371a89ab3df90da2e1da7/internal/service/scheduler/catchup.go#L80-L87).

## Important limit

The cap is applied after interval collection. More importantly for data coverage, a bounded replay window and the retained suffix are deliberate omissions. Successful scheduled execution does not prove every expected market-data interval exists. For order submission, replaying a missed schedule requires a separate safety decision; historical data catch-up and live order replay have different consequences.

## Questions to take into your own design

- Does recovery publish the exact interval set omitted by the window or replay cap?
- Which jobs are safe to backfill, and which should expire rather than run after their decision deadline?

## Why this score for a trading system

3/5: a transferable recovery pattern with explicit timing and truncation behaviour. Data completeness and safe treatment of stale trading decisions remain application responsibilities.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
