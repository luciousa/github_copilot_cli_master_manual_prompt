<a id="c1-command-literacy"></a>
# C1. Command literacy

**Outcomes:** distinguish shell commands, CLI commands and options, interactive slash commands and natural-language prompts. **Prerequisites:** [F2](../fundamentals/02-setup.md) and [F3](../fundamentals/03-sessions.md).

| Form | Interpreter | Example role | Principal risk |
|---|---|---|---|
| Shell command | PowerShell, Bash or another shell | Starts a program or changes the environment | Shell quoting and command side effects |
| CLI subcommand / flag | Copilot CLI invoked from a shell | Selects an operation or configures a session | Version-specific syntax and settings |
| Slash command | Copilot CLI interactive prompt | Requests an interactive CLI operation | Command-specific side effects; not a shell command |
| Natural-language prompt | Copilot agent | Describes a task or desired answer | Ambiguous scope and proposed tool use |

The [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) documents `copilot` as an interactive entry point, `copilot help [TOPIC]` as command-line help and `/help` as interactive help. It lists `/init [suppress|INSTRUCTIONS]` and `/plan [PROMPT]` as interactive commands. Exact behavior, arguments and availability are version dependent. **These examples are documentation-backed but unverified locally—do not execute until checked against the target installation.**

## Apply the distinction

For a Node service in a monorepo, first establish which terminal and workspace you are using. Consult the matching CLI's help before selecting a mode or changing settings. In the interactive session, issue slash commands only at the CLI prompt; put a task request in natural language. Keep quoted shell examples specific to PowerShell or POSIX when expansion differs. Do not paste interactive slash commands into the system shell and assume they mean the same thing.

**Illustrative prompt — not a shell command:**

> Explain which files and tests are relevant to the Node service's retry behavior. Provide paths and uncertainties. Do not edit files or run state-changing commands.

Expected result: cited observations and proposed next steps. Independently check important paths and any requested tool action. If the command is not recognized, inspect the installed version's help and policy; do not replace it with a similarly named command from an IDE or another agent.

## Safety and limitations

Slash commands may initiate actions and are not inherently read-only. Shell arguments can expand differently across operating systems; avoid constructing commands containing secrets or untrusted pasted text. The exhaustive catalog, aliases and version matrix are planned for a later batch and must not be inferred from this introductory table.
