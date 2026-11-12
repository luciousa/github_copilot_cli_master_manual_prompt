<a id="m1-selection"></a>
# M1. Model selection and availability

**Outcomes:** distinguish an account's available models from a general catalog, understand session and default selection, and identify the correct billing regime. **Prerequisites:** [F2](../fundamentals/02-setup.md), an authenticated CLI where permitted, and the applicable organization policy.

**Evidence date:** 2026-11-11. No model picker, account entitlement or selection was tested locally. The controls below are documented by GitHub; exact syntax and behavior are **unverified locally—do not execute** until checked against the installed version. [Choosing a model in Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model).

## Availability and controls

GitHub says available models depend on the Copilot plan and organization or enterprise settings. Its CLI guide describes an interactive `/model` picker and `--model` option, and says some models offer context-capacity or reasoning controls. A session selection persists if that session is resumed; a default setting may be overridden by project settings, managed policy or explicit invocation options. Verify each detail against your installed version and policy. [CLI model selection](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model).

The [live CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) lists model identifiers and descriptions, but is not an account-specific entitlement list or proof of support in older releases. Use the installed CLI's picker and documented controls to determine what is actually available; record the selected model, provider and settings with an evaluation. If a requested model is unavailable, investigate access and policy before selecting an approved alternative; do not assume an automatic fallback occurred.

GitHub documents an automatic selection option, Copilot Fusion, and model-specific configurations. Automatic selection can introduce another variable into comparisons; record the selection mode and any model information the CLI actually reports. Local models and subagent-specific settings have their own prerequisites and are outside the verified runtime scope of this batch. [CLI model selection](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model).

## Cost and quotas

GitHub's [models and pricing page](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) describes usage-based token pricing expressed in GitHub AI Credits and states one credit equals $0.01 USD. Included allowances, budgets, rates, caching and account policies affect actual charges; consult current individual or organization billing and do not infer an invoice from a model name. [Individual billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing); [organization billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/organizations-and-enterprises/billing).

GitHub separately documents legacy premium-request billing for eligible existing annual subscribers. Request multipliers are a legacy billing concept and must not be substituted for token-based pricing. Verify your actual billing regime. [Legacy billing](https://docs.github.com/en/copilot/reference/copilot-billing/request-based-billing-legacy/what-changed-with-billing).

## Scenario and checks

For a .NET service review, check the organization's allowed models and usage budget, select an available candidate using the verified local interface, and record its identity and settings. Make the task and acceptance tests identical when comparing an alternative. Inspect the billing dashboard after the work when usage is relevant; a request's predicted cost is not its measured cost.

**Illustrative prompt — not a shell command:**

> Review the authorization logic in the named service. Identify evidence for each finding, state uncertainties and propose tests. Do not change files or access production systems.

**Expected result:** a reviewable analysis whose findings require independent verification. If a model is absent, check plan, policy and session type. If selection appears not to take effect, inspect the current session and pending turn before assuming the model changed. Avoid publishing unsupported cost or performance rankings.
