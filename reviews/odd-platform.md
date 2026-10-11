# ODD Platform: replace lineage claims by the producer that supplied them

**Decision question:** Can refreshing one producer's lineage accidentally delete another producer's evidence?

| Field | Review |
| --- | --- |
| Upstream | [ODD Platform](https://github.com/opendatadiscovery/odd-platform) |
| Primary area | Data Quality & Lineage |
| Source commit | [015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f](https://github.com/opendatadiscovery/odd-platform/commit/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/opendatadiscovery/odd-platform/blob/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f/LICENSE.md) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Catalogs data assets, quality evidence, and lineage. Its lineage replacement is scoped to the entity that established each relationship, allowing one producer's claims to be refreshed without treating the whole graph as a single snapshot. |

## Project overview

A data-discovery platform implements the Open Data Discovery specification and combines cataloging, lineage, pipeline monitoring, and quality integrations. [Project documentation](https://github.com/opendatadiscovery/odd-platform/blob/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f/README.md#L32-L71).

## Mechanism worth inspecting

The [lineage replacement method](https://github.com/opendatadiscovery/odd-platform/blob/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f/odd-platform-api/src/main/java/org/opendatadiscovery/oddplatform/service/LineageServiceImpl.java#L124-L133) derives establisher identities, deletes their prior claims, and inserts replacements under a transactional annotation. The [repository deletion](https://github.com/opendatadiscovery/odd-platform/blob/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f/odd-platform-api/src/main/java/org/opendatadiscovery/oddplatform/repository/reactive/ReactiveLineageRepositoryImpl.java#L44-L54) scopes deletion by ESTABLISHER_ODDRN. [Graph retrieval](https://github.com/opendatadiscovery/odd-platform/blob/015f6fa2dac9b6d0dfd00b6b6d9baab9329e6c4f/odd-platform-api/src/main/java/org/opendatadiscovery/oddplatform/service/LineageServiceImpl.java#L88-L119) also makes traversal depth and direction explicit.

## Important limit

An empty list identifies no establishers to clear; absence of incoming edges cannot by itself mean that every prior claim vanished. The inspected retrieval code merges expanded relations and deduplicates them, but graph visibility does not certify that producers reported all dependencies.

## Questions to take into your own design

- Does every lineage edge retain who asserted it and which run supplied the assertion?
- Can a producer explicitly publish an empty authoritative relationship set?

## Why this score for a trading system

3/5: a specific reusable ownership model for lineage refresh and impact analysis. It requires producer completeness and empty-refresh semantics outside the inspected method.

**Scope of this review:** README features, lineage retrieval/replacement service, and establisher-scoped repository query.
