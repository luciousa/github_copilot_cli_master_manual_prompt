# CLI 1.0.109 interactive help index

**Documentary evidence captured 2026-11-11 on Windows.** This is an index of primary names and first-line descriptions from local `copilot help commands`, not a complete alias/subcommand catalog. Command behavior, permissions, accounts and interactive execution are **unverified—do not execute**. Additional details and context are preserved in the [full captured help](../research/evidence/copilot-1.0.109-commands.txt); compare with [GitHub’s current CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference) and the [verification ledger](verification-ledger.md).

| Name | Built-in help summary |
|---|---|
| `/add-dir` | Allow file access to a directory and load its .github skills and agents as trusted configuration |
| `/agent` | Browse and select agents: /agent [name] |
| `/allow-all` | Enable all permissions (tools, paths, and URLs) |
| `/app` | Prefer a visual workspace? Try out the GitHub Copilot desktop app |
| `/ask` | Ask a side question or reopen a recently cached answer without adding to history |
| `/autopilot` | Toggle autopilot mode, or set an autopilot objective with an optional AI-credit limit (--max-ai-credits) |
| `/changelog` | Display changelog for CLI versions. Add 'summarize' to get an AI summary. |
| `/chronicle` | Session history tools and insights |
| `/clear` | Abandon this session and start fresh |
| `/collect-debug-logs` | Collect debug logs to a local .tgz file, share with GitHub after consent, or create a secret GitHub gist |
| `/compact` | Summarize conversation history to reduce context window usage. Optionally provide focus instructions. |
| `/computer` | Show or toggle Computer Use |
| `/config` | Open the configuration screen, or one area of it (e.g. '/config mcp'). Any other argument behaves as '/settings' does, so '/config model claude-sonnet-5.5' still sets the default model. |
| `/context` | Show context window token usage for the current model, split into System Prompt, Custom Instructions, System Tools, MCP Tools, Messages, Free Space and Buffer (room reserved for the reply and compaction). Experimental mode adds usage per skill, subagent, MCP server, tool and plugin, and the largest messages. |
| `/copy` | Copy the last response to the clipboard |
| `/cwd` | Change working directory or show current directory |
| `/delegate` | Send this session to GitHub and Copilot will create a PR; use --base to choose the PR target branch |
| `/diagnose` | Analyze session logs, including why a permission request needed approval |
| `/diff` | Review the changes made in the current directory |
| `/env` | Show loaded environment details (instructions, MCP servers, skills, agents, hooks, plugins, LSPs, extensions) |
| `/exit` | Exit the CLI; use 'print' to print the session after exiting alt screen |
| `/experimental` | Show available experimental features. /experimental on\|off is deprecated; use /settings experimental on\|off |
| `/feedback` | Report a bug or feature request as a public github/copilot-cli issue, or send private feedback. Logs are saved locally as copilot-feedback-<session-id>.tgz, secrets redacted, and not uploaded automatically: attach it yourself. |
| `/fleet` | Enable fleet mode for parallel subagent execution |
| `/footer` | Configure status line items |
| `/fork` | Fork the current session into a new session, optionally with a name, and switch to it; the original keeps running in the background. To fork a different session, /resume it first. Use /fork worktree to fork into a new worktree based on the current branch. |
| `/help` | Show help for interactive commands |
| `/ide` | Connect to an IDE workspace |
| `/index` | Inspect and manage this worktree's shared search index (experimental) |
| `/init` | Initialize instructions; add guidance after /init |
| `/instructions` | View and toggle custom instruction files |
| `/keep-alive` | Prevent sleep this run: on/off/busy (while working) or 30m/2h/1d (bare minutes). No args: status. keepAlive sets startup mode. |
| `/limits` | View or edit session limits; the AI Credit limit is a soft cap |
| `/list-dirs` | Display allowed directories and exact session path grants |
| `/login` | Log in to Copilot |
| `/logout` | Sign out of an account you added with /login or copilot login and delete its saved credentials: the token in the system keychain, or in config.json under the active Copilot home if it was stored as plain text. It does not sign out a COPILOT_GITHUB_TOKEN, GH_TOKEN or GITHUB_TOKEN token or a GitHub CLI login: unset the variable or run gh auth logout. |
| `/lsp` | Manage language server configuration |
| `/mcp` | Manage MCP server configuration |
| `/memory` | Show memory status, or enable/disable memory across sessions |
| `/model` | Select the AI model for this session (use 'auto' to let Copilot pick automatically). Use /config model to set the user default, '--repo'/'--local' to set the repo default, or 'plan'/'--plan' to set the plan-mode model. |
| `/move` | Move your uncommitted changes into a new git worktree and switch into it. Pass a branch name, a task to start, or nothing to auto-name. |
| `/new` | Start a new conversation |
| `/permissions` | Switch between permission modes |
| `/plan` | Create an implementation plan before coding |
| `/plugin` | Manage plugins and plugin marketplaces |
| `/pr` | Operate on pull requests for the current branch |
| `/refine` | Rewrite a rough, stream-of-consciousness prompt into a clear one for review (Ctrl+X / then /refine cleans up your current input) |
| `/remote` | Show remote status or toggle remote control from GitHub web and mobile |
| `/rename` | Rename the current session, or auto-generate a name from conversation |
| `/research` | Run deep research investigation using GitHub search and web sources |
| `/reset-allowed-tools` | Reset session tool and exact-path approvals, turn off allow-all, and clear saved approvals for this location |
| `/restart` | Restart the CLI, restoring supported live sessions in this process |
| `/resume` | Switch sessions by local or cloud history ID, task ID, or name |
| `/review` | Run code review agent to analyze changes |
| `/rewind` | Pick an earlier turn to rewind to: restore the conversation only, or also the files Copilot changed. A rewind cannot be undone: once rewound, the later turns are gone from the session, so /fork first to keep a copy of the conversation |
| `/rubber-duck` | Get an independent critique of your current work from the rubber duck agent |
| `/sandbox` | Manage sandbox settings, including file path permissions, network permissions, and more |
| `/search` | Search the conversation timeline (experimental) |
| `/security-review` | Analyze staged and unstaged changes for security vulnerabilities, or the branch diff when the working tree is clean. |
| `/session` | View and manage sessions. Use subcommands for details. |
| `/settings` | Open the settings UI, show, set, or unset a single value ('/settings unset <key>' removes it). Use '--repo'/'--local' to target repo settings. |
| `/share` | Open sharing actions for this session, or export with file, html, gist, research, or link |
| `/skills` | Manage skills for enhanced capabilities |
| `/statusline` | Configure status line items |
| `/subagents` | Configure each subagent's model and settings, or turn it on or off |
| `/tasks` | View running subagents and background shell commands, check their status, and open their live transcript or recent output |
| `/terminal-setup` | Configure terminal for multiline input support (shift+enter) |
| `/theme` | Open the color mode picker. /theme <mode> is deprecated; use /settings theme <mode> |
| `/update` | Update the CLI to the latest version |
| `/usage` | Display session usage metrics and statistics |
| `/user` | Manage signed-in accounts |
| `/version` | Display version information and check for updates |
| `/vim` | Toggle Vim mode for the input (hjkl/w/b/e/ge/0/^/$/gg/G motions, f/F/t/T/;/, char search, i/a/o insert, r/~/J/x/D/C edit, d/c/y operators, y/p/P yank & put, . repeat, u/ctrl+r undo & redo, counts, esc for normal mode) |
| `/voice` | Manage voice mode (dictation transcription via Foundry Local) |
| `/worktree` | Create a new git worktree from your configured base ref and switch into it, leaving your uncommitted changes behind. Use /new worktree for an empty session or /fork worktree to preserve the current context. The deprecated /worktree new command still works for now. |

Further work: map every alias and subcommand, side effect, prerequisite and lifecycle state against version-specific help and test the applicable behavior.
