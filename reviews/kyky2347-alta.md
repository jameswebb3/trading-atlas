# ALTA — Can a delayed read overwrite a newer broker view

**Decision question:** Can a delayed read overwrite a newer broker view?

| Field | Review |
| --- | --- |
| Upstream | [ALTA](https://github.com/kyky2347/ALTA) |
| Primary area | Operations & Observability |
| Source commit | [68c31c4b713335eb7f68892f3c90699f52c03502](https://github.com/kyky2347/ALTA/commit/68c31c4b713335eb7f68892f3c90699f52c03502) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/kyky2347/ALTA/blob/68c31c4b713335eb7f68892f3c90699f52c03502/LICENSE) |
| Review depth | 3/3: documentation, relevant implementation and tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A compact reference for preventing delayed polls from overwriting a newer operator view. Keep this display guarantee separate from exchange reconciliation and server-side authorization. |

## Project overview

A trading-agent application with broker routing and revision-aware interface state. [Project documentation](https://github.com/kyky2347/ALTA/blob/68c31c4b713335eb7f68892f3c90699f52c03502/docs/audits/broker-routing-2026-09-13.md).

## Mechanism worth inspecting

The [snapshot fence](https://github.com/kyky2347/ALTA/blob/68c31c4b713335eb7f68892f3c90699f52c03502/alta-dashboard/src/lib/snapshot-fence.ts#L1-L16) assigns revisions to reads and invalidates older responses. Its [tests](https://github.com/kyky2347/ALTA/blob/68c31c4b713335eb7f68892f3c90699f52c03502/alta-dashboard/tests/snapshot-fence.test.mjs#L1-L19) cover a poll returning after a mutation.

## Important limit

The fence protects local display ordering. It does not independently establish exchange freshness, server permissions or the correctness of an external order.

## Questions to take into your own design

- Can a delayed read overwrite a newer broker view?
- Can any poll started before a broker mutation replace the view after that mutation?

## Why this score for a trading system

3/5: a small, tested interface pattern; it does not justify confidence in the full autonomous trading application.

**Scope of this review:** Focused reading of the linked documentation and implementation plus cited tests (read, not executed). Other subsystems and runtime behavior were not assessed.
