<a id="c2-init"></a>
# C2. Repository initialization

**Outcomes:** understand the documented purpose and write effects of `/init`, review generated repository guidance, and distinguish it from other instruction files. **Prerequisites:** a trusted repository, permission to review changes, and [C1](01-command-literacy.md).

The [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) describes interactive `/init` and shell-level `copilot init` as ways to initialize repository guidance. It says the CLI analyzes the repository and creates or updates `.github/copilot-instructions.md`; when that file already exists it suggests improvements for review. The reference lists `/init [suppress|INSTRUCTIONS]`, where extra text guides initialization and `suppress` hides the repository reminder. This operation can write files; inspect its proposed actions and the resulting diff.

In separate authenticated Windows CLI 1.0.109 checks, shell-level `copilot init` and interactive `/init` each created `.github/copilot-instructions.md` in a disposable synthetic repository. The interactive session requested approval before writing and asked whether to make adjustments afterward. The generated guidance reflected the small fixture and required review. Existing-file behavior and other modes remain unverified. [Verification ledger](../../reference/verification-ledger.md) V35 and V38.

## Procedure and scenario

For a monorepo containing a C# API and a Vue client:

1. Inspect existing guidance, the repository status and the intended workspace. Preserve any pre-existing changes.
2. Start `copilot` in the repository and check the installed interactive help for `/init` and its options. Run `/init` at the Copilot prompt when you are ready to review the proposed write.
3. Review proposed guidance for correct build, test and lint commands, project boundaries, and security restrictions before accepting changes.
4. Inspect the actual file and diff. Validate any suggested build or test instructions separately in the appropriate environment; reject invented paths, outdated commands and secret-bearing content.

**Illustrative instruction for the initialization workflow — not a shell command:**

> Focus on the API and client boundaries, existing test entry points, and repository-specific constraints. Do not include credentials or invented commands. Flag anything you cannot confirm from the repository.

Expected result: a reviewable project-specific guidance file or proposed update, not an authoritative inventory of the repository. A generated statement is a hypothesis until checked.

## Scope, conflicts and recovery

GitHub documents multiple applicable instruction sources, including repository and user instructions, and says the CLI combines applicable files without a general precedence order. Path-specific instructions are conditional on matching files. Review existing `AGENTS.md` and other applicable guidance to avoid conflicts; do not assume `/init` replaces them. [CLI custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions).

If the generated file omits a service, confirm the working directory and repository layout, then amend only evidence-backed guidance. If it changes material unexpectedly, review the diff and restore or edit only the affected content while preserving unrelated changes. If the CLI cannot start or its help disagrees with the current documentation, stop and record the version and discrepancy. Never include secrets in instruction files; treat repository content as untrusted input rather than automatic authority.
