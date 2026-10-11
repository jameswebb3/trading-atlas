# chain - An archive bundle can fail quorum

**Decision question:** When should a produced archive bundle count as accepted data?

| Field | Review |
| --- | --- |
| Upstream | [KYVENetwork/chain](https://github.com/KYVENetwork/chain) |
| Primary area | Market Data & Ingestion |
| Source commit | [611fe2d48f537f7ecfb3faab34e5f47b3f65fc83](https://github.com/KYVENetwork/chain/commit/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83) |
| Reviewed | 2026-10-10 |
| Declared license | MIT ([source](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/LICENSE)) |
| Review depth | 2/3: README and relevant implementation read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The end-block handler checks vote distribution; no quorum drops the proposed bundle, while a valid tally finalizes it and starts a new upload round. This is a Cosmos consensus workflow, not a market-feed collector; the transferable control is the explicit accepted, dropped and timed-out bundle state. |

## What this project does

KYVE uses a consensus-backed bundle workflow to archive data in named pools. [README](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/README.md).

## Mechanism inspected

The end-block handler checks vote distribution; no quorum drops the proposed bundle, while a valid tally finalizes it and starts a new upload round. [Implementation](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/x/bundles/keeper/logic_end_block_handle_upload_timeout.go#L42-L105).

## Limitation that matters

This is a Cosmos consensus workflow, not a market-feed collector; the transferable control is the explicit accepted, dropped and timed-out bundle state. This conclusion is limited to the inspected paths at the pinned commit.

## Practical check for a trading system

Represent a market-data partition as proposed, validated, accepted or rejected, and prevent rejected partitions from appearing complete to research.

## Why this score

The end-block handler checks vote distribution; no quorum drops the proposed bundle, while a valid tally finalizes it and starts a new upload round. This is a Cosmos consensus workflow, not a market-feed collector; the transferable control is the explicit accepted, dropped and timed-out bundle state.

## Source trail

[README](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/README.md) - [Implementation](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/x/bundles/keeper/logic_end_block_handle_upload_timeout.go#L42-L105) - [License](https://github.com/KYVENetwork/chain/blob/611fe2d48f537f7ecfb3faab34e5f47b3f65fc83/LICENSE).

**Scope:** We read the linked source; we did not install, run, audit or replicate the upstream project.
