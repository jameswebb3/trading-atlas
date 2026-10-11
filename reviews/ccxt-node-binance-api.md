# Node Binance API — False is not an omitted setting

**Decision question:** Does an explicit false survive configuration defaults?

| Field | Review |
| --- | --- |
| Upstream | [Node Binance API](https://github.com/ccxt/node-binance-api) |
| Primary area | Execution & Exchange Integration |
| Source commit | [ce12132843c1ce712890bd3167da1acddca61dc9](https://github.com/ccxt/node-binance-api/commit/ce12132843c1ce712890bd3167da1acddca61dc9) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/ccxt/node-binance-api/blob/ce12132843c1ce712890bd3167da1acddca61dc9/LICENSE) |
| Review depth | 2/3: documentation, relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | The public options path reaches setOptions and then assignOptions. At this pinned source, reconnect=false is replaced by the true default. |

## Project overview

JavaScript/TypeScript client for Binance market data, WebSockets and trading APIs. [Documentation](https://github.com/ccxt/node-binance-api/blob/ce12132843c1ce712890bd3167da1acddca61dc9/README.md).

## Mechanism worth inspecting

The public options path reaches setOptions and then assignOptions. That helper uses falsy checks to install defaults, including reconnect=true. [Source](https://github.com/ccxt/node-binance-api/blob/ce12132843c1ce712890bd3167da1acddca61dc9/src/node-binance-api.ts#L162-L208).

## Important limit

At this pinned source, reconnect=false is replaced by the true default. This observation concerns the configuration path inspected, not every stream or reconnect implementation. [Evidence 1](https://github.com/ccxt/node-binance-api/blob/ce12132843c1ce712890bd3167da1acddca61dc9/src/node-binance-api.ts#L162-L208). [Evidence 2](https://github.com/ccxt/node-binance-api/blob/ce12132843c1ce712890bd3167da1acddca61dc9/src/node-binance-api.ts#L240-L247).

## Questions to take into your own design

- Do false, zero and missing have separate configuration semantics?
- Does a post-merge receipt show the effective setting?

## Why this score for a trading system

A concrete exchange-client configuration boundary with operational consequences; it supplies no new strategy and requires no SDK adoption.

**Scope of this review:** The linked documentation, source paths and line ranges above. Conclusions apply to the described mechanism at this commit; unlinked components were not assessed. No behavior or test suite was executed.
