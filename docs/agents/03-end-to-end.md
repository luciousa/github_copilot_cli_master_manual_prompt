<a id="a3-delivery"></a>
# A3. End-to-end delivery

**Outcomes:** guide a multi-service request from requirements to acceptance with evidence at each transition. **Prerequisites:** [C3](../commands/03-plan-to-acceptance.md), [A1](01-supervised-autonomy.md), and your team's release and security policies.

## Scenario: order status across a .NET API and Vue client

| Stage | Human decision and agent task | Evidence and stop condition |
|---|---|---|
| Intake | Define users, authorization, status transitions, non-goals and compatibility. Ask the agent to surface missing details. | Approved acceptance criteria; stop on ambiguous access rules. |
| Discovery | Request existing API, client and test paths; verify the evidence. | Source references and unknowns; stop if required service ownership is unclear. |
| Plan | Review ordered changes, tests, migration or rollout impacts and rollback. | Approved plan and permitted actions; stop before unapproved writes. |
| Implementation | Authorize a bounded increment; review any tool requests and actual changes. | Focused diff and explanation; stop on new dependencies or external changes. |
| Validation | Run agreed tests in an appropriate environment and inspect output. | API, UI and authorization evidence; report failures and tests not run. |
| Review | Check correctness, security, accessibility and compatibility; use a separate review if useful and supported. | Verified findings and dispositions; stop on unresolved material issues. |
| Acceptance | Compare the final diff and behavior with every criterion; follow release policy. | Human acceptance, documented limitations and release decision. |

**Illustrative prompt — not a shell command:**

> Investigate the existing order-status flow across the .NET API and Vue client. Cite relevant files and authorization checks. Propose acceptance criteria and a staged plan including tests and rollback. Do not modify files, use production data, deploy, or create external resources. Wait for review.

Expected result: a reviewable plan with uncertainties. The operator verifies claims and decides whether to authorize each subsequent stage. If the agent or environment fails, preserve the approved contract, actual working-tree state and test output; resume only after reconciling them. See [session recovery](../context/02-context-lifecycle.md). For a documented CLI planning workflow and its approval-mode exception, see [C3](../commands/03-plan-to-acceptance.md).

**Common mistakes:** treating a plan as proof, granting deployment authority during investigation, accepting a passing narrow test as complete coverage, or conflating an agent's summary with a human acceptance decision. Do not share credentials or private data merely to improve the prompt.
