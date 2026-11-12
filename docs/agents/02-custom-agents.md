<a id="a2-custom-agents"></a>
# A2. Custom agents and delegation

**Outcomes:** distinguish a custom agent profile, a subagent and cloud delegation; plan safe parallel work; check inheritance and side effects. **Prerequisites:** [A1](01-supervised-autonomy.md) and [X1](../context/01-instructions.md).

GitHub documents custom agent profiles with specialized instructions and tool access, and says the CLI may delegate suitable work to a subagent with a separate context. It documents user, repository, organization and enterprise scopes, subject to access and version. [Invoking custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents). A separate context is a context-management feature; do not assume it is a filesystem, network or credential isolation boundary.

The [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) describes different repository-instruction inheritance for built-in and custom subagents. A custom subagent may need an explicit opt-in for repository instructions; verify the exact current agent and target CLI version. Do not assume all agents inherit the parent session's guidance, tool permissions or model. Agent profile syntax and invocation are **unverified locally—do not execute** until version-specific help and behavior are checked.

## Choose the execution location

| Mechanism | Documented purpose | Review before use |
|---|---|---|
| Local subagent | Focus a task in a separate context within the CLI workflow | Scope, tools, inherited guidance, model, result and conflict risk. |
| Parallel fleet mode | Divide work among parallel subagents where supported | Independent ownership, supported client, concurrency, integration and cost; GitHub documents an ACP limitation. [Programmatic reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-programmatic-reference). |
| Local Autopilot | Continue a task locally across steps | Continuation and tool permissions separately, sandbox and stop conditions. |
| Cloud delegation | Hand work to Copilot cloud agent | Remote access, branch and draft pull-request side effects, data policy and review. |

GitHub's [delegation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca) says cloud delegation can create a branch and draft pull request and may ask to checkpoint local changes. Those are externally visible changes; obtain the required authorization and inspect the current workflow before proceeding. Exact entitlement and behavior remain untested here.

## Scenario: parallel review of an API change

Assign one bounded review of authorization and another of pagination tests only if the CLI version and policy support the intended delegation. Avoid overlapping edits; specify allowed files and expected evidence. The parent must reconcile findings against the same diff and independently verify any claimed defect. Parallel summaries are not proof that checks ran, and multiple agents can repeat the same mistake.

**Illustrative prompt — not a shell command:**

> If supported and permitted, assign independent read-only reviews of authorization and pagination tests. Each review must cite files, distinguish confirmed findings from hypotheses, and avoid edits or external access. Summarize disagreements for human review.

Expected result: traceable, bounded findings. If an agent is unavailable or inheritance is unclear, perform the review without assuming delegation occurred. Check profile provenance and tool grants before enabling any custom agent.
