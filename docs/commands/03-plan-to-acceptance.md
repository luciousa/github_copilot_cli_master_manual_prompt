<a id="c3-plan"></a>
# C3. Plan to accepted change

**Outcomes:** turn a feature request into an inspectable plan, set approval boundaries, validate implementation, and handle autonomous exceptions. **Prerequisites:** [C1](01-command-literacy.md), a scoped workspace and permission settings reviewed under [F3](../fundamentals/03-sessions.md).

GitHub documents `/plan [PROMPT]` for creating an implementation plan and describes a normal planning workflow in which the user reviews and approves the plan before implementation. Its [command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) also documents an explicitly configured plan-then-autopilot mode that proceeds without a human approval transition. Do not assume every plan configuration waits for approval. [CLI best practices](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices).

**Runtime verification status:** In one Windows CLI 1.0.109 test, interactive `/plan` in manual-approval mode produced a review dialog and a private plan; the target file was absent afterward. The dialog's exit-without-running option also produced a transient “Plan approved” message, so inspect the actual mode and workspace rather than inferring effects from that message. Other versions, implementation approval and plan-then-autopilot remain untested. [Test evidence](../../research/evidence/copilot-1.0.109-plan-check.md). Check effective permissions and policy; neither a prompt nor a plan is an independent security boundary.

GitHub's current CLI reference describes protections against direct project edits in plan mode, but explicitly says the protections are not airtight: some shell effects and connected external-tool calls can still occur. Treat plan mode as an additional safeguard, not a guarantee of zero side effects. This description has not been tested in the target environment. [CLI reference, security](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Scenario: paginated order history

1. **Define the contract.** State who may see orders, pagination semantics, API compatibility, UI behavior, non-goals and acceptance tests. Avoid production data and credentials.
2. **Request discovery and a plan.** Ask for affected API and React files, contract changes, tests, rollout and rollback, risks, unknowns and checkpoints. Require the assistant to identify evidence and ask about missing requirements.
3. **Review and decide.** Check the plan against actual source and policies. Resolve questions before allowing edits. Reject a plan that assumes authorization rules, runs destructive migrations, or grants itself broader access.
4. **Authorize bounded implementation.** Approve the agreed scope and individually review any requested file, shell, network or external-system action according to its risk. Pause when new facts change the contract.
5. **Test and review.** Inspect the diff, run the agreed relevant tests and assess failure output. Verify that pagination and access-control tests cover the intended cases. Report what was not run and why.
6. **Accept.** Compare the observed result to every criterion, check for unintended files and security-sensitive changes, and obtain human sign-off according to the team's process.

**Illustrative plan prompt — not a shell command:**

> Investigate adding paginated order history to the existing .NET API and React client. Identify the current authorization rules and tests with file evidence. Propose acceptance criteria, implementation steps, compatibility risks, test cases and unresolved questions. Do not implement or run state-changing commands. Wait for my review before any edits.

Expected result: a reviewable plan and open questions. Because plans are generated, their completeness, correctness and approval behavior must be verified; do not treat the output itself as a tested implementation.

## Recovery and anti-patterns

If implementation starts unexpectedly, stop the session's action, inspect changes and permissions, and preserve unrelated work before deciding how to recover. If tests fail, capture failure details, distinguish pre-existing from introduced problems, and revise the plan rather than repeatedly retrying without diagnosis. If requirements change, obtain a new decision on scope before proceeding. A plan that omits test and rollback considerations is not ready for approval merely because it is detailed.
