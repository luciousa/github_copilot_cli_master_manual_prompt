# Initial configuration and CLI options index

**Partial index — as of 2026-11-11.** CLI 1.0.109 [built-in help](../research/evidence/copilot-1.0.109-help.txt) has been captured on Windows; configuration behavior remains **unverified—do not execute or apply**. Consult the live [CLI configuration directory reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) and [command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference), then verify the installed version and managed policy.

| Item | Documented role | Validation gap |
|---|---|---|
| `~/.copilot/settings.json` | User settings; `COPILOT_HOME` changes the configuration home | Effective path, parsing and policy not tested. |
| `.github/copilot/settings.json` | Repository settings for supported overrideable keys | Exact scope and supported keys depend on version. |
| `.github/copilot/settings.local.json` | Local repository overrides for supported keys | Verify precedence, privacy and ignored-file policy. |
| `config.json` | CLI-managed state including trusted folders; current docs separate this from user settings | Do not overwrite internal state or assume older versions behave identically. |
| `--model` | Model selection | Availability and effective selection depend on account, mode and policy. |
| `--autopilot` | Autonomous continuation | Distinct from tool approvals; exact version and policy untested. |
| `--allow-all` / `--yolo` | Broad tool, path and URL approvals per documentation | High impact; managed policy may prohibit it. Not a sandbox. |
| `--no-ask-user` | Suppress user clarification requests | Does not itself enable autonomous continuation. |
| `--disable-client-telemetry` | Disable specified client-side telemetry for an invocation | Does not disable server-side collection or all configured exports. |

The current configuration reference describes a general order from built-in defaults through managed baseline, user, repository, local, environment and command-line settings, with important managed permission and sandbox exceptions. Do not equate this settings order with instruction-file precedence. Verify each setting's supported scope and effective managed policy in the target version. [Configuration reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference).

**Completion gate:** capture full options, environment variables, config paths, defaults, version introduction/removal, scopes, precedence and examples against target-version help. Reconcile settings with managed policy and [verification ledger](verification-ledger.md); never publish secrets in configuration examples.

For the target build, the [option help index](options-1.0.109.md), [global help](../research/evidence/copilot-1.0.109-help.txt), [configuration help](../research/evidence/copilot-1.0.109-config-help.txt) and [environment help](../research/evidence/copilot-1.0.109-environment-help.txt) provide version-specific discovery. These are captured help, not tested settings or proof of account entitlement. In particular, setting a value can persist or change permission scope; inspect help and policy before any configuration change.
