# QuickNode Hyperliquid SDK — Which party determines the action being signed

**Decision question:** Which party determines the action being signed?

| Field | Review |
| --- | --- |
| Upstream | [QuickNode Hyperliquid SDK](https://github.com/quiknode-labs/hyperliquid-sdk) |
| Primary area | Execution & Exchange Integration |
| Source commit | [f6713ffeec6ac159a2006cef88a7b2be43694ee7](https://github.com/quiknode-labs/hyperliquid-sdk/commit/f6713ffeec6ac159a2006cef88a7b2be43694ee7) |
| Reviewed | 2026-09-26 |
| Declared license | [MIT](https://github.com/quiknode-labs/hyperliquid-sdk/blob/f6713ffeec6ac159a2006cef88a7b2be43694ee7/LICENSE) |
| Review depth | 2/3: documentation and relevant implementation read; no runtime test |
| Trading-system value | 2/5 |
| Trading-system fit | Direct |
| Verdict | A convenient community trading interface whose build-sign-send path relies on a remote builder. Inspect and verify the returned action, nonce and hash relationship before treating local signing as complete control over an order. |

## Project overview

This community SDK offers order builders and data access. Its Python documentation distinguishes public read-only access from a QuickNode trading endpoint. [Project documentation](https://github.com/quiknode-labs/hyperliquid-sdk/blob/f6713ffeec6ac159a2006cef88a7b2be43694ee7/python/README.md#L1-L41).

## Mechanism worth inspecting

The trading path sends an action to a build endpoint, signs the returned hash locally, then sends the returned action and nonce with that signature. [Build-sign-send](https://github.com/quiknode-labs/hyperliquid-sdk/blob/f6713ffeec6ac159a2006cef88a7b2be43694ee7/python/hyperliquid_sdk/client.py#L2588-L2624).

## Important limit

The inspected function checks for a returned hash but does not independently recompute it from a locally validated final action. Local key custody alone does not establish control over every signed parameter.

## Questions to take into your own design

- Which party determines the action being signed?
- Can the final action, nonce and hash be recomputed independently before signing?

## Why this score for a trading system

2/5: the trust boundary is concrete and educational, but remote order construction reduces its value for an independently controlled execution stack.

**Scope of this review:** Focused reading of the linked documentation and implementation. Other subsystems and runtime behavior were not assessed.
