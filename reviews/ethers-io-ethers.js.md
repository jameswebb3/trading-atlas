# ethers.js — repeated RPC calls may share one observation

**Decision question:** Are two nearby RPC responses independent observations of chain state?

| Field | Review |
| --- | --- |
| Upstream | [ethers.js](https://github.com/ethers-io/ethers.js) |
| Primary area | Market Data & Ingestion |
| Source commit | [3ea4c226dd0b3a074abf90748de9d11192027f4f](https://github.com/ethers-io/ethers.js/commit/3ea4c226dd0b3a074abf90748de9d11192027f4f) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/ethers-io/ethers.js/blob/3ea4c226dd0b3a074abf90748de9d11192027f4f/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A clear RPC caching boundary: nearby identical requests can share a result. Useful for designing freshness evidence that records provider, block and observation identity rather than merely counting successful calls. |

## Project overview

ethers.js is a TypeScript library for Ethereum interaction, including providers, contracts and transaction handling. [Project documentation](https://github.com/ethers-io/ethers.js/blob/3ea4c226dd0b3a074abf90748de9d11192027f4f/README.md#L13-L14).

## Mechanism worth inspecting

The abstract provider caches identical low-level requests as promises. Its default timeout is 250 milliseconds; repeated calls with the same request tag can reuse one result during that interval. Negative timeout disables this cache. [Options](https://github.com/ethers-io/ethers.js/blob/3ea4c226dd0b3a074abf90748de9d11192027f4f/src.ts/providers/abstract-provider.ts#L412-L430); [request sharing](https://github.com/ethers-io/ethers.js/blob/3ea4c226dd0b3a074abf90748de9d11192027f4f/src.ts/providers/abstract-provider.ts#L585-L612).

## Important limit

A second successful call is not necessarily a fresh independent node observation. Disabling request sharing does not establish finality or provider agreement either. Data consumers should record block identity, provider identity and observation time rather than treating call count as freshness evidence.

## Questions to take into your own design

- Do freshness and quorum checks count independent provider/block observations rather than API calls?
- Is request caching an explicit part of the collector's provenance and latency contract?

## Why this score for a trading system

3/5: a relevant RPC observation-identity reference, with canonicality and independent-provider evidence still required above the SDK.

**Scope of this review:** Abstract-provider low-level request caching; wallet and contract functionality were not evaluated.
