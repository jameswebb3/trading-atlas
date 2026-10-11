# data-diff: localize changes between data copies

**Decision question:** Can a table comparison localize changed rows without copying both datasets?

| Field | Review |
| --- | --- |
| Upstream | [datafold/data-diff](https://github.com/datafold/data-diff) |
| Primary area | Data Quality & Lineage |
| Source commit | [1410c6cd0b915ae24a15e03a7de15ff41beebaf0](https://github.com/datafold/data-diff/commit/1410c6cd0b915ae24a15e03a7de15ff41beebaf0) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Compares per-segment counts and checksums, then bisects mismatched key ranges and downloads only small leaves. Only selected columns are checked, precision may be reduced across sources, and maintainers stopped development in 2024. |

## Mechanism worth inspecting

The [technical explanation](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/docs/technical-explanation.md#L3-L18) distinguishes same-database joins from cross-database hash bisection. The pinned [hash differ](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/data_diff/hashdiff_tables.py#L185-L215) compares count and checksum for a key range and descends only when they differ. At a small leaf it [downloads and compares rows](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/data_diff/hashdiff_tables.py#L228-L262). This is a concrete pattern for checking two market-data copies after a migration without copying every row first.

## Important limits

The comparison covers the columns chosen for hashing. The [precision normalization path](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/data_diff/hashdiff_tables.py#L118-L158) can reduce both sides to their lowest common precision and logs a warning; as an inference, a smaller numeric difference could disappear from the comparison. The [README notice](https://github.com/datafold/data-diff/blob/1410c6cd0b915ae24a15e03a7de15ff41beebaf0/README.md#L1-L5) says maintainers stopped actively supporting or developing this open-source project in May 2024. The pattern is worth studying; adopting an unmaintained tool would carry a different cost.

## Questions to take into your own design

- Are the compared keys stable and all decision-relevant columns included?
- Does normalization discard precision that matters for prices or sizes?
- Were both source snapshots fixed while the comparison ran?

## Why this score for a trading system

Segmented reconciliation is useful for comparing two trading-data copies, but selected-column and precision limits plus discontinued maintenance reduce its reference value.

**Scope of this review:** We read the pinned README, technical explanation, and selected implementation. We did not install or run data-diff, benchmark it, inspect every database driver, or establish behavior beyond this archived commit.
