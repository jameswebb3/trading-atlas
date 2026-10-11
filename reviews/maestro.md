# Netflix Maestro: separate retry budgets by failure class

**Decision question:** Should an infrastructure failure consume the same retry budget as invalid research input?

| Field | Review |
| --- | --- |
| Upstream | [Netflix Maestro](https://github.com/Netflix/maestro) |
| Primary area | Operations & Observability |
| Source commit | [1aec679bd72be7d150507cf9a881994ca58b808c](https://github.com/Netflix/maestro/commit/1aec679bd72be7d150507cf9a881994ca58b808c) |
| Reviewed | 2026-09-26 |
| Declared license | [Apache-2.0](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | Separates user, platform, and timeout retry policies and maps exhausted error budgets to fatal failure. Useful for research pipelines with expensive or unsafe retries; failure classification does not prove that repeating a side effect is safe. |

## Project overview

Workflow orchestrator from Netflix for data and ML pipelines. Provides step dependencies, execution history, and separate retry policies for user, platform, and timeout failures.

[Project documentation](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/README.md#L3-L17).

## Mechanism worth inspecting

The [overview](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/README.md#L3-L17) describes workflow orchestration. The [official retry-policy explanation](https://netflixtechblog.com/maestro-netflixs-workflow-orchestrator-ee13a06f9c78) distinguishes retry classes and discusses disabling retries for non-idempotent steps. The pinned [policy model](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/maestro-common/src/main/java/com/netflix/maestro/models/definition/RetryPolicy.java#L30-L51) includes separate user, platform, and timeout limits. The [runtime manager](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/maestro-engine/src/main/java/com/netflix/maestro/engine/execution/StepRuntimeManager.java#L81-L94) changes exhausted user/platform failures to FATALLY_FAILED, and its [start-state handling](https://github.com/Netflix/maestro/blob/1aec679bd72be7d150507cf9a881994ca58b808c/maestro-engine/src/main/java/com/netflix/maestro/engine/execution/StepRuntimeManager.java#L111-L133) keeps error classes distinct.

## Important limit

Classification and budgets are workflow controls. They do not establish whether an order request, artifact publication, or dataset write already succeeded before the failure became visible. The cited manager does not provide a trading reconciliation mechanism. External documentation describes the design; the source links establish the pinned implementation examined here.

## Questions to take into your own design

- Can a failed step distinguish invalid input, transient infrastructure failure, timeout, and unknown side-effect outcome?
- Which steps require reconciliation or an idempotency key before any retry is permitted?

## Why this score for a trading system

3/5: a transferable pattern for research and data orchestration, grounded in policy and runtime code. Its large workflow platform is not necessary to implement the narrower retry taxonomy.

**Scope of this review:** We read the pinned overview, relevant documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
