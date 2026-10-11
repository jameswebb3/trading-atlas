# Require an adapter to own its order-event semantics

**Decision question:** Should a generic order manager guess an exchange's client-ID format?

| Field | Review |
| --- | --- |
| Upstream | [Banbot](https://github.com/banbox/banbot) |
| Primary area | Execution & Exchange Integration |
| Source commit | [7a5e3097ec68a80cf6c05bdfe5306510ad2425ab](https://github.com/banbox/banbot/commit/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab) |
| Reviewed | 2026-09-26 |
| Declared license | [AGPL-3.0](https://github.com/banbox/banbot/blob/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab/LICENSE) |
| Review depth | 3/3: documentation, relevant source, and focused tests read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Banbot defines an adapter capability for client-ID parsing, event order identity, and timestamp normalization. In strict mode it rejects adapters that do not implement that capability. This is a useful boundary for exchange integration; capability presence still needs behavioral conformance tests. |

## Mechanism worth inspecting

The [README](https://github.com/banbox/banbot/blob/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab/README.md#L18-L29) describes shared trading modes and exchange adapters; the [documentation overview](https://github.com/banbox/banbot/blob/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab/bandoc/README.md#L1-L6) identifies the separate guide. The [capability gate](https://github.com/banbox/banbot/blob/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab/exg/order_events.go#L9-L58) separates native semantics from compatibility fallback. The [tests](https://github.com/banbox/banbot/blob/7a5e3097ec68a80cf6c05bdfe5306510ad2425ab/exg/order_events_test.go#L22-L57) verify strict rejection and a fallback that does not guess client or algorithmic order IDs.

## Important limit

An interface check proves that methods exist, not that the adapter handles duplicate, late, partial, or contradictory events correctly. The inspected gate does not establish complete account-history reconciliation.

## Questions to take into your own design

- Does each adapter have fixtures for its exact ID and timestamp semantics?
- Can compatibility fallback remain disabled in live mode?

## Why this score for a trading system

4/5: An explicit venue-semantic gate addresses a direct order-state risk, with focused tests and clearly bounded guarantees.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
