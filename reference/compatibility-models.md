# Initial compatibility and model matrix

**Snapshot: 2026-11-11.** CLI 1.0.109 was tested on Windows with a signed-in account for selected synthetic prompts, planning and initialization; the [verification ledger](verification-ledger.md) records exact scope. Blank or unknown cells are not evidence of support or absence. Consult current [installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli), [model selection](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/choose-a-model) and [plans](https://docs.github.com/en/copilot/get-started/plans).

| Dimension | Documentation baseline | Unverified before release |
|---|---|---|
| Windows | PowerShell 6 or later listed; WinGet and npm channels documented. CLI 1.0.109, pinned npm installation, authentication and selected interactive workflows were tested in isolated environments. | Other install channels and interactive workflows. |
| macOS | Homebrew, npm and install-script channels documented. | OS/architecture/version matrix and local tests; Homebrew discrepancy V04. |
| Linux | Homebrew, npm and install-script channels documented. | Distribution, architecture, sandbox backend, installation and shell variants. |
| Organization access | CLI policy and applicable seat/plan control access. | This user's entitlement and effective organization settings. |
| Model selection | Models vary by plan and organization/enterprise policy. | Account-specific picker contents, retirement dates and configuration support. |
| Billing | Usage-based AI credits and qualifying legacy request-based billing are distinct. | Actual plan, rates, budgets and charges; refresh [pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing). |
| Managed sandbox | GitHub's current managed settings reference states CLI 1.0.93 or later for the managed `sandbox` setting. | Host support, deployed policy, bypass and enforcement; see V23. |

## Model identifiers in the live CLI reference

The following identifiers appeared in GitHub's [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) accessed 2026-11-11. This is a documentary snapshot, **not** the model picker from CLI 1.0.109 or an account entitlement list. The reference's release status, minimum CLI version, per-plan eligibility and pricing were not established for these rows. Model availability changes and may be restricted by policy; no named model is assigned a universal rank here.

| Documented identifier | Documented characterization | Local account availability / lifecycle |
|---|---|---|
| `claude-sonnet-5.5` | General-purpose coding; described as default in the live reference | Unverified |
| `claude-opus-5.5` | Complex tasks | Unverified |
| `claude-haiku-5.5` | Lightweight operations | Unverified |
| `claude-haiku-4.5` | Lightweight operations | Unverified |
| `gpt-5.3-codex` | Code-focused tasks | Unverified |
| `gpt-6.1-sol` | Opt-in recommendation | Unverified |
| `gpt-6.1-terra` | Opt-in recommendation | Unverified |
| `gpt-6-astra` | Opt-in recommendation | Unverified |
| `gpt-6-luna` | Opt-in recommendation | Unverified |
| `gemini-3.8-flash` | Fast responses | Unverified |

The characterizations are attributed to GitHub, not independent measurements. The linked model matrix provides GitHub's published lifecycle, client and plan information; verify footnotes and effective restrictions for your own account. No account-specific model picker or measured benchmark has been validated in this project.

## Illustrative published usage rates

GitHub's [models and pricing reference](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing), accessed 2026-11-11, lists these default-tier rates in USD per one million tokens. They are examples from a larger, changing table; they do not establish that a model is available to a particular CLI account. Long-context tiers, cached input, cache writes, included allowances, budgets and legacy billing may change the effective charge.

| Model in GitHub pricing table | Input | Output | Default-tier input threshold |
|---|---:|---:|---|
| GPT-5.3-Codex | $1.75 | $14.00 | Not applicable |
| GPT-6.1 Sol | $2.00 | $10.00 | Up to 272K tokens |
| GPT-6.1 Terra | $1.00 | $5.00 | Up to 272K tokens |

For example, at the listed GPT-6.1 Sol default-tier rates, 100,000 uncached input tokens plus 10,000 output tokens gives $0.20 + $0.10 = $0.30 before allowances, cache-write charges or other adjustments. GitHub states that one AI credit equals $0.01; consult the current source and your billing settings before forecasting actual charges.

The [published model matrix](models-live-matrix.md) preserves the plan and client support markers recovered from GitHub's accessible HTML (V37). Footnotes, current account access and policy still need checking in the linked live source and actual session picker.
