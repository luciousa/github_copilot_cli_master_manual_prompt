<a id="c4-operation"></a>
# C4. Interactive and automation reference

**Outcomes:** find the correct source for an operation, recognize scope and side effects, and construct an evidence record for future automation. **Prerequisites:** [C1](01-command-literacy.md) and [F3](../fundamentals/03-sessions.md).

This is an orientation, not the exhaustive command catalog. The [GitHub CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) lists command-line operations, interactive slash commands, options, configuration and environment variables. Availability can differ by version, account, platform and policy. An interactive command is entered in the CLI; a CLI subcommand is invoked from the system shell. Settings changes and session-management actions can have side effects.

| Need | Where to investigate | Review before use |
|---|---|---|
| Discover supported operations | Installed version's help and current CLI reference | Version, aliases, mode and lifecycle status |
| Inspect or change settings | CLI configuration documentation and installed help | Scope, effective policy, persistence and secrets |
| Start or resume work | Session and restoration documentation | Workspace trust, pre-existing changes and interrupted actions |
| Run a scripted task | Non-interactive CLI documentation for the installed version | Quoting, exit behavior, tool permissions, credentials and output handling |
| Initialize or plan | [C2](02-initialization.md) and [C3](03-plan-to-acceptance.md) | Potential writes and whether the mode waits for approval |

## Scenario: a CI investigation

A TypeScript service has a failing pipeline. First use an interactive session to review the failure and propose a diagnostic plan. Only after establishing the installed version, permission model and CI secret policy should the team consider a non-interactive workflow. Record command syntax from the target version's help, expected exit behavior and a failure path, then test in an isolated environment before granting CI access.

**Illustrative prompt — not a shell command:**

> Review the provided, redacted CI failure and identify plausible causes and evidence needed to distinguish them. Do not modify workflow files, access secrets or start external jobs.

Expected result: hypotheses with evidence and uncertainty. Reproduce and verify independently; a suggested CI change is not validated until the workflow is reviewed and tested under appropriate controls.

**Troubleshooting:** if documented options are missing locally, record the exact installed version and help output, then check release-specific documentation. If a scripted invocation returns an unexpected status or prompts for access, inspect its mode and permissions. The [versioned help index](../../reference/commands-1.0.109.md), [live slash catalog](../../reference/slash-command-catalog.md) and [verification ledger](../../reference/verification-ledger.md) distinguish documented syntax from the limited invocations actually tested; they do not establish a general exit-code contract.
