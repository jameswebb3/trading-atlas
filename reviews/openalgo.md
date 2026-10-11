# A successful cancel service response is not a fill-history receipt

**Decision question:** Which evidence turns a broker cancellation response into a closed order?

| Field | Review |
| --- | --- |
| Upstream | [OpenAlgo](https://github.com/marketcalls/openalgo) |
| Primary area | Execution & Exchange Integration |
| Source commit | [e78f2edee924141b8ff57a37da26132f5447fd5b](https://github.com/marketcalls/openalgo/commit/e78f2edee924141b8ff57a37da26132f5447fd5b) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/marketcalls/openalgo/blob/e78f2edee924141b8ff57a37da26132f5447fd5b/License.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The cancel service emits OrderCancelledEvent and returns success when the broker module returns HTTP 200. It does not query order status within that branch. That is a useful adapter-contract question: determine whether each broker response means request acceptance or confirmed cancellation, then reconcile fills. |

## Mechanism worth inspecting

The [overview](https://github.com/marketcalls/openalgo/blob/e78f2edee924141b8ff57a37da26132f5447fd5b/README.md#L13-L29) describes shared broker services. The [status API](https://github.com/marketcalls/openalgo/blob/e78f2edee924141b8ff57a37da26132f5447fd5b/docs/api/order-information/orderstatus.md#L1-L3) is a separate query. The [cancel branch](https://github.com/marketcalls/openalgo/blob/e78f2edee924141b8ff57a37da26132f5447fd5b/services/cancel_order_service.py#L133-L158) relies on the adapter's status code, emits a cancellation event, and returns without invoking that status query.

## Important limit

HTTP 200 can be valid terminal evidence for some adapters; this review does not claim every broker is wrong. The service-level event alone does not show the venue's contract, fill completeness, or subsequent reconciliation.

## Questions to take into your own design

- For this adapter, does HTTP 200 confirm terminal cancellation or only accept the request?
- Which path accounts for fills that raced the cancellation?

## Why this score for a trading system

3/5: The inspected response-to-event boundary is directly useful for auditing cancellation contracts across adapters.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
