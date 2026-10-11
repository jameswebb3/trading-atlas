# An artifact digest is only as strong as its weakest reference

**Decision question:** Can an artifact manifest change when a referenced resource changes at the same URI?

| Field | Review |
| --- | --- |
| Upstream | [Weights & Biases SDK](https://github.com/wandb/wandb) |
| Primary area | Research & Reproducibility |
| Source commit | [98f93d636e523bf6e195a2a154f23ba8775623a9](https://github.com/wandb/wandb/commit/98f93d636e523bf6e195a2a154f23ba8775623a9) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/wandb/wandb/blob/98f93d636e523bf6e195a2a154f23ba8775623a9/LICENSE) |
| Review depth | 2/3: documentation and relevant source read; no runtime test |
| Trading-system value | 3/5 |
| Trading-system fit | Transferable |
| Verdict | The artifact manifest hashes sorted paths and entry digests. For unsupported URI schemes, the tracking handler stores the URI itself as the digest and cannot download the resource. That pattern needs explicit evidence labels: a manifest hash does not always imply every referenced object's bytes were checked. |

## Mechanism worth inspecting

The [README](https://github.com/wandb/wandb/blob/98f93d636e523bf6e195a2a154f23ba8775623a9/README.md#L29-L48) presents experiment tracking. The [reference API documentation](https://github.com/wandb/wandb/blob/98f93d636e523bf6e195a2a154f23ba8775623a9/wandb/sdk/artifacts/artifact.py#L1658-L1702) explains external references and checksum options. The [manifest digest](https://github.com/wandb/wandb/blob/98f93d636e523bf6e195a2a154f23ba8775623a9/wandb/sdk/artifacts/artifact_manifests/artifact_manifest_v1.py#L74-L86) combines entry digests, while the [unsupported-scheme handler](https://github.com/wandb/wandb/blob/98f93d636e523bf6e195a2a154f23ba8775623a9/wandb/sdk/artifacts/storage_handlers/tracking_handler.py#L36-L70) records a URI and refuses local download.

## Important limit

The SDK's MIT license is not a license or availability guarantee for the hosted service. This review extracts the manifest contract as an engineering reference; it does not recommend adopting a SaaS backend or equate a URI-only entry with archived evidence.

## Questions to take into your own design

- Which entries can be verified against immutable bytes?
- Does an experiment's provenance report expose URI-only references?

## Why this score for a trading system

3/5: Entry-level provenance strength is a strong research-manifest pattern, but the SDK and service context are not a self-hosted trading solution.

**Scope of this review:** We read the pinned overview, linked documentation, and cited implementation; focused test code is identified where inspected. No upstream code was executed.
