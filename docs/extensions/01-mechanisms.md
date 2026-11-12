<a id="e1-mechanisms"></a>
# E1. Choosing an extension mechanism

**Outcomes:** choose the smallest suitable mechanism and recognize its trust boundary. **Prerequisites:** [X1](../context/01-instructions.md), [A2](../agents/02-custom-agents.md) and a trusted workspace.

GitHub's [CLI customization overview](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/overview) describes the mechanisms below. “Documented” is not a claim that every version, plan or organization supports a feature. Minimal local skill and plugin lifecycle fixtures were tested; real integrations remain untested.

| Mechanism | Primary role | Trust and scope question |
|---|---|---|
| Instructions | Persistent guidance within an applicable scope | Who can edit it, and can it conflict with other guidance? |
| Skill | Task-specific instructions and optionally resources or scripts | What content or executable resources can load, and from where? |
| Custom agent | Specialist profile with instructions and tool configuration | Which tools and instructions does the agent receive? |
| Hook | Run configured commands at lifecycle events | What executes, when, under whose permissions? |
| MCP server | Provide external tools and data | What credentials, network destinations and operations does the server expose? |
| Connector | GitHub-managed connection to an external service | What account, scope and preview restrictions apply? GitHub's [support matrix](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) labels connectors preview. |
| Plugin | Package multiple customizations for distribution | What components and update behavior are included? |
| Marketplace | Catalog for discovering plugins | Who controls the catalog and each referenced source? |
| Language server | Code-intelligence integration where supported | Which executable and workspace data does it access? |

Use an instruction for a stable repository rule, a skill for a reusable task procedure, an agent for a defined role, and MCP only when external tools or data are needed. These are judgment guidelines; assess permissions and maintenance for the actual implementation. A marketplace listing or first-party label does not prove that every component is suitable for a particular environment.

**Scenario:** an API team needs consistent test review. First check whether repository instructions suffice; consider a focused skill or agent only if reusable specialization adds value. An MCP server is justified only if the task actually needs an external service.

**Illustrative prompt — not a shell command:**

> Compare the mechanisms already available in this repository for documenting API test review. Identify proposed scope and trust implications. Do not install, enable or execute extensions.

Expected result: an evidence-backed choice, not automatic installation. If support is unclear, consult the CLI-specific reference and installed help; do not transfer an IDE feature to the CLI by name alone.
