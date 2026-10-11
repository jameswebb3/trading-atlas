# python-bitcoinlib — parse the complete payload

**Decision question:** Does successful decoding account for every byte in the supplied record?

| Field | Review |
| --- | --- |
| Upstream | [python-bitcoinlib](https://github.com/petertodd/python-bitcoinlib) |
| Primary area | Market Data & Ingestion |
| Source commit | [91e334d831fd16c60c932ad7df42c88fd6567c02](https://github.com/petertodd/python-bitcoinlib/commit/91e334d831fd16c60c932ad7df42c88fd6567c02) |
| Reviewed | 2026-09-27 |
| Declared license | [LGPL-3.0-or-later](https://github.com/petertodd/python-bitcoinlib/blob/91e334d831fd16c60c932ad7df42c88fd6567c02/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | A precise raw-ingestion reference: default object decoding rejects unconsumed trailing bytes. That checks framing, while transaction validity and canonical inclusion remain separate responsibilities. |

## Project overview

python-bitcoinlib exposes low-level Bitcoin protocol data structures and serialization tools. [Project documentation](https://github.com/petertodd/python-bitcoinlib/blob/91e334d831fd16c60c932ad7df42c88fd6567c02/README.md#L3-L5).

## Mechanism worth inspecting

The object deserializer parses a byte buffer and, by default, reads the remainder and raises if any bytes are left. `allow_padding=True` explicitly relaxes that check. [Deserializer contract](https://github.com/petertodd/python-bitcoinlib/blob/91e334d831fd16c60c932ad7df42c88fd6567c02/bitcoin/core/serialize.py#L93-L108).

## Important limit

Full buffer consumption catches framing or trailing-data problems, but it does not validate consensus, signatures or canonical-chain membership. Calling stream-level decoding directly also gives the caller responsibility for framing. The root declares LGPL-3.0-or-later, which matters for code reuse.

## Questions to take into your own design

- Are raw records length-framed and rejected when unexpected bytes remain?
- Is parser validity stored separately from transaction validity and inclusion evidence?

## Why this score for a trading system

3/5: a concrete ingestion framing contract, useful independently of adopting the library or copying its licensed implementation.

**Scope of this review:** Object-buffer deserialization and trailing-data rejection; script execution and consensus were not reviewed.
