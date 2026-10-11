# Cryptostore — Can collector configuration describe the evidence needed for replay

**Decision question:** Can collector configuration describe the evidence needed for replay?

| Field | Review |
| --- | --- |
| Upstream | [Cryptostore](https://github.com/bmoscon/cryptostore) |
| Primary area | Market Data & Ingestion |
| Source commit | [8a4310d6ca1d52f294e015c802863f1ff9da44e2](https://github.com/bmoscon/cryptostore/commit/8a4310d6ca1d52f294e015c802863f1ff9da44e2) |
| Reviewed | 2026-09-26 |
| Declared license | [XFree86-style acknowledgment license](https://github.com/bmoscon/cryptostore/blob/8a4310d6ca1d52f294e015c802863f1ff9da44e2/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A small reference for explicit collector configuration, including raw capture and snapshot policy. Durable ingestion and replay completeness still need their own contracts. |

## Project overview

Cryptostore configures a Cryptofeed collector through environment variables and sends selected channels to storage backends. [Project documentation](https://github.com/bmoscon/cryptostore/blob/8a4310d6ca1d52f294e015c802863f1ff9da44e2/docs/overview.md#L16-L28).

## Mechanism worth inspecting

The configuration separates snapshot frequency, snapshot-only storage and raw capture. Backend validation rejects unknown destinations; channel callbacks are pruned to the configured subscription. [Configuration](https://github.com/bmoscon/cryptostore/blob/8a4310d6ca1d52f294e015c802863f1ff9da44e2/cryptostore.py#L29-L53), [routing and raw capture](https://github.com/bmoscon/cryptostore/blob/8a4310d6ca1d52f294e015c802863f1ff9da44e2/cryptostore.py#L145-L168).

## Important limit

Raw capture is optional. The inspected wrapper does not provide a durable checkpoint or prove that storage acknowledges every received event.

## Questions to take into your own design

- Can collector configuration describe the evidence needed for replay?
- Which raw-capture and snapshot settings are part of the collector's versioned manifest?

## Why this score for a trading system

2/5: relevant collector boundaries, but most behavior is delegated to Cryptofeed and storage backends; the wrapper adds limited independent verification.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
