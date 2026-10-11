# Nethermind — How should a collector handle an RPC scan limit

**Decision question:** How should a collector handle an RPC scan limit?

| Field | Review |
| --- | --- |
| Upstream | [Nethermind](https://github.com/NethermindEth/nethermind) |
| Primary area | Market Data & Ingestion |
| Source commit | [cc1cd4af17d8636468d927e9a11fa61edf9d8597](https://github.com/NethermindEth/nethermind/commit/cc1cd4af17d8636468d927e9a11fa61edf9d8597) |
| Reviewed | 2026-09-26 |
| Declared license | [LGPL-3.0-only on inspected file; repository includes GPL/LGPL components](https://github.com/NethermindEth/nethermind/blob/cc1cd4af17d8636468d927e9a11fa61edf9d8597/LICENSE-LGPL) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A practical Ethereum log-ingestion reference: expensive fallback scans are bounded explicitly. Collectors must distinguish range rejection from a valid empty response and record the coverage of each successful batch. |

## Project overview

Nethermind is an Ethereum execution client. Its log-query layer includes a guard for ranges that cannot be answered efficiently through the index. [Project documentation](https://github.com/NethermindEth/nethermind/blob/cc1cd4af17d8636468d927e9a11fa61edf9d8597/README.md).

## Mechanism worth inspecting

RangeLimitedLogFinder counts the requested blocks outside usable index coverage and throws when the sequential scan exceeds the configured maximum. A disabled limit explicitly bypasses the gate. [Range contract](https://github.com/NethermindEth/nethermind/blob/cc1cd4af17d8636468d927e9a11fa61edf9d8597/src/Nethermind/Nethermind.Facade/Find/RangeLimitedLogFinder.cs#L15-L83).

## Important limit

An RPC range rejection is not an empty result. A collector must subdivide and account for coverage; successful bounded queries still need block identity and finality handling.

## Questions to take into your own design

- How should a collector handle an RPC scan limit?
- How are rejected RPC ranges split without losing or duplicating block coverage?

## Why this score for a trading system

3/5: concrete on-chain query semantics that affect completeness; reviewing this guard does not establish whole-client correctness or archival coverage.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
