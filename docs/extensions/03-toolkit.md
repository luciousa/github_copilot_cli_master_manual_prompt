<a id="e3-toolkit"></a>
# E3. Toolkit evaluation

**Outcomes:** select a minimal, evidence-backed full-stack toolkit and recognize what remains unverified. **Prerequisites:** [E1](01-mechanisms.md), [E2](02-lifecycle.md), and a defined task and trust policy.

## Provisional candidates

This is a candidate shortlist, not a set of approved installations. GitHub documents the mechanisms; this project tested only minimal local skill and plugin fixtures, not the installation, permissions, removal or interoperability of the recommended candidates. No third-party package is recommended without provenance and lifecycle review.

| Need | Candidate mechanism | Evidence and decision gate |
|---|---|---|
| Repository conventions across .NET and frontend work | CLI repository instructions | [CLI custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions); resolve scope and conflicts. |
| Repeatable cross-platform test review | Project skill | [CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills); inspect every included script and supported shell. |
| Separate architecture or test reviewer | Custom agent | [CLI agent guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/invoke-custom-agents); verify inheritance and tool restrictions. |
| GitHub issues or pull-request context | Built-in GitHub MCP server, if needed and permitted | [CLI MCP guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers); verify exposed tools, account and scopes. |
| Language-aware navigation | CLI-supported language-server integration | [Customization support](https://docs.github.com/en/copilot/reference/customization-cheat-sheet); verify executable provenance and runtime access. |
| Team-distributed collection | Plugin or marketplace after review | [Plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference); inspect package, update policy and V18. |

Cloud, database, CI and RAG integrations require explicit service-specific provenance, least-privilege permissions, data policy and verified installation/removal. Candidate names and commands are deliberately deferred until supported by evidence; popularity is not an evaluation criterion. A conceptual example cannot be treated as a working plugin or agent.

**Scenario:** a React/.NET team needs repository navigation and issue context. Start with reviewed repository instructions and the built-in capabilities that already meet the need. Evaluate GitHub MCP access only if issue or pull-request data is required, and inspect scopes before enabling tools. Add another server only when it fills a demonstrated gap.

**Illustrative prompt — not a shell command:**

> Inventory the integrations already available to this session and explain which are necessary for the requested repository review. Identify unknown permissions and provenance; do not install, update, disable or invoke external services.

Expected result: a proposed minimal toolkit with unresolved questions. If the runtime inventory is unavailable, mark it unknown. Verify setup, usage, upgrade and removal in a disposable environment before any recommendation becomes copy-ready. No installation commands have been validated in this batch.
