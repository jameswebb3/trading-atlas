# Apache Iceberg — Will an experiment's named dataset still exist when it must be reproduced

**Decision question:** Will an experiment's named dataset still exist when it must be reproduced?

| Field | Review |
| --- | --- |
| Upstream | [Apache Iceberg](https://github.com/apache/iceberg) |
| Primary area | Data Quality & Lineage |
| Source commit | [ac16c2950b298c8725f57cc8d34f8690d452ef57](https://github.com/apache/iceberg/commit/ac16c2950b298c8725f57cc8d34f8690d452ef57) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/apache/iceberg/blob/ac16c2950b298c8725f57cc8d34f8690d452ef57/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | A useful data-versioning reference for explicit retention of experiment inputs. Named snapshots need a retention contract; an experiment label alone does not ensure that its data remains reproducible. |

## Project overview

Iceberg manages analytical tables through snapshots, with named branches and tags and explicit retention policies. [Project documentation](https://github.com/apache/iceberg/blob/ac16c2950b298c8725f57cc8d34f8690d452ef57/docs/docs/branching.md#L26-L40).

## Mechanism worth inspecting

Snapshot expiration retains main, then keeps other references only if their snapshot exists and its age satisfies the reference policy. [Retention implementation](https://github.com/apache/iceberg/blob/ac16c2950b298c8725f57cc8d34f8690d452ef57/core/src/main/java/org/apache/iceberg/RemoveSnapshots.java#L278-L300). The docs distinguish reference retention from snapshot lifecycle. [Lifecycle](https://github.com/apache/iceberg/blob/ac16c2950b298c8725f57cc8d34f8690d452ef57/docs/docs/branching.md#L26-L35).

## Important limit

A tag with a finite retention policy is not a permanent reproducibility guarantee. Table snapshots also do not preserve code, features or external artifacts outside the table.

## Questions to take into your own design

- Will an experiment's named dataset still exist when it must be reproduced?
- Which retention rule preserves every dataset snapshot referenced by an experiment?

## Why this score for a trading system

3/5: precise transferable dataset lifecycle, without a trading-specific experiment manifest or protection for artifacts outside the table.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
