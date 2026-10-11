# digital-oracle - Replay an external request only when its snapshot exists

**Decision question:** Can a research run replay exactly the external response it previously observed?

| Field | Review |
| --- | --- |
| Upstream | [komako-workshop/digital-oracle](https://github.com/komako-workshop/digital-oracle) |
| Primary area | Market Data & Ingestion |
| Source commit | [a63e4c19a2f3313d54914c44666febaf5ffb9d6f](https://github.com/komako-workshop/digital-oracle/commit/a63e4c19a2f3313d54914c44666febaf5ffb9d6f) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/LICENSE)) |
| Review depth | 2/3: README, documentation where present and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Executive assessment | The recorder keys a snapshot by response kind, URL and normalized parameters, stores the response with captured_at, and the replay client raises SnapshotMissError when the matching request is absent. A second call with the same key overwrites the file. captured_at is a capture timestamp, not proof of when the provider published the underlying observation. |

## What this project does

Digital Oracle queries financial and macro providers and includes an HTTP capture/replay layer. [README](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/README.en.md).

## Mechanism inspected

The recorder keys a snapshot by response kind, URL and normalized parameters, stores the response with captured_at, and the replay client raises SnapshotMissError when the matching request is absent. [Implementation](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/digital_oracle/snapshots.py#L40-L53). [Related path](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/digital_oracle/snapshots.py#L92-L140).

## Limitation that matters

A second call with the same key overwrites the file. captured_at is a capture timestamp, not proof of when the provider published the underlying observation. The conclusion is limited to these inspected paths at the pinned commit.

## Practical check for a trading system

Keep an immutable capture ID and source publication time beside the response; make a missing request a hard replay failure.

## Why this score

The capture/replay boundary is a direct research control, but the timestamp and overwrite semantics are insufficient for point-in-time market evidence.

## Source trail

[README](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/README.en.md) - [Implementation](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/digital_oracle/snapshots.py#L40-L53) - [Related path](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/digital_oracle/snapshots.py#L92-L140) - [License](https://github.com/komako-workshop/digital-oracle/blob/a63e4c19a2f3313d54914c44666febaf5ffb9d6f/LICENSE).

**Scope:** Source reading only; no upstream installation, execution, security audit or claim of trading profitability.
