# Toxiproxy — Can an order execute while its response is delayed or lost

**Decision question:** Can an order execute while its response is delayed or lost?

| Field | Review |
| --- | --- |
| Upstream | [Toxiproxy](https://github.com/Shopify/toxiproxy) |
| Primary area | Testing & Verification |
| Source commit | [40f7fd31bee529d824116bd2a11a9e3425e904ec](https://github.com/Shopify/toxiproxy/commit/40f7fd31bee529d824116bd2a11a9e3425e904ec) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/Shopify/toxiproxy/blob/40f7fd31bee529d824116bd2a11a9e3425e904ec/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful fault-injection reference for separating request delivery from response delivery. Delayed or dropped acknowledgments need an order-state oracle; a socket failure alone cannot tell whether the exchange acted. |

## Project overview

Toxiproxy applies configurable faults to TCP traffic, separately for requests and responses. [Project documentation](https://github.com/Shopify/toxiproxy/blob/40f7fd31bee529d824116bd2a11a9e3425e904ec/README.md#L7-L19).

## Mechanism worth inspecting

The API distinguishes upstream client-to-server faults from downstream server-to-client faults. The latency toxic delays chunks using explicit millisecond latency and jitter, accounting for elapsed chunk time. [Directions](https://github.com/Shopify/toxiproxy/blob/40f7fd31bee529d824116bd2a11a9e3425e904ec/README.md#L486-L495), [delay implementation](https://github.com/Shopify/toxiproxy/blob/40f7fd31bee529d824116bd2a11a9e3425e904ec/toxics/latency.go#L19-L48).

## Important limit

Transport faults do not identify application-level order outcomes. Trading tests must record whether the remote action occurred and inject a reconciliation path, rather than infer rejection from a missing response.

## Questions to take into your own design

- Can an order execute while its response is delayed or lost?
- Can the test oracle distinguish an unreceived request from an executed request with a lost response?

## Why this score for a trading system

3/5: concrete transferable network fault seam, with trading state and safe retry policy deliberately outside the proxy.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
