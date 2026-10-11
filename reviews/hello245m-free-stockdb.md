# free-stockdb — Does a verified file download also make a database snapshot consistent

**Decision question:** Does a verified file download also make a database snapshot consistent?

| Field | Review |
| --- | --- |
| Upstream | [free-stockdb](https://github.com/hello245m/free-stockdb) |
| Primary area | Market Data & Ingestion |
| Source commit | [74a26af765acef4f1c6b703d12eb25493fa05c0d](https://github.com/hello245m/free-stockdb/commit/74a26af765acef4f1c6b703d12eb25493fa05c0d) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/hello245m/free-stockdb/blob/74a26af765acef4f1c6b703d12eb25493fa05c0d/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Synchronizes local datasets against a size-and-hash manifest. Useful for inspecting file integrity; database consistency still requires a coordinated snapshot switch. |

## Project overview

Local Chinese-equity data engine exposing stored data through SDK, HTTP and MCP interfaces. [Project documentation](https://github.com/hello245m/free-stockdb/blob/74a26af765acef4f1c6b703d12eb25493fa05c0d/README.md#L5-L34).

## Mechanism worth inspecting

The mirror contract includes byte size and SHA-256. The updater skips matching files, downloads replacements to temporary paths, checks both properties and then renames each file. [Protocol](https://github.com/hello245m/free-stockdb/blob/74a26af765acef4f1c6b703d12eb25493fa05c0d/docs/DATA_SOURCE.md#L13-L33), [updater](https://github.com/hello245m/free-stockdb/blob/74a26af765acef4f1c6b703d12eb25493fa05c0d/cpp/src/updater.cpp#L238-L273).

## Important limit

Replacement is per file, not one atomic database generation; the protocol explicitly requires stopping the local service. Hashes establish integrity against a supplied manifest, not the publisher's trustworthiness. [Limit](https://github.com/hello245m/free-stockdb/blob/74a26af765acef4f1c6b703d12eb25493fa05c0d/docs/DATA_SOURCE.md#L27-L39).

## Questions to take into your own design

- Does a verified file download also make a database snapshot consistent?
- Does a dataset update expose one complete generation or a mixture of old and new files?

## Why this score for a trading system

3/5: a transferable dataset-delivery pattern, with equity-specific data and no atomic multi-file publication in the inspected loop.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
