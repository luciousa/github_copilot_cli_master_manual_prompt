<a id="m3-evaluation"></a>
# M3. Repeatable model evaluation

**Outcomes:** compare permitted model configurations on representative work and report the limitations of the results. **Prerequisites:** [M1](01-selection.md), [M2](02-decisions.md), isolated test workspaces and an agreed data-handling policy.

## Evaluation protocol

1. Select a small, representative task set: for example a C# defect, TypeScript refactor, SQL review and repository-research question. Define acceptance tests and scoring criteria before seeing candidate outputs.
2. Fix repository revision, task prompt, available context, tool permissions, time budget and environment. Use separate clean copies or equivalent isolated starting states. Record any unavoidable differences.
3. Record CLI version, OS, selected model or automatic mode, reasoning/context settings, provider, date and policy constraints. Do not record credentials or confidential prompts in an unapproved location.
4. Apply the same review process to each candidate. Measure task completion, failing and passing tests, correctness, unsupported claims, tool requests and human correction effort. Record elapsed time and actual usage only when reliably measured.
5. Repeat enough representative trials to characterize variability; report the sample size and failures. Avoid treating one success as a universal capability or a small internal trial as a public benchmark.
6. Review results for security and reproducibility before selecting a candidate for the specific workflow. Re-evaluate after meaningful model, CLI, policy or repository changes.

**Scenario:** compare two allowed configurations on a fixed React pagination bug. The acceptance suite must detect the original bug and prevent an authorization regression. A reviewer inspects the diff without relying on the model's success narrative. Record test results, elapsed time and actual usage, and mark any unavailable measurement as unknown.

**Illustrative prompt — not a shell command:**

> Investigate the pagination defect described in the supplied issue. State the reproduction, propose the smallest correction and identify tests needed to detect the original failure. Stay within the provided workspace and ask before actions that change files.

**Expected result:** a comparable, reviewable plan or change, depending on the approved test phase. If candidates use different tools or context windows, report that difference instead of attributing all outcomes to model quality. Stop if isolation or approval boundaries cannot be maintained. Current rates and available models should be verified from [GitHub's pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) and [model guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model); no measurements have been performed for this manual.
