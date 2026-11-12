<a id="m2-decisions"></a>
# M2. Task-based model decisions

**Outcomes:** select candidates using task risk and measurable acceptance criteria, and distinguish editorial judgment from verified capability. **Prerequisites:** [M1](01-selection.md) and a known set of models actually available to your account.

## Decision matrix

The following is **editorial guidance dated 2026-11-11**, not a benchmark or a ranking of named models. GitHub notes that models differ in speed, reasoning and context characteristics, and availability depends on plan and policy; assess candidate-specific documentation and test on your own work. [Model selection guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model).

| Task | Candidate selection principle | Evidence required to accept or escalate |
|---|---|---|
| Repository research | Candidate that can work within the available context and tools | Cited paths, accurate findings, stated gaps; escalate unresolved ambiguity |
| Planning and architecture | Candidate evaluated on decomposition and constraints | Reviewable alternatives, risks and acceptance criteria; expert approval |
| Focused implementation | Candidate evaluated on similar code changes | Correct diff, tests, style and contained side effects |
| Debugging | Candidate evaluated on causal hypotheses | Reproduction, disconfirming checks, root-cause evidence and regression test |
| Refactoring / migration | Candidate evaluated on behavior preservation | Characterization tests, staged diff, rollback plan and compatibility checks |
| Security review | Candidate used as an additional reviewer | Human threat assessment, evidence, independent tools and remediation verification |
| Testing and documentation | Candidate evaluated on coverage and factuality | Useful failure-detecting tests; citations and actual behavior for documentation |

Start with an approved candidate that meets context, data-handling and cost constraints. If quality is insufficient, narrow the task, provide missing evidence, or try another permitted candidate. Record the reason and repeat the same acceptance checks. A more expensive, larger or slower model is not automatically better for a particular task. Do not rely on a second model as independent evidence when both might use the same flawed source or assumptions.

## Scenario: modernization review

Ask one approved candidate to inventory behavior in a legacy Node service; independently check its cited files. Ask a second candidate, if policy and budget permit, to challenge the migration plan against a fixed checklist. Compare substantive findings and test outcomes, not confidence or response length. Resolve disagreements against source code, tests and expert review.

**Illustrative prompt — not a shell command:**

> Assess this migration plan against the supplied acceptance criteria and current repository evidence. List unsupported assumptions, compatibility risks and tests that could falsify the plan. Do not edit files or call external services.

**Expected result:** a prioritized set of verifiable questions. If the response lacks evidence, request specific paths and counterexamples. A model's claimed security or reasoning ability is not proof of reliability. Avoid exposing secrets or confidential material to a candidate without approved data handling.
