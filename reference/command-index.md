# Initial CLI command index

**Partial index — as of 2026-11-11.** CLI 1.0.109 reported [built-in interactive command help](../research/evidence/copilot-1.0.109-commands.txt) on Windows. Entries are also based on GitHub's live [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference); behavior remains **unverified—do not execute**. This is not the promised exhaustive catalog: full arguments, aliases, availability and side effects must be checked before release.

| Form / context | Documented purpose | Material review point |
|---|---|---|
| `copilot` / shell | Start the interactive CLI | Review workspace trust and effective permissions. |
| `copilot help [TOPIC]` / shell | Display help | Available topics vary by version. |
| `copilot init` / shell; `/init [suppress|INSTRUCTIONS]` / interactive | Initialize repository guidance; slash form can suppress reminder or receive guidance | May create or update instructions; see [C2](../docs/commands/02-initialization.md). |
| `/help` / interactive | Show interactive command help | Does not establish entitlement to all features. |
| `/plan [PROMPT]` / interactive | Create an implementation plan | Approval behavior varies with configuration; see [C3](../docs/commands/03-plan-to-acceptance.md). |
| `/model` / interactive; `--model` / shell option | Select a model | Account and policy dependent; see [M1](../docs/models/01-selection.md). |
| `/instructions` / interactive | View or toggle discovered instruction files | Discovery and inheritance are version-sensitive. |
| `/context`, `/compact` / interactive | Inspect context or compact session history | Compaction is a lossy summary; see [X2](../docs/context/02-context-lifecycle.md). |
| `/agent`, `/fleet` / interactive | Select agents; request parallel subagent execution | Verify available agents, scope and client limitations. |
| `/delegate` / interactive | Delegate to cloud agent | Can create external branch and draft PR; [delegation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/delegate-tasks-to-cca). |
| `/sandbox` / interactive | Inspect or configure sandbox | Settings can have persistent or session effects; check effective policy and bypass. |
| `/plugin`, `/skills`, `/mcp` / interactive | Manage separate extension mechanisms | Installs, removal and external access require review. |

## Completion gate

Enumerate every documented slash command, syntax variant, alias, prerequisite, lifecycle label, side effect and version, and compare with version-pinned local help. Record unsupported, removed and experimental entries with evidence; do not infer absence from this partial list. Link every catalog claim to a source and mark entries untested until runtime validation where required.

The [1.0.109 interactive help index](commands-1.0.109.md) expands the primary names with their first-line built-in descriptions. The [full captured help](../research/evidence/copilot-1.0.109-commands.txt) includes extra details not represented by the index. Neither source proves that all aliases or interactive behaviors have been tested.

## Names reported by version 1.0.109 built-in help

These 75 primary names were extracted from the captured Windows help output. They are a version-specific discovery list, not proof that every alias, subcommand or runtime feature is available to a given account. **Unverified—do not execute** until behavior and permissions are checked. See the [captured help](../research/evidence/copilot-1.0.109-commands.txt) for descriptions and [live CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) for additional documented syntax.

/add-dir · /agent · /allow-all · /app · /ask · /autopilot · /changelog · /chronicle · /clear · /collect-debug-logs · /compact · /computer · /config · /context · /copy · /cwd · /delegate · /diagnose · /diff · /env · /exit · /experimental · /feedback · /fleet · /footer · /fork · /help · /ide · /index · /init · /instructions · /keep-alive · /limits · /list-dirs · /login · /logout · /lsp · /mcp · /memory · /model · /move · /new · /permissions · /plan · /plugin · /pr · /refine · /remote · /rename · /research · /reset-allowed-tools · /restart · /resume · /review · /rewind · /rubber-duck · /sandbox · /search · /security-review · /session · /settings · /share · /skills · /statusline · /subagents · /tasks · /terminal-setup · /theme · /update · /usage · /user · /version · /vim · /voice · /worktree
