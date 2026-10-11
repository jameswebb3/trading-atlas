# fuzz-rest-api — Fuzzed requests expose a demonstration endpoint's assumptions

**Decision question:** Can generated malformed payloads exercise an API boundary?

| Field | Review |
| --- | --- |
| Upstream | [dubzzz/fuzz-rest-api](https://github.com/dubzzz/fuzz-rest-api) |
| Primary area | Testing & Verification |
| Source commit | [6e5b3dfa015bf0adb3b325f44d335999f339fcb0](https://github.com/dubzzz/fuzz-rest-api/commit/6e5b3dfa015bf0adb3b325f44d335999f339fcb0) |
| Reviewed | 2026-10-09 |
| Declared license | MIT ([source](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/LICENSE)) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Transferable |
| Verdict | The test generates login objects with deleted keys, Unicode profile IDs and inferred comment payloads, then asserts the HTTP call does not fail. The oracle only treats HTTP failure as a defect; a successful response with a wrong state transition would pass. |

## What this project does

Small demonstration of property-based REST API fuzzing with fast-check. [README](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/README.md).

## Mechanism inspected

The test generates login objects with deleted keys, Unicode profile IDs and inferred comment payloads, then asserts the HTTP call does not fail. [Implementation](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/test/fuzz.js#L1-L43).

## Limitation that matters

The oracle only treats HTTP failure as a defect; a successful response with a wrong state transition would pass. This conclusion applies to the inspected path at the pinned commit.

## Practical check for a trading system

Fuzz order API payloads only with stateful oracles for accepted, rejected and uncertain outcomes; never use this demo as a live client.

## Why this score

The test generates login objects with deleted keys, Unicode profile IDs and inferred comment payloads, then asserts the HTTP call does not fail. The oracle only treats HTTP failure as a defect; a successful response with a wrong state transition would pass.

## Source trail

[README](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/README.md) · [Implementation](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/test/fuzz.js#L1-L43) · [License](https://github.com/dubzzz/fuzz-rest-api/blob/6e5b3dfa015bf0adb3b325f44d335999f339fcb0/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
