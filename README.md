# GitHub Copilot CLI Advanced Vibe Coding Master Reference

**Evidence reviewed 2026-11-11.** This manual is for developers practicing specification-led, supervised software engineering with GitHub Copilot CLI. Windows CLI 1.0.109 was used for selected installation, planning, initialization and synthetic prompt checks; the [verification ledger](reference/verification-ledger.md) records the results and limits. Availability and behavior vary with CLI version, platform, account and organizational policy.

The guide distinguishes GitHub-documented behavior from observations in the test environment. Most complete recipes, real third-party integrations, macOS and Linux have not been tested; check the relevant version and permissions. Cookbook prompts are task text, not shell commands.

## Chapters

1. [F1: Orientation and operating model](docs/fundamentals/01-orientation.md)
2. [F2: Setup and lifecycle](docs/fundamentals/02-setup.md)
3. [F3: Sessions and configuration](docs/fundamentals/03-sessions.md)
4. [C1: Command literacy](docs/commands/01-command-literacy.md)
5. [C2: Repository initialization](docs/commands/02-initialization.md)
6. [C3: Plan to accepted change](docs/commands/03-plan-to-acceptance.md)
7. [C4: Interactive and automation reference](docs/commands/04-operation-reference.md)
8. [M1: Model selection and availability](docs/models/01-selection.md)
9. [M2: Task-based model decisions](docs/models/02-decisions.md)
10. [M3: Repeatable model evaluation](docs/models/03-evaluation.md)
11. [X1: Instructions and discovery](docs/context/01-instructions.md)
12. [X2: Context lifecycle](docs/context/02-context-lifecycle.md)
13. [X3: Task contracts and prompting](docs/context/03-task-contracts.md)
14. [A1: Supervised autonomy](docs/agents/01-supervised-autonomy.md)
15. [A2: Custom agents and delegation](docs/agents/02-custom-agents.md)
16. [A3: End-to-end delivery](docs/agents/03-end-to-end.md)
17. [E1: Choosing an extension mechanism](docs/extensions/01-mechanisms.md)
18. [E2: Extension lifecycle and trust](docs/extensions/02-lifecycle.md)
19. [E3: Toolkit evaluation](docs/extensions/03-toolkit.md)
20. [S1: Permissions and isolation](docs/security/01-permissions-isolation.md)
21. [S2: Threats and incident response](docs/security/02-threats-response.md)
22. [S3: Enterprise governance](docs/security/03-governance.md)
23. [Cookbook contract and status](docs/cookbook/00-recipe-contract.md)
24. [K01–K15: Discovery and planning](docs/cookbook/01-discovery-planning.md)
25. [K16–K30: Brownfield and quality](docs/cookbook/02-brownfield-quality.md)
26. [K31–K45: Modernization and operations](docs/cookbook/03-modernization-operations.md)
27. [K46–K60: Full-stack and AI systems](docs/cookbook/04-fullstack-ai.md)
28. [K61–K80: Context, governance and recovery](docs/cookbook/05-context-recovery.md)

References include the [command index](reference/command-index.md), [slash-command catalog](reference/slash-command-catalog.md), [version 1.0.109 help index](reference/commands-1.0.109.md), [configuration index](reference/configuration-index.md), and [published model matrix](reference/models-live-matrix.md). The live documentation and local version-specific help can differ.

Appendices: [extensions](docs/appendices/extensions.md), [security checklist](docs/appendices/security-checklist.md), [prompt and template library](docs/appendices/templates.md), [troubleshooting and FAQ](docs/appendices/troubleshooting.md), and [glossary and topic index](docs/appendices/glossary-index.md).

## Build the Word document

The Python project combines the guide and reference Markdown into a Word document with a cover, author, contents, headers, footers and page numbers. Generating the document does not verify its outstanding claims or recipes.

Requirements: Python 3.11 or later, Pandoc on `PATH`, and the project's Python dependencies. Microsoft Word and `pywin32` are optional; when available on Windows, the builder updates the Word table of contents. The output retains clickable contents if Word automation is unavailable. In Word, right-click the table of contents and select **Update Field** to refresh page numbers after editing.

Install and build from the project root:

```text
python -m pip install -e .
python -m reference_builder.cli
```

On Windows, install the optional Word integration with `python -m pip install -e ".[windows]"`. Configure title, author, section order, typography and output paths in [document.toml](document.toml). Use `python -m reference_builder.cli --help` for options; `--no-word` skips Word automation and `--output PATH` selects another DOCX destination. The default output is `releases/copilot-cli-master-reference-lucio.docx`, leaving the earlier partial-draft document intact. A companion build report lists all included files and unavailable checks. Research logs and scripts are not included as chapters; references to them are identified as source-repository material.

For development checks, install `python -m pip install -e ".[test]"` and run `python -m pytest -q tests`.

See the [source registry](reference/source-registry.md) and [verification ledger](reference/verification-ledger.md) for sources, results, conflicts and limitations. Earlier partial snapshots in `releases/` are preserved separately from the current Word build.
