# Langfuse: validate the evaluation case before the score

**Decision question:** Can an evaluation dataset reject malformed inputs and expected outputs before a run is scored?

| Field | Review |
| --- | --- |
| Upstream | [langfuse/langfuse](https://github.com/langfuse/langfuse) |
| Primary area | Agents & Decision Systems |
| Source commit | [fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1](https://github.com/langfuse/langfuse/commit/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1) |
| Reviewed | 2026-09-25 |
| Declared license | [MIT core; separate EE terms](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/LICENSE) |
| Review depth | 2/3: documentation and implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Adjacent |
| Verdict | Normalizes dataset items and validates both input and expected output against schemas before storing them. Normalization can turn an empty string into null and remove control characters; preserve original evidence when exact input bytes matter. |

## Mechanism worth inspecting

The [README](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/README.md#L74-L88) describes datasets and evaluations as part of an LLM workflow. The [dataset item validator](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/packages/shared/src/server/services/DatasetService/DatasetItemValidator.ts#L29-L64) compiles input and expected-output schemas once for a batch. It [normalizes JSON](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/packages/shared/src/server/services/DatasetService/DatasetItemValidator.ts#L114-L151) and [returns distinct validation errors](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/packages/shared/src/server/services/DatasetService/DatasetItemValidator.ts#L197-L270) for the two sides before persistence.

## Important limit

The same normalizer treats an empty string as null and can strip control characters. That may be appropriate for storage, but a scientific evaluation may need both original and normalized forms to audit why a case passed or failed. Valid schema does not establish that the expected answer is correct. The [repository license](https://github.com/langfuse/langfuse/blob/fd5c9ee18e0759b6aea6247351e84d7ee02ed1b1/LICENSE#L1-L8) also excludes enterprise directories from its MIT core terms.

## Questions to take into your own design

- Is the case schema version attached to each run?
- Does an invalid expected output stop scoring distinctly from a failed agent answer?
- Is the raw input retained when normalization changes it?

## Why this score for a trading system

Dataset-item schema checks can organize agent evaluations, but normalization changes evidence and no trading outcome is tested.

**Scope of this review:** We read the pinned README, license, and dataset item validator. We did not deploy Langfuse, inspect every dataset write path, or run evaluations.
