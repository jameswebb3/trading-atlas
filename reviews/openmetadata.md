# OpenMetadata: a registered contract is not an enforced contract

**Decision question:** Which schema violations count as failures in a data-contract validation?

| Field | Review |
| --- | --- |
| Upstream | [OpenMetadata](https://github.com/open-metadata/OpenMetadata) |
| Primary area | Data Quality & Lineage |
| Source commit | [37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030](https://github.com/open-metadata/OpenMetadata/commit/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Connects data assets, lineage, ownership, quality, and versioned contracts. Its schema validation distinguishes missing fields, duplicates, and type mismatches, but the inspected path treats type mismatches as informational rather than failed checks. |

## Project overview

A metadata platform catalogs data assets, semantics, ownership, lineage, quality signals, and data contracts. [Project documentation](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/README.md#L9-L28).

## Mechanism worth inspecting

The [contract schema](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/openmetadata-spec/src/main/resources/json/schema/entity/data/dataContract.json#L10-L55) records contract lifecycle and timestamped versions. [Schema validation](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/openmetadata-service/src/main/java/org/openmetadata/service/jdbi3/DataContractRepository.java#L454-L504) returns separate missing, duplicate, and type-mismatch fields. The [table comparison](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/openmetadata-service/src/main/java/org/openmetadata/service/jdbi3/DataContractRepository.java#L527-L552) distinguishes absent columns from incompatible types.

## Important limit

The validation deliberately excludes type mismatches from failedCount. [Contract preparation](https://github.com/open-metadata/OpenMetadata/blob/37c5e037ea2df9c0ac291d9cd9a0b2ec2c4df030/openmetadata-service/src/main/java/org/openmetadata/service/jdbi3/DataContractRepository.java#L172-L198) also documents that these mismatches do not block creation. A contract stored in a catalog is therefore not evidence that a consumer enforces its intended types, units, or availability rules.

## Questions to take into your own design

- Does the acceptance gate use detailed violations, or only a summary failure count?
- Are descriptive expectations, informational warnings, and blocking invariants explicitly different?

## Why this score for a trading system

3/5: a concrete versioned contract/result model and an important distinction between registration and enforcement. The broader catalog is generic infrastructure with substantial integration scope.

**Scope of this review:** README, contract JSON schema, documented design patterns treated as source data, and schema validation/preparation code; no platform deployed.
