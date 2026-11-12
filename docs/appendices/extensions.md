<a id="r4-extensions"></a>
# R4. Extension and integration reference

**Evidence as of 2026-11-11.** Minimal disposable local plugin and skill add/remove tests have run on Windows CLI 1.0.109; no recommended third-party integration, remote marketplace or real MCP server has been installed or invoked. Consult [E1–E3](../extensions/01-mechanisms.md) and the [verification ledger](../../reference/verification-ledger.md) before adopting an integration.

| Mechanism / candidate | Provenance and evidence | Install and removal status | Review before adoption |
|---|---|---|
| Repository instruction | Project-authored; [CLI instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) | Synthetic file discovery and initialization observed; removal untested | Review scope, conflicting rules and change ownership. |
| Project skill | Project- or third-party-authored; [CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | Local fixture added and removed on Windows 1.0.109 | Inspect scripts and resources, source revision, shell and permissions. |
| Custom agent | Project or organization profile; [agent guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents) | Definition and removal untested | Verify profile scope, tools and instruction inheritance. |
| Built-in GitHub MCP | GitHub describes a built-in server in its [CLI MCP guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers) | Enablement, configuration and disabling untested | Verify account, toolset, data flow and credentials. |
| External MCP server | Publisher and source depend on candidate | No third-party candidate reviewed | Inspect code, endpoint, credential scope, isolation and revocation. |
| Plugin and marketplace | [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) | Local fixture added and removed; marketplace and updates untested; default marketplace conflict V18 | Review package contents, publisher, version and automatic updates. |
| Connector | GitHub [support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) describes preview support | Plan and connection lifecycle untested | Verify preview terms, account authorization and revocation. |

For each eventual recommendation, record exact immutable source/version, publisher, license, CLI and OS compatibility, plan/policy requirements, install, verification, usage, upgrade, uninstall, residual credential revocation and test evidence. If any executable step is not verified, label it **Unverified—do not execute** and omit it from copy-ready instructions. A marketplace listing is not a security endorsement.

Version-specific local evidence: CLI 1.0.109 help lists [plugin](../../research/evidence/copilot-1.0.109-plugin-help.txt), [MCP](../../research/evidence/copilot-1.0.109-mcp-help.txt) and [skill](../../research/evidence/copilot-1.0.109-skill-help.txt) management subcommands. Help output does not prove installation, removal, configuration state or successful execution. The plugin help reports one included default marketplace, but the actual registered catalog was not inspected; see V18.

### Version 1.0.109 lifecycle evidence

The following help links identify version-specific management commands. Component-specific behavior depends on its source and configuration; review the intended component in an isolated environment. Angle-bracket labels denote required input, not literal shell commands.

| Resource | Version-specific help | Limits to verify |
|---|---|---|
| Plugin | [Install help](../../research/evidence/copilot-1.0.109-plugin-install-help.txt); [uninstall help](../../research/evidence/copilot-1.0.109-plugin-uninstall-help.txt) | Exact source, optional verification/digest flow, policy and residual data. |
| MCP server | [Add help](../../research/evidence/copilot-1.0.109-mcp-add-help.txt); [remove help](../../research/evidence/copilot-1.0.109-mcp-remove-help.txt) | Help says removal targets user configuration; workspace and plugin sources require separate handling. Verify credential revocation independently. |
| Skill | [Add help](../../research/evidence/copilot-1.0.109-skill-add-help.txt); [remove help](../../research/evidence/copilot-1.0.109-skill-remove-help.txt) | Help distinguishes named skills, custom directories and plugin/built-in skills; verify the actual source and ownership before removal. |

No named third-party integration has passed provenance and lifecycle review. In an isolated Windows 1.0.109 profile a minimal local skill and plugin were added, listed, removed and absent afterward; see [skill test](../../research/evidence/copilot-1.0.109-disposable-checks.txt) and [plugin test](../../research/evidence/copilot-1.0.109-plugin-fixture.txt). The plugin installation printed a warning that direct repository, URL and local-path installs are deprecated. The MCP fixture add failed with a storage I/O error, so MCP lifecycle remains unverified. Results do not establish behavior for real components, other platforms or marketplace installs.
