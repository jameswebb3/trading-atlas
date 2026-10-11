# An immutable dataset can still contain a mutable file reference

**Decision question:** Does a saved file fingerprint identify the actual bytes behind an experiment?

| Field | Review |
| --- | --- |
| Upstream | [DataChain](https://github.com/datachain-ai/datachain) |
| Primary area | Research & Reproducibility |
| Source commit | [0509279ffd26a187ae9525bf039cc57d88090984](https://github.com/datachain-ai/datachain/commit/0509279ffd26a187ae9525bf039cc57d88090984) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/datachain-ai/datachain/blob/0509279ffd26a187ae9525bf039cc57d88090984/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | DataChain versions datasets, but its File.get_hash fingerprints source, path, version, ETag, and optional location rather than reading file bytes. That is useful identity metadata, not automatically a content checksum. Reproducible trading inputs need storage-version guarantees or independent byte digests. |

## Mechanism worth inspecting

The [README](https://github.com/datachain-ai/datachain/blob/0509279ffd26a187ae9525bf039cc57d88090984/README.md#L33-L37) places local and object-storage files in a query pipeline. The [dataset guide](https://github.com/datachain-ai/datachain/blob/0509279ffd26a187ae9525bf039cc57d88090984/docs/concepts/datasets.md#L9-L20) promises immutable saved versions. The [file model](https://github.com/datachain-ai/datachain/blob/0509279ffd26a187ae9525bf039cc57d88090984/src/datachain/lib/file.py#L212-L231) permits empty version and ETag fields, and its [hash function](https://github.com/datachain-ai/datachain/blob/0509279ffd26a187ae9525bf039cc57d88090984/src/datachain/lib/file.py#L1039-L1043) hashes a metadata string.

## Important limit

The observation concerns this file-identity helper, not every storage backend's integrity mechanism. An immutable record pointing at mutable storage does not by itself pin bytes or show historical publication time.

## Questions to take into your own design

- Are external objects versioned and retrievable at the recorded version?
- Can the manifest distinguish a byte checksum from a metadata-derived fingerprint?

## Why this score for a trading system

3/5: Separating reference identity from consumed-byte identity is a useful reproducibility pattern for trading datasets.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
