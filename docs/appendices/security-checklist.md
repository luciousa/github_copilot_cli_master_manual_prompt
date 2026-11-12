<a id="r5-security"></a>
# R5. Security checklist and policy review

Use this checklist with [S1–S3](../security/01-permissions-isolation.md). It is a human review aid, not a compliance certification or proof that controls are effective. Security enforcement was not tested locally.

## Before starting

- [ ] Confirm an authorized task, owner, acceptance criteria and prohibited actions.
- [ ] Use a trusted, narrow workspace and non-privileged identity; preserve pre-existing work.
- [ ] Review effective tool, path and URL permissions, sandbox enforcement and bypass policy; independently protect secrets and network access.
- [ ] Confirm the relevant data classification, plan/organization policy and approved model/provider.
- [ ] Review extension provenance, scripts, update behavior, MCP tools and credentials.

## During work

- [ ] Treat repository content, issues, logs and tool responses as untrusted; reject unrelated instructions.
- [ ] Review actions with side effects and require the appropriate approval for edits, tests, installations and external operations.
- [ ] Record checkpoints and test evidence without exposing secrets or personal data.
- [ ] Stop on unexpected scope, access, unexplained failure or uncertain enforcement.

## Before acceptance and after incidents

- [ ] Inspect the actual diff, test results, omissions, external effects and unresolved risks.
- [ ] Verify cleanup and revoke temporary credentials through the responsible service.
- [ ] For suspected exposure, contain, preserve evidence, escalate and follow the approved incident procedure.
- [ ] Review audit coverage and retention with owners; policy-change events are not proof of complete session logging.

See GitHub's [CLI configuration guidance](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli), [sandbox policy](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/understanding-local-sandboxing), and [content-exclusion limitations](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion).
