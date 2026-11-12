<a id="s3-governance"></a>
# S3. Enterprise governance

**Outcomes:** define a practical policy, distinguish audit evidence from complete monitoring, and assess privacy and compliance obligations. **Prerequisites:** [S1](01-permissions-isolation.md), [S2](02-threats-response.md), and participation from the organization's security, privacy and platform owners.

## Documented controls and limits

GitHub documents enterprise CLI enablement, content exclusions, MCP policies and audit events for changes to enterprise policies affecting CLI. Cloud delegation also requires the relevant cloud-agent policy. These facts do not establish that every local command, prompt or session is centrally logged. [Administering Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/administer-copilot-cli-for-your-enterprise).

GitHub documents managed sandbox settings and their version and platform constraints. The current reference says adding managed `sandbox` settings requires CLI 1.0.93 or later; validate current requirements and effective behavior in your environment. Some settings affect local MCP or language servers, while remote MCP services execute elsewhere. Managed policy, backend availability, bypass settings and network rules must be assessed together. [Enterprise managed settings](https://docs.github.com/en/copilot/reference/enterprise-administrators/enterprise-managed-settings).

Disabling first-party client-side telemetry does not disable GitHub server-side collection or every separately configured telemetry export. Logging prompts and tool use can itself expose sensitive information; use data minimization, redaction, access controls and retention rules. GitHub's documentation describes these distinctions; actual retention, data processing terms and plan-specific settings must be reviewed for the organization and contract. [CLI configuration](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli); [CLI hooks tutorial](https://docs.github.com/en/copilot/tutorials/copilot-cli-hooks).

## Conceptual policy template

This is a **review template**, not executable configuration or a claim of compliance. An authorized owner must replace each bracketed decision and validate it against the current service, contract and law.

> **Owner and scope:** [responsible team; repositories, identities and environments].
>
> **Data:** [permitted classifications; prohibited data; redaction and secret-handling rules].
>
> **Access:** [approved tools, extensions and external services; least-privilege account and credential requirements].
>
> **Risk and approval:** [which local changes, migrations, network actions and external writes require review; stop and escalation conditions].
>
> **Isolation:** [supported platforms, required sandbox and independent OS/network controls; handling when enforcement is unavailable].
>
> **Evidence and retention:** [what is logged, where, access, retention, redaction and audit review owner].
>
> **Incident response:** [containment, credential rotation, preservation, internal notification and recovery owners].
>
> **Review cadence:** [policy owner, verification schedule and change-control process].

## Scenario and validation

For a regulated multi-service team, the platform owner documents effective managed settings and tests them in a disposable environment; the security owner reviews extension access and network restrictions; the privacy owner verifies contract terms and retention. A developer uses a bounded test account and a redacted issue. The team samples actual policy events and local evidence to determine what is and is not auditable.

**Illustrative prompt — not a shell command:**

> Compare this redacted draft policy with the supplied technical controls. List assumptions, missing owners and claims that need evidence. Do not change settings, access accounts or make legal conclusions.

Expected result: a list of review items, not a compliance certification. If a managed setting cannot be verified or logs are missing, treat the control as unconfirmed and escalate. Recheck vendor documentation, service terms and policy behavior before rollout; these controls have not been tested in this project.
