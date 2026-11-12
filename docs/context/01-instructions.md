<a id="x1-instructions"></a>
# X1. Instructions and discovery

**Outcomes:** identify applicable CLI instruction sources, understand scoped guidance and avoid inventing a precedence hierarchy. **Prerequisites:** [C2](../commands/02-initialization.md), repository access and permission to inspect its guidance.

GitHub's [CLI custom-instructions guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) describes user-level `.copilot` instructions, repository-wide `.github/copilot-instructions.md`, path-specific `*.instructions.md`, and agent instruction files including `AGENTS.md`, `CLAUDE.md` and `GEMINI.md`. The guide describes discovery across repository and working-directory locations with different rules for modular files. It says applicable files are combined and does **not** define a general precedence order between them. Path-specific instructions apply to matching files.

GitHub documents `/instructions` for inspecting and toggling discovered instruction files. This command and discovery behavior are **unverified locally—do not execute** until checked in the installed version. Do not infer a CLI precedence rule from documentation for GitHub.com or an IDE. Subagent inheritance has separate rules documented in the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference); verify the target version before relying on it.

In a disposable Windows CLI 1.0.109 test, the non-interactive instruction-listing subcommand reported both repository-root fixture `AGENTS.md` and `.github/copilot-instructions.md`. This verifies only their listing in that setup, not interactive loading, matching, precedence or agent inheritance. [Recorded evidence](../../research/evidence/copilot-1.0.109-instruction-discovery.txt).

## Review workflow and example

In a monorepo, inventory user and repository guidance relevant to the C# API and Vue client. Identify contradictory build steps or permissions and resolve them with the responsible maintainers rather than assuming one wins. Confirm which files actually match the task and validate commands against the repository. Review instruction changes as code; instructions are guidance, not an access-control boundary.

**Conceptual instruction text — not a complete executable configuration:**

> For API changes, identify the relevant authorization tests and explain which were run. Do not include credentials or production data in output.

**Illustrative prompt — not a shell command:**

> Identify instruction files applicable to this task, summarize any contradictions, and cite their locations. Do not modify them or execute commands.

Expected result: a proposed inventory; independently inspect the discovered files and verify scoping. If expected instructions are missing, check location, current directory, matching rules, enablement and installed version. If they conflict, update the source of truth rather than relying on assumed priority.

## Import conflict and security

The CLI-specific guide restricts referenced files to relative paths within the applicable repository or custom-instructions directory, while the [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) describes absolute paths as supported. The difference is unresolved (V16). **Import examples are unverified—do not execute** until version-specific behavior and scope are tested. Treat instruction files and imported material as potentially untrusted; never add secrets and never let a repository file authorize access beyond the user's permissions.
