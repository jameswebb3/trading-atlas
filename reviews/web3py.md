# web3.py: bounded log scanning

**Decision question:** What is needed beyond an RPC client to build a resumable Ethereum event dataset?

| Field | Review |
| --- | --- |
| Upstream | [web3.py](https://github.com/ethereum/web3.py) |
| Primary area | Market Data & Ingestion |
| Source commit | [d8ac0c118e74745f1837bddb467046e87e2203be](https://github.com/ethereum/web3.py/commit/d8ac0c118e74745f1837bddb467046e87e2203be) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Provides RPC and ABI access plus practical log-scanning examples. The middleware handles inclusive block-range boundaries; the documented scanner shrinks failing requests and rescans recent blocks. |

## Project overview

Python library for Ethereum RPC and smart-contract interaction. Its filtering code and event-scanner documentation offer concrete examples of bounded log requests, adaptive retries, and incremental collection. [Project documentation](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/README.md#L9-L13).

## Mechanism worth inspecting

[The filter middleware](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/web3/middleware/filter.py#L115-L133) converts half-open segments into non-overlapping inclusive RPC ranges. [RequestLogs](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/web3/middleware/filter.py#L271-L303) joins the resulting bounded requests. This is a small but material boundary condition for historical extracts: adjacent batches must not omit or duplicate their shared endpoint.

[The advanced scanner documentation](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/docs/filters.rst#L394-L439) covers interruptions, RPC result limits, and incremental state. Its [retry example](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/docs/filters.rst#L757-L792) halves the end range after a failed request and returns the end actually fetched. Persisting that completed end instead of the originally requested end is the pattern worth carrying into a custom collector.

## Important limit

[The example's restart rule](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/docs/filters.rst#L576-L603) rescans a fixed recent tail and describes that approach as a simple heuristic. It does not prove repair for an arbitrary fork or supply production storage transactions. [The middleware](https://github.com/ethereum/web3.py/blob/d8ac0c118e74745f1837bddb467046e87e2203be/web3/middleware/filter.py#L245-L250) defaults a new latest filter to the next block, so it is not an automatic historical backfill. An RPC client supplies access and decoding; the consumer must retain receipts, canonical hashes, and publication or observation times.

## Questions to take into your own design

- After range shrinkage, is progress advanced only to the returned end block?
- Does the overlap-rescan policy verify hashes and replace all affected derived rows?

## Why this score for a trading system

Exact range boundaries and adaptive collection are direct market-data concerns, but the inspected client and example do not provide an end-to-end durable, reorg-safe dataset.

**Scope of this review:** README, advanced event-scanner documentation/code example, and local filter middleware; transaction signing, provider security, and runtime RPC behavior were not evaluated.
