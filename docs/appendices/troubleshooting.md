<a id="r7-troubleshooting"></a>
# R7. Troubleshooting and FAQ

**Status:** diagnostic guidance, not a tested runbook. Preserve existing work and redact secrets before collecting or sharing evidence. Verify commands against the installed version before executing them.

| Symptom | First checks | Escalate or recover |
|---|---|---|
| Executable missing or startup fails | Record OS, shell, install source, version if obtainable and exact redacted error. | Use [installation guidance](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli); do not assume installation succeeded because a link exists. |
| Authentication or access denied | Distinguish login, seat, organization policy and network issues. | Consult [authentication troubleshooting](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth); do not disclose tokens. |
| Command or model unavailable | Compare actual CLI help, version, plan, policy and session type. | Record the mismatch; select a permitted alternative only after checking scope. |
| Instructions not applied | Inspect expected location, path match, discovery and disabled state. | Avoid assuming precedence; resolve conflicts with owners and verify target-version behavior. |
| Permission or sandbox denial | Review the effective policy, operation and required access. | Reduce scope or request an authorized policy decision; do not bypass a control merely to make a task succeed. |
| Lost context or interrupted session | Compare checkpoint, actual working tree, running processes and test results. | Preserve unrelated work; see [X2](../context/02-context-lifecycle.md). |
| Extension missing or unsafe | Check source, version, configuration scope, policy and component type. | Disable or contain through approved procedures; revoke credentials separately if necessary. |
| Failing tests or wrong edits | Compare baseline, diff and failure output. | Stop repeated retries, isolate the failure and obtain approval for recovery. |

**Does plan mode guarantee no side effects?** GitHub documents protections for project changes but also limitations, including some shell and external-tool behavior. Verify mode and effective permissions; do not use a prompt as the sole isolation boundary. [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

**Does removing a plugin revoke a service credential?** Do not assume so. Verify local state and separately revoke any service authorization under the service owner's procedure.

**Can a current online command be used on an older CLI?** Check version-specific support, syntax and policy. CLI 1.0.109 help and selected interactive workflows were observed locally; the [verification ledger](../../reference/verification-ledger.md) states their limits.
