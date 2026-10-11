# A printed validation failure may still leave a successful process

**Decision question:** Will a data-quality failure actually stop the research pipeline?

| Field | Review |
| --- | --- |
| Upstream | [Target Data Validator](https://github.com/target/data-validator) |
| Primary area | Data Quality & Lineage |
| Source commit | [8d1326c4118488bfb61b74d9b57535c6581e1e93](https://github.com/target/data-validator/commit/8d1326c4118488bfb61b74d9b57535c6581e1e93) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/target/data-validator/blob/8d1326c4118488bfb61b74d9b57535c6581e1e93/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The validator separates fatal execution errors from failed data checks. A failed check prints FAIL, but exits with an error only when exitErrorOnFail is enabled. That makes the caller's gate configuration as important as the validation report. |

## Mechanism worth inspecting

The [README usage](https://github.com/target/data-validator/blob/8d1326c4118488bfb61b74d9b57535c6581e1e93/README.md#L55-L65) exposes the exitErrorOnFail option. The [execution contract](https://github.com/target/data-validator/blob/8d1326c4118488bfb61b74d9b57535c6581e1e93/src/main/scala/com/target/data_validator/Main.scala#L78-L104) separates fatal and validation status. The [CLI branch](https://github.com/target/data-validator/blob/8d1326c4118488bfb61b74d9b57535c6581e1e93/src/main/scala/com/target/data_validator/Main.scala#L134-L152) prints FAIL for either but only makes validation failure fatal when the option is enabled.

## Important limit

A correct validation result can be operationally ignored if the caller only checks process exit. The README's stated default is not a durable guarantee across versions; check the pinned CLI configuration and wrapper.

## Questions to take into your own design

- Which exact signal prevents an invalid dataset from reaching an experiment?
- Are gate behavior and process exit tested for validation failure, not just exceptions?

## Why this score for a trading system

3/5: Separating execution failure from data failure is useful, but the pipeline must bind the latter to an explicit stop condition.

**Scope of this review:** We read the pinned overview, linked documentation, and the cited implementation. No upstream code was executed.
