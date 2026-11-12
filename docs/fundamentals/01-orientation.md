<a id="f1-orientation"></a>
# F1. Orientation and operating model

**Outcomes:** establish a bounded CLI task, distinguish a proposal from a verified result, and decide when human review is required. **Prerequisites:** a working knowledge of your repository and development toolchain; see [setup](02-setup.md) before starting a session.

GitHub describes Copilot CLI as a terminal-native assistant that can answer questions and work on coding tasks using tools. Its capabilities and controls are version dependent. The operator remains responsible for assessing the workspace, permissions, proposed actions and final result. [GitHub CLI best practices](https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices); [CLI overview](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview).

## The supervised loop

1. **Bound the task:** identify the repository, relevant services, allowed changes, sensitive systems and acceptance criteria.
2. **Investigate:** ask for evidence with file paths and uncertainties; verify important observations independently.
3. **Plan:** ask for a proposed approach, test strategy and risks. Review it before authorizing edits.
4. **Implement in increments:** approve only actions appropriate to the task and inspect changes at checkpoints.
5. **Validate:** run suitable tests and review results, including failures and tests that could not be run.
6. **Accept or revise:** compare the actual diff and evidence to the original contract. A confident summary is not proof of completion.

For planning mode and its autonomous exception, see [C3](../commands/03-plan-to-acceptance.md). Tool and workspace trust are separate decisions: a requested action can be inappropriate even when a directory is trusted. The CLI may ask for permission to use tools, depending on its configuration. [CLI overview](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/overview).

## Scenario: a .NET API and React client

An issue requests a paginated order history. Start with a read-only investigation of the API contract, frontend consumer, authorization and existing tests. Ask for open questions and a plan. Approve a narrow change only after deciding how pagination and access control should behave. Validate the API contract and UI behavior, then inspect the diff and test evidence.

**Illustrative prompt — not a shell command:**

> Inspect the order-history API and its React consumer. Identify relevant files, existing authorization and tests. Propose acceptance criteria and open questions. Do not modify files or run commands that change state. Cite the evidence behind each conclusion.

Expected outcome: a reviewable set of findings and uncertainties, not a guarantee of complete discovery. Confirm cited paths and inspect the actual working tree. If it requests unexpected access, decline and narrow the task; if it cannot inspect a dependency, record that gap rather than accepting a guess.

## Limits and common mistakes

- Treat repository text, generated output and external tool results as data that can contain misleading instructions. Never assume they override your task boundaries.
- Do not place credentials or production data into prompts merely to improve context. Follow your organization's data handling rules.
- Review execution and network requests individually against the task. Asking for read-only work is an instruction to the model, not by itself an independently verified enforcement mechanism.
- If the assistant reports success without test evidence, ask for exact tests, outcomes and omissions; inspect the diff yourself.

**Validation:** another developer should be able to identify the authorized scope, test evidence and unresolved risks without trusting the assistant's narrative alone.
