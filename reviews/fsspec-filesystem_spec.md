# fsspec — cache freshness is not content identity

**Decision question:** What makes a cached remote dataset the same dataset as the original?

| Field | Review |
| --- | --- |
| Upstream | [fsspec](https://github.com/fsspec/filesystem_spec) |
| Primary area | Data Quality & Lineage |
| Source commit | [6dee6af5c1b03cb02d9d5370bfebfba2f571166f](https://github.com/fsspec/filesystem_spec/commit/6dee6af5c1b03cb02d9d5370bfebfba2f571166f) |
| Reviewed | 2026-09-27 |
| Declared license | [BSD-3-Clause](https://github.com/fsspec/filesystem_spec/blob/6dee6af5c1b03cb02d9d5370bfebfba2f571166f/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Its cache policy exposes age and optional remote-identity checks. Those controls manage freshness; reproducible trading research still needs immutable dataset identity, especially when URLs or files can be replaced. |

## Project overview

fsspec provides a common filesystem interface and local caching implementations for different storage backends. [Project documentation](https://github.com/fsspec/filesystem_spec/blob/6dee6af5c1b03cb02d9d5370bfebfba2f571166f/README.md#L29-L33).

## Mechanism worth inspecting

The caching filesystem exposes remote UID checks and an expiry time, with `check_files=False` by default. Cache metadata rejects a record when a requested UID check differs or its age exceeds expiry. [Configuration](https://github.com/fsspec/filesystem_spec/blob/6dee6af5c1b03cb02d9d5370bfebfba2f571166f/fsspec/implementations/cached.py#L106-L140); [metadata check](https://github.com/fsspec/filesystem_spec/blob/6dee6af5c1b03cb02d9d5370bfebfba2f571166f/fsspec/implementations/cache_metadata.py#L85-L109).

## Important limit

A backend UID may represent file properties rather than an immutable digest of bytes, and the docs explicitly caution about unreliable HTTP content UIDs. Time-based expiry is also a freshness policy, not a reproducibility guarantee. Research needs an immutable content/version identity in addition to caching.

## Questions to take into your own design

- Does every stored input identify content or a stable upstream version independently of its path?
- Can remote replacement within the expiry window change the meaning of a replayed experiment?

## Why this score for a trading system

3/5: an inspectable freshness-versus-identity distinction, requiring immutable dataset provenance above backend-specific cache behavior.

**Scope of this review:** Caching options and metadata validity; filesystem implementations were not broadly audited.
