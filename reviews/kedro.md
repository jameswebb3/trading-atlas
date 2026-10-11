# Kedro: keep dataset versions explicit across a pipeline run

**Decision question:** Does a pipeline catalog prevent mixed output-version labels?

| Field | Review |
| --- | --- |
| Upstream | [kedro-org/kedro](https://github.com/kedro-org/kedro) |
| Primary area | Research & Reproducibility |
| Source commit | [8d9abdf02b1ce93fbe9079cff6f696fb230facc4](https://github.com/kedro-org/kedro/commit/8d9abdf02b1ce93fbe9079cff6f696fb230facc4) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/LICENSE.md) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Uses named datasets and checks that versioned outputs in one catalog share the same save-version label. Loads default to the latest version unless the caller pins each input; matching labels do not prove matching bytes. |

## Mechanism worth inspecting

The [README](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/README.md#L24-L28) describes modular data pipelines. The [catalog guide](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/docs/catalog-data/data_catalog.md#L1-L18) maps node inputs and outputs to named datasets. Its [version guide](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/docs/catalog-data/how_to_configure_the_data_catalog.md#L89-L108) says runs load the latest dataset version by default and can pin a named input version. The pinned [catalog validation](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/kedro/io/data_catalog.py#L1323-L1371) raises when versioned datasets disagree on the save-version label. The [configuration API](https://github.com/kedro-org/kedro/blob/8d9abdf02b1ce93fbe9079cff6f696fb230facc4/kedro/io/data_catalog.py#L678-L710) has separate load versions and one output save version.

For research, this suggests recording explicit versions for every market input and a common output run label.

## Important limit

A common save-version string is a consistency check on names, not a content hash or proof that each input was available at decision time. Loading latest is convenient but makes a replay depend on when it runs unless versions are pinned.

## Questions to take into your own design

- Are input versions explicit rather than implicit latest?
- Does one experiment identify every output from the same run?
- Are version labels bound to hashes or immutable object IDs?

## Why this score for a trading system

The catalog version guard transfers to reproducible trading research, but version labels alone do not identify data bytes or prevent time leakage.

**Scope of this review:** We read pinned README, catalog documentation, and selected catalog code. We did not install or run Kedro or inspect every dataset adapter.
