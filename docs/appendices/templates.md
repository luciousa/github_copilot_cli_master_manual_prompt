<a id="r6-templates"></a>
# R6. Prompt and template library

These are illustrative natural-language templates, not shell commands or verified configuration files. Replace bracketed fields with confirmed, non-sensitive information. Prompts do not enforce permissions; use actual controls and obtain the required approvals.

## Investigation

> Investigate [question] within [scope]. Cite relevant files and distinguish observed facts, assumptions and missing evidence. Do not modify files, access external services or run state-changing commands. Ask before actions outside this scope.

## Plan and review

> Propose a staged plan for [goal] against [acceptance criteria]. Include affected components, compatibility and security risks, test cases, rollback and open decisions. Wait for review before edits or external actions.

## Evidence-based acceptance

> Map each criterion in [contract] to the actual diff and supplied test results. Report failed or unrun checks and unresolved risks. Do not claim that a test passed without evidence or make the acceptance decision.

## Checkpoint

> Summarize the approved goal, decisions, changed files, tests and outcomes, unresolved issues and next step. Separate confirmed facts from assumptions and omit credentials. Do not change files.

## Conceptual instruction, agent and skill templates

These are content outlines only. **Unverified—do not execute or install:** exact frontmatter, path, tool restrictions and inheritance must be checked against the target CLI and current official documentation.

- **Instruction:** scope; repository conventions supported by evidence; applicable test expectations; security restrictions; owner and review date.
- **Agent:** role; allowed task boundaries; required evidence; minimal tools; instruction-inheritance decision; escalation and output format.
- **Skill:** purpose and trigger; prerequisites; procedure and approval points; supporting resources; validation and recovery; version and maintainer.

GitHub documents [instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions), [skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), and [custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents). The templates are starting points; validate executable artifacts and component-specific lifecycle steps before adopting them.
