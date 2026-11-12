<a id="e2-lifecycle"></a>
# E2. Extension lifecycle and trust

**Outcomes:** evaluate provenance, test scope, manage updates and remove an integration without assuming cleanup is complete. **Prerequisites:** [E1](01-mechanisms.md), organizational approval and an isolated test environment.

## Lifecycle

1. **Discover:** identify the precise publisher, repository, version or immutable revision, license, intended function and support status. Determine whether the component is native, first-party, third-party or preview from authoritative evidence.
2. **Review:** inspect manifests, instructions, scripts, hooks, server commands, network endpoints and requested credentials. Confirm the source and update policy; treat instructions and tool results as untrusted data.
3. **Authorize and install:** use version-specific official instructions only after confirming scope and policy. Test in an isolated environment with least privilege and disposable credentials. Installation can execute code or grant access.
4. **Verify:** check what was installed, enabled and loaded; exercise a narrowly scoped task and observe file, network and permission requests. Record version, source, configuration scope and results.
5. **Maintain:** review changes and update cadence, including automatic updates; re-evaluate when permissions or dependencies change. GitHub's [plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) documents session-start automatic updates for certain first-party plugins, subject to its stated conditions.
6. **Remove:** use the applicable component's documented removal mechanism, then verify residual settings, caches, hooks, credentials and server access. Revoke credentials separately when appropriate; removing a listing is not proof that access has been revoked.

Exact commands and component-specific cleanup depend on the installed version. Minimal local plugin and skill fixtures were added and removed in a disposable Windows CLI 1.0.109 profile; real integrations, marketplace workflows and MCP lifecycle remain untested. **Unverified—do not execute** a procedure for an actual component until its source, scope and behavior are checked. The [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference), [skills guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) and [MCP guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) are separate sources; a skill, server and plugin are not interchangeable installation targets. See [fixture evidence](../../reference/verification-ledger.md) V27–V28.

## Scenario: a CI integration

Before connecting an external CI service, identify its owner, required endpoints, permissions and data retention. Prefer a limited test account and read-only capabilities if those meet the task. Confirm that disabling or removing the integration also leads to credential revocation through the service's own controls.

**Illustrative prompt — not a shell command:**

> Review this extension's manifest and documentation for executable components, requested access, update behavior and unresolved provenance. Do not install it, contact its endpoints or reveal credentials.

Expected result: a review checklist with source evidence. If the publisher or source is uncertain, do not install it. If unexpected execution occurs, stop the session, isolate the integration and follow the organization's incident process.

**Known conflict:** GitHub's plugin reference and a separate installation page disagree about default registered marketplaces; the current draft does not assume a default list. See [V18](../../reference/verification-ledger.md).
