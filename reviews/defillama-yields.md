# DefiLlama Yields: separate yield components and identify the actual asset

**Decision question:** Can a pool metric distinguish its receipt token, underlying assets, and incentive component?

| Field | Review |
| --- | --- |
| Upstream | [DefiLlama Yields](https://github.com/DefiLlama/yield-server) |
| Primary area | Data Quality & Lineage |
| Source commit | [accc8c8cf95182457731e7bdf5195a1552da0b93](https://github.com/DefiLlama/yield-server/commit/accc8c8cf95182457731e7bdf5195a1552da0b93) |
| Reviewed | 2026-09-26 |
| Declared license | [ISC declared in package.json](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/package.json#L15) |
| Review depth | 3/3: documentation, handler source, and adapter validation tests read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Defines separate base and reward yields, explicit pool identifiers, and token roles. Its handler preserves an explicit null token instead of guessing an address, avoiding misleading holder attribution for debt positions. |

## Project overview

An adapter-backed yield dataset standardizes pool identifiers, TVL, yield components, and token metadata. Its methodology excludes several forms of boosted or locked rewards. [Project documentation](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/README.md#L9-L60).

## Mechanism worth inspecting

The [schema documentation](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/README.md#L67-L88) distinguishes receipt-token identity from underlying assets and documents debt positions with no transferable receipt token. The [production handler](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/src/handlers/triggerAdaptor.js#L331-L343) respects an explicitly supplied token, including null; only an absent field invokes [address extraction](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/src/handlers/triggerAdaptor.js#L445-L450). The [validation suite](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/src/adaptors/test.js#L87-L117) checks identifier uniqueness and finite yield/TVL values.

## Important limit

A syntactically plausible address extracted from a pool name need not identify its receipt token. The [methodology](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/README.md#L17-L27) defines the intended yield but schema checks do not reconstruct attainable historical yield or its publication time. [Display filters](https://github.com/DefiLlama/yield-server/blob/accc8c8cf95182457731e7bdf5195a1552da0b93/README.md#L114-L126) also affect which pools a visitor sees.

## Questions to take into your own design

- Are absent identity, explicit no-token identity, and unknown identity represented differently?
- Can base yield, token incentives, observation time, and display exclusions be audited separately?

## Why this score for a trading system

3/5: useful for interpreting on-chain metrics and designing explicit asset contracts. DeFi yield does not itself establish a tradable signal or historical availability.

**Scope of this review:** README methodology and schema, production normalization handler, and selected adapter contract tests.
