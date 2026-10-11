# TrueBlocks chifra: validate the index as well as its manifest

**Decision question:** Which checks establish index coverage, and which only establish plausible metadata?

| Field | Review |
| --- | --- |
| Upstream | [TrueBlocks chifra](https://github.com/TrueBlocks/trueblocks-chifra) |
| Primary area | Market Data & Ingestion |
| Source commit | [ff9df4fc2ae8e884304bd527b89e0486ccffa3e9](https://github.com/TrueBlocks/trueblocks-chifra/commit/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9) |
| Reviewed | 2026-09-26 |
| Declared license | [GPL-3.0](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 4/5 |
| Trading-system fit | Direct |
| Verdict | Indexes address appearances and exposes separate checks for chunk coverage, manifest fields, and Bloom-filter consistency. The distinction is useful when validating a large local index: a well-formed manifest alone proves little about its contents. |

## Project overview

The TrueBlocks command interface provides address histories, cached chain queries, and tools for inspecting the Unchained Index. [Project documentation](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/README.md#L9-L30).

## Mechanism worth inspecting

The [chunk documentation](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/internal/chunks/README.md#L1-L49) separates ordinary consistency checks from deep inspection. [Range validation](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/internal/chunks/handle_check_sequential.go#L37-L70) reports overlaps, gaps, reversed ranges, and duplicates. [Deep index inspection](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/internal/chunks/handle_check_deep.go#L57-L98) reads indexed addresses and checks their corresponding Bloom filter. Each check answers a different question about the stored dataset.

## Important limit

The function called [CheckHashes](https://github.com/TrueBlocks/trueblocks-chifra/blob/ff9df4fc2ae8e884304bd527b89e0486ccffa3e9/internal/chunks/handle_check_hashes.go#L14-L51) checks hash-string lengths rather than recomputing content hashes. Bloom membership validates consistency between two artifacts; it does not prove that all relevant chain appearances were collected. Range checking also has an explicit allow-missing caveat.

## Questions to take into your own design

- Does each validation result state whether it checked syntax, artifact consistency, or chain completeness?
- Can a missing or overlapping chunk be detected independently of a valid-looking manifest?

## Why this score for a trading system

4/5: concrete index-validation mechanisms with clearly inspectable scopes. These patterns directly support reproducible on-chain datasets, while full chain completeness still needs independent evidence.

**Scope of this review:** CLI README, chunk documentation, and sequential, hash-field, and deep index check implementations. The umbrella trueblocks-core repository delegates this implementation to a submodule.
