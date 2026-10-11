# hypothesis-jsonschema: generated valid inputs need an independent oracle

**Decision question:** How can generated payload tests prove a schema's accepted shape without trusting one example?

| Field | Review |
| --- | --- |
| Upstream | [python-jsonschema/hypothesis-jsonschema](https://github.com/python-jsonschema/hypothesis-jsonschema) |
| Primary area | Testing & Verification |
| Source commit | [fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc](https://github.com/python-jsonschema/hypothesis-jsonschema/commit/fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc) |
| Reviewed | 2026-09-25 |
| Declared license | [MPL-2.0](https://github.com/python-jsonschema/hypothesis-jsonschema/blob/fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc/LICENSE) |
| Review depth | 3/3: documentation, implementation, and test code read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Generates JSON values from a schema and checks sampled outputs against a separate schema validator in its tests. The generator targets valid values; rejection paths still need invalid mutations, and recursive references are outside the stated support. |

## Mechanism worth inspecting

The [README API](https://github.com/python-jsonschema/hypothesis-jsonschema/blob/fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc/README.md#L1-L22) returns a strategy for objects allowed by a JSON Schema. The [implementation entry point](https://github.com/python-jsonschema/hypothesis-jsonschema/blob/fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc/src/hypothesis_jsonschema/_from_schema.py#L118-L150) builds that strategy and states its draft and recursive-reference boundary. Its [property test](https://github.com/python-jsonschema/hypothesis-jsonschema/blob/fa38b03d8bb6f917ba749ef84ce1e4465d1e27cc/tests/test_from_schema.py#L39-L55) draws both a schema and a value, then asks an independent validator whether the value conforms. This avoids merely comparing a generator with itself.

## Important limit

Passing valid generated inputs says little about rejection of malformed fields, missing IDs, or incompatible order types. A separate one-field mutation set is needed for those paths. The README also notes that custom string formats are ignored unless strategies are provided.

## Questions to take into your own design

- Does the oracle differ from the generator's own acceptance logic?
- Which malformed variants must fail before a side effect?
- Are seed and smallest counterexample retained when a property fails?

## Why this score for a trading system

Schema-derived payloads can probe trading data contracts, but valid-value generation leaves rejection and event-order paths untested.

**Scope of this review:** We read the pinned README, generator entry point, and test property. We did not install the package, run tests, or assess every JSON Schema draft feature.
