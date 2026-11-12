<a id="x3-contracts"></a>
# X3. Task contracts and prompting

**Outcomes:** turn a request into a bounded, testable contract and detect drift during implementation. **Prerequisites:** [C3](../commands/03-plan-to-acceptance.md), [X1](01-instructions.md) and knowledge of the repository's actual conventions.

## Contract template

The following is an **illustrative prompt template, not executable code**. Replace bracketed text with confirmed information; do not include secrets.

> **Goal:** [observable user or system outcome].
>
> **Context:** [relevant services, files, evidence and current behavior].
>
> **Scope:** [permitted changes and explicit exclusions].
>
> **Constraints:** [compatibility, performance, security and operational requirements].
>
> **Acceptance:** [observable cases and tests, including failure and authorization cases].
>
> **Workflow:** Investigate first; cite evidence and identify unknowns. Propose a plan and wait for review before edits. Ask before operations outside the agreed scope, external access, destructive commands or deployment. Report tests run, results and omissions.

This structure is editorial guidance. It does not enforce permissions: use the CLI's actual permission controls and organizational safeguards, and review requested actions. A vague instruction to “make it secure” is not a testable acceptance criterion.

## Scenario: SQL-backed account search

Specify tenant isolation, allowed query fields, pagination, expected API response, representative unauthorized cases and a dataset safe for testing. Ask the assistant to identify existing query and authorization patterns, then review the proposed plan. During implementation, compare each diff and test to the contract. If the assistant proposes a schema migration, external service, or access to production data that was not in scope, stop and decide whether to revise the contract.

**Expected result:** a plan with traceable criteria, an implementation whose actual diff stays within scope, and test evidence for each material requirement. If a requirement cannot be tested, record the gap and decide whether acceptance is possible. Request file-level evidence for claims; independently inspect security-sensitive behavior. Refer to [GitHub's CLI best practices](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices) for documented planning and repository-context practices.

## Anti-drift checks

- Keep durable requirements and approval decisions outside transient summaries when the work spans sessions.
- Require a new decision when the plan changes, tests fail in an unexplained way, or proposed actions exceed authority.
- Separate observed evidence, assumptions and recommendations in status reports. A completed tool call does not establish that its output is correct.
- Avoid demanding unrestricted tool access to compensate for an unclear task. Reduce scope and request the minimum evidence instead.
