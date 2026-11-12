<a id="a1-supervised-autonomy"></a>
# A1. Supervised autonomy

**Outcomes:** separate autonomous continuation from permissions, select checkpoints based on risk, and recognize when a task must pause. **Prerequisites:** [C3](../commands/03-plan-to-acceptance.md), [X3](../context/03-task-contracts.md), and an approved workspace and tool policy.

GitHub describes interactive work and Autopilot as different ways to continue a task. Autopilot controls whether the agent continues through successive steps; broad permission settings control which tools, paths and URLs can be used without further prompts. Suppressing user questions is another separate control. These should not be treated as interchangeable. The CLI's current [Autopilot guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/use-autopilot-mode) describes a manual-approval choice in which requests requiring approval are automatically denied, as well as a full-permissions choice. Other GitHub pages describe this differently; see [V17](../../reference/verification-ledger.md). None of these modes or settings was tested locally.

**All CLI controls mentioned in this chapter are unverified locally—do not execute** until checked against installed help, effective policy and a disposable environment. A continuation limit or credit budget is not a permission boundary; a sandbox is a distinct layer whose enforcement and configuration must be independently checked.

## Match supervision to risk

| Task risk | Example | Review and boundary |
|---|---|---|
| Bounded investigation | Trace a function in a trusted checkout | Restrict access; verify citations and requested tools. |
| Local reversible change | Add a test to a disposable branch | Approve scope, inspect diff and run focused tests. |
| Sensitive or hard to reverse | Migration, credentials, cloud or deployment | Require explicit human decisions, narrow external access, rollback plan and independent review. |

These are editorial risk tiers, not built-in CLI modes. State the goal, allowed paths, denied operations, acceptance tests and stop conditions. Ask for checkpoints at changes in scope, failed tests, unexpected tool requests and insufficient evidence. An agent's claim that it has stopped is not a substitute for verifying actual processes and workspace state.

**Scenario:** a Python service needs a test refactor. Begin with investigation and a reviewed plan. Permit only the agreed local files and test commands under your environment's controls. Stop when a test failure suggests behavior is changing. Inspect the diff and test output before deciding whether to continue.

**Illustrative prompt — not a shell command:**

> Propose a small test refactor with no behavior change. Identify the tests and files involved, risks and a rollback approach. Wait for review before editing; stop if new dependencies, network access or unrelated files are needed.

**Expected result:** a plan or bounded change with evidence, depending on approval. If the agent repeats a failed action, stop it, preserve evidence and diagnose the failure. Do not treat a broad approval as necessary just because a narrower workflow is slower.
