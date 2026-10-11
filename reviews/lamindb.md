# LaminDB: static lineage checks expose untracked file paths

**Decision question:** Can a script claim lineage while reading an unregistered file?

| Field | Review |
| --- | --- |
| Upstream | [LaminDB](https://github.com/laminlabs/lamindb) |
| Primary area | Data Quality & Lineage |
| Source commit | [9c3c9ca82cc7defd50733a5dcf705192f000e6ba](https://github.com/laminlabs/lamindb/commit/9c3c9ca82cc7defd50733a5dcf705192f000e6ba) |
| Reviewed | 2026-09-25 |
| Declared license | [Apache-2.0](https://github.com/laminlabs/lamindb/blob/9c3c9ca82cc7defd50733a5dcf705192f000e6ba/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | Statically checks a script for tracking lifecycle calls and path-like file usage outside tracked artifact calls, then reports source lines. This is a useful missing-lineage alarm, but AST analysis cannot prove that runtime data actually matched the registered artifact. |

## Mechanism worth inspecting

The [overview](https://github.com/laminlabs/lamindb/blob/9c3c9ca82cc7defd50733a5dcf705192f000e6ba/README.md#L3-L42) centers traceable data and runs. The [architecture notes](https://github.com/laminlabs/lamindb/blob/9c3c9ca82cc7defd50733a5dcf705192f000e6ba/docs/architecture.md#L131-L169) describe metadata-backed snapshot history. The [verify_lineage implementation](https://github.com/laminlabs/lamindb/blob/9c3c9ca82cc7defd50733a5dcf705192f000e6ba/lamindb/core/_verify_lineage.py#L357-L435) parses one script, requires tracking start and finish calls, and reports path-like strings used in untracked calls with line numbers. Missing files and syntax errors are reported as failed checks.

## Important limit

The code itself calls this a static AST check. It excludes setup/path helpers, and dynamic paths or external tools can escape the analyzed syntax. Passing the check does not bind actual input bytes to an artifact hash.

## Questions to take into your own design

- Can every consumed input be tied to an exact content hash at run time?
- Does a static coverage check flag scripts that bypass the registered data API?

## Why this score for a trading system

Its AST check transfers to research-script hygiene, but dynamic I/O and runtime value identity require separate evidence.

**Scope of this review:** We read the pinned README, architecture notes, and lineage checker. We did not run it on a script.
