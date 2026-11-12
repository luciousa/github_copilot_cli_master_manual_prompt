<a id="f3-sessions"></a>
# F3. Sessions and configuration

**Outcomes:** select an appropriate workspace and session scope, review effective permissions, and preserve enough evidence to resume work. **Prerequisites:** [F2 setup](02-setup.md) and a trusted, appropriately bounded repository.

The [CLI overview](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview) describes launching an interactive session from a folder containing code and asking whether the folder is trusted. GitHub warns that the CLI may attempt to read, modify and execute files in and below that folder. Trust a directory only after considering its contents and the access appropriate for the task. A trusted directory is not a blanket approval for every tool request.

The [command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) documents interactive and non-interactive entry points, settings and session restoration. It describes user-level settings and repository/local overrides for supported settings. Configuration precedence, available settings, storage paths, and restoration details must be checked against the installed version and policy; do not assume all options are valid at every scope.

## A repeatable session procedure

1. Identify the repository, working directory, current branch and pre-existing changes. Record the task contract and permitted write scope.
2. Review effective tool permissions, accessible paths, network access and any organizational controls using the installed CLI's current help. Start with the least authority that permits the investigation.
3. Request an investigation, then a plan. Review tool requests and proposed changes before allowing actions with side effects.
4. At checkpoints, record the approved objective, decisions, changed files, tests and results, unresolved questions, and next action in an appropriate project record. Do not include secrets.
5. On resumption, inspect the actual repository and test status before relying on a prior summary. If the CLI offers session restoration, verify its current version's behavior and avoid assuming interrupted work completed.

**Scenario:** a service upgrade spans multiple sessions. Save the approved migration scope and test outcomes in the team's existing tracking system, then compare the working tree and the latest test results when returning. Ask the assistant to identify discrepancies before continuing.

**Illustrative prompt — not a shell command:**

> Based on the visible repository state and the checkpoint I provide, list completed work, unverified claims, changed files and the next smallest safe step. Do not edit files or run state-changing commands.

Expected result: a proposed reconciliation. Confirm the repository state and tests independently; session history is not a substitute for source control or a durable evidence record.

## Troubleshooting and common mistakes

If restored context disagrees with the working tree, treat the tree and independently checked test output as evidence and investigate the difference. If a setting appears ignored, check its supported scope and managed policy before changing it. Avoid enabling broad permissions merely to reduce prompts. Review logs before sharing them because paths, prompts or other sensitive details may be present. CLI 1.0.109 subsequently reported version and help locally; restoration and configuration behavior remain untested.
