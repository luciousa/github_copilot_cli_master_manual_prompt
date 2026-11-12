<a id="s1-permissions"></a>
# S1. Permissions and isolation

**Outcomes:** distinguish trusted directories, approvals, sandbox policy, content exclusion and external controls; review effective access before a task. **Prerequisites:** [F3](../fundamentals/03-sessions.md), [A1](../agents/01-supervised-autonomy.md), and your organization's security policy.

**Evidence date:** 2026-11-11. CLI 1.0.109 has reported version and help on Windows; permission and sandbox behavior has not been tested. Security procedures remain **unverified locally—do not execute** until checked against the installed version and effective policy. This guidance is not a guarantee of containment.

## Understand the layers

| Layer | What the documentation describes | Limit to account for |
|---|---|---|
| Directory trust | The CLI asks whether to trust the working directory and its contents. | Trusting a folder is not a per-action approval or a complete filesystem boundary. Avoid starting from a sensitive, broad directory. |
| Tool, path and URL approvals | Permissions control particular tool requests and access, subject to mode and existing grants. | GitHub says shell-path detection is heuristic; complex constructs, some variable expansions and new symlinks have limitations. |
| Local sandbox | OS sandboxing can restrict sandboxed child processes; built-in file tools enforce corresponding policy in software. | Verify enablement, effective policy, backend, bypass and platform. Not every process or remote service is necessarily inside it. |
| Content exclusion | Eligible organization policies can prevent supported Copilot tools from accessing excluded content. | It is not an OS boundary; indirect access, symlinks, remote filesystems and third-party MCP are documented limitations. |
| External controls | OS accounts and permissions, isolated environments, network controls, secret managers and organization review. | These are organizational safeguards, not automatic Copilot features; configure and test them independently. |

Sources: [CLI configuration](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli), [filesystem policy](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/understanding-local-sandboxing), and [content exclusion](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/content-exclusion).

## Review the effective boundary

1. Choose a trusted, narrowly scoped checkout and a non-privileged account. Keep secrets and unrelated sensitive files outside the working environment where practical.
2. Identify the active permission mode, existing approvals, accessible paths and URLs, sandbox enablement and effective policy. GitHub documents a sandbox-policy view; verify the target version's help before relying on it. [Local sandbox settings](https://docs.github.com/en/copilot/how-tos/cloud-and-local-sandboxes/configuring-local-sandbox-settings).
3. Check managed restrictions and whether a bypass is permitted. GitHub documents that managed sandbox behavior depends on settings and backend availability; an enabled setting alone is not proof that enforcement cannot be bypassed. [Enterprise managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).
4. Review every requested action for its actual command, inputs and consequences. Give the smallest necessary approval; inspect grants again when the task changes.

GitHub documents a platform difference: its Windows host-rule and upstream-proxy controls rely on programs honoring proxy settings, unlike the stated direct-connection enforcement on macOS and Linux. Use independently enforced network restrictions where required. Local sandboxing of an MCP server must be explicitly understood; remote servers do not execute inside the local sandbox. [Enterprise managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).

## Scenario and validation

A team investigates a TypeScript CI failure in a disposable checkout. It limits access to relevant source, uses redacted logs and reviews proposed commands. Before any network or package operation, the operator checks the effective policy and authorizes only the needed action. Validate the boundary using an approved test environment and known non-sensitive fixtures; do not probe production secrets.

**Illustrative prompt — not a shell command:**

> Examine the supplied redacted failure and propose diagnostic steps. Do not access credentials, contact external services, or change files. Ask before any command; list the information needed to verify each hypothesis.

Expected result: a reviewable diagnostic plan. If the sandbox is unavailable or a policy cannot be confirmed, stop sensitive work and use an approved alternative. A prompt, path exclusion or approval dialog alone is not proof of isolation.
