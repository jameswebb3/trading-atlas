# eth-abi — decoded values need structural and chain evidence

**Decision question:** What does strict ABI decoding establish about an on-chain observation?

| Field | Review |
| --- | --- |
| Upstream | [eth-abi](https://github.com/ethereum/eth-abi) |
| Primary area | Market Data & Ingestion |
| Source commit | [c0d2d0fb757b06f6f1994e2848db0d84932cb2fe](https://github.com/ethereum/eth-abi/commit/c0d2d0fb757b06f6f1994e2848db0d84932cb2fe) |
| Reviewed | 2026-09-27 |
| Declared license | [MIT](https://github.com/ethereum/eth-abi/blob/c0d2d0fb757b06f6f1994e2848db0d84932cb2fe/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Direct |
| Verdict | Exposes concrete checks for offsets, lengths and padding. A useful ingestion reference, provided structurally decoded values retain contract, ABI and canonical-block evidence and malformed inputs remain explicit failures. |

## Project overview

eth-abi encodes and decodes Ethereum ABI values with checks for dynamic offsets and padding. [Project documentation](https://github.com/ethereum/eth-abi/blob/c0d2d0fb757b06f6f1994e2848db0d84932cb2fe/README.md#L9-L11).

## Mechanism worth inspecting

Tuple decoding validates that dynamic pointers reference legal positions outside the head and within the payload. Strict byte-string decoding checks padded length and zero padding before returning bytes. [Pointer checks](https://github.com/ethereum/eth-abi/blob/c0d2d0fb757b06f6f1994e2848db0d84932cb2fe/eth_abi/decoding.py#L191-L228); [strict bytes](https://github.com/ethereum/eth-abi/blob/c0d2d0fb757b06f6f1994e2848db0d84932cb2fe/eth_abi/decoding.py#L588-L613).

## Important limit

Correct encoding is not proof that the log came from the intended contract, ABI version, network or canonical block. A non-strict decoding policy also changes accepted payloads. Preserve undecoded input and explicit rejection reasons instead of converting malformed observations into numeric defaults.

## Questions to take into your own design

- Does every decoded metric carry contract, ABI version, chain and block-hash provenance?
- Can malformed pointers and nonzero padding fail the collector visibly without yielding a zero metric?

## Why this score for a trading system

3/5: an inspectable binary-data validation layer, with source identity and canonicality required separately for trading use.

**Scope of this review:** Tuple pointers and strict byte-string decoding; no complete ABI compatibility or security audit.
