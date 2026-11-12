# GitHub Copilot CLI slash-command catalog

**Documentation accessed:** 2026-11-11 20:42 EST. **Local help baseline:** Windows CLI 1.0.109. The signatures below come from the [live GitHub CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference#slash-commands-in-the-interactive-interface); the middle column is the first-line **command-family** summary from [captured 1.0.109 help](../research/evidence/copilot-1.0.109-commands.txt), not proof that the exact live signature exists in 1.0.109. Features, aliases, arguments and lifecycle status can change. Check target-version interactive help and policy before use; untested syntax is **Unverified—do not execute**.

The online table contained 95 entries at access. Rows represent documented variants or subcommands, not unique commands; local help is not a complete account-specific inventory. Examples and details, prerequisites and version-specific exceptions are in the source reference. Inspect the requested action before approval: commands can change settings, create or remove files, transmit data, delegate work or alter external resources. The side-effect column is a conservative review flag, not a safety certification.

| Live documented syntax and aliases | 1.0.109 local family summary | Review |
|---|---|---|
| /add-dir PATH | Allow file access to a directory and load its .github skills and agents as trusted configuration | Review side effects and permissions |
| /after [DELAY PROMPT],/after | Not listed in captured 1.0.109 primary-command help | Review side effects and permissions |
| /agent | Browse and select agents: /agent [name] | Check command and session context |
| /app | Prefer a visual workspace? Try out the GitHub Copilot desktop app | Check command and session context |
| /ask [QUESTION],/btw [QUESTION] | Ask a side question or reopen a recently cached answer without adding to history | Check command and session context |
| /allow-all [on\|off\|show],/yolo [on\|off\|show] | Enable all permissions (tools, paths, and URLs) | Review side effects and permissions |
| /autopilot [OBJECTIVE],/goal [OBJECTIVE] | Toggle autopilot mode, or set an autopilot objective with an optional AI-credit limit (--max-ai-credits) | Review side effects and permissions |
| /changelog [summarize] [VERSION\|last N\|since VERSION],/release-notes [summarize] [VERSION\|last N\|since VERSION] | Display changelog for CLI versions. Add 'summarize' to get an AI summary. | Check command and session context |
| /chronicle &lt;standup\|tips\|improve\|reindex\|skills create\|skills review\|skills status&gt; | Session history tools and insights | Check command and session context |
| /clear [PROMPT],/new [PROMPT],/reset [PROMPT] | Abandon this session and start fresh | Review side effects and permissions |
| /clikit [COMPONENT] | Not listed in captured 1.0.109 primary-command help | Check command and session context |
| /collect-debug-logs [file\|gist\|share] [PATH] | Collect debug logs to a local .tgz file, share with GitHub after consent, or create a secret GitHub gist | Review side effects and permissions |
| /compact [FOCUS-INSTRUCTIONS] | Summarize conversation history to reduce context window usage. Optionally provide focus instructions. | Check command and session context |
| /context | Show context window token usage for the current model, split into System Prompt, Custom Instructions, System Tools, MCP Tools, Messages, Free Space and Buffer (room reserved for the reply and compaction). Experimental mode adds usage per skill, subagent, MCP server, tool and plugin, and the largest messages. | Check command and session context |
| /copy | Copy the last response to the clipboard | Check command and session context |
| /cwd,/cd [PATH] | Change working directory or show current directory | Check command and session context |
| /delegate [PROMPT] | Send this session to GitHub and Copilot will create a PR; use --base to choose the PR target branch | Review side effects and permissions |
| /diagnose [PROMPT],/diagnose | Analyze session logs, including why a permission request needed approval | Check command and session context |
| /diff | Review the changes made in the current directory | Check command and session context |
| /downgrade VERSION | Not listed in captured 1.0.109 primary-command help | Review side effects and permissions |
| /env | Show loaded environment details (instructions, MCP servers, skills, agents, hooks, plugins, LSPs, extensions) | Check command and session context |
| /every [INTERVAL] PROMPT,/every | Not listed in captured 1.0.109 primary-command help | Review side effects and permissions |
| /exit,/quit | Exit the CLI; use 'print' to print the session after exiting alt screen | Review side effects and permissions |
| /extensions [manage\|mode],/extension | Not listed in captured 1.0.109 primary-command help | Review side effects and permissions |
| /experimental [on\|off\|show] | Show available experimental features. /experimental on\|off is deprecated; use /settings experimental on\|off | Review side effects and permissions |
| /feedback,/bug | Report a bug or feature request as a public github/copilot-cli issue, or send private feedback. Logs are saved locally as copilot-feedback-&lt;session-id&gt;.tgz, secrets redacted, and not uploaded automatically: attach it yourself. | Check command and session context |
| /fleet [PROMPT] | Enable fleet mode for parallel subagent execution | Review side effects and permissions |
| /help | Show help for interactive commands | Check command and session context |
| /ide | Connect to an IDE workspace | Check command and session context |
| /init [suppress\|INSTRUCTIONS] | Initialize instructions; add guidance after /init | Review side effects and permissions |
| /instructions | View and toggle custom instruction files | Check command and session context |
| /keep-alive [on\|off\|busy\|DURATION],/caffeinate [on\|off\|busy\|DURATION] | Prevent sleep this run: on/off/busy (while working) or 30m/2h/1d (bare minutes). No args: status. keepAlive sets startup mode. | Check command and session context |
| /limits | View or edit session limits; the AI Credit limit is a soft cap | Check command and session context |
| /limits set max-ai-credits VALUE | View or edit session limits; the AI Credit limit is a soft cap | Check command and session context |
| /limits unset [max-ai-credits\|all] | View or edit session limits; the AI Credit limit is a soft cap | Check command and session context |
| /list-dirs | Display allowed directories and exact session path grants | Check command and session context |
| /login | Log in to Copilot | Review side effects and permissions |
| /logout | Sign out of an account you added with /login or `copilot login` and delete its saved credentials: the token in the system keychain, or in config.json under the active Copilot home if it was stored as plain text. It does not sign out a COPILOT_GITHUB_TOKEN, GH_TOKEN or GITHUB_TOKEN token or a GitHub CLI login: unset the variable or run `gh auth logout`. | Review side effects and permissions |
| /lsp [show\|test\|reload\|logs\|help] [SERVER-NAME] | Manage language server configuration | Review side effects and permissions |
| /mcp [config\|list\|show\|add\|edit\|delete\|disable\|enable\|auth\|reload\|search] [SERVER-NAME] | Manage MCP server configuration | Review side effects and permissions |
| /model [--session\|--global\|--repo\|--local] [MODEL\|auto TIER],/models | Select the AI model for this session (use 'auto' to let Copilot pick automatically). Use /config model to set the user default, '--repo'/'--local' to set the repo default, or 'plan'/'--plan' to set the plan-mode model. | Review side effects and permissions |
| /permissions [default\|assisted\|allow-all\|show] | Switch between permission modes | Review side effects and permissions |
| /permissions reset | Switch between permission modes | Review side effects and permissions |
| /plan [PROMPT] | Create an implementation plan before coding | Check command and session context |
| /plugin | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin install SOURCE | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin update PLUGIN[@MARKETPLACE] | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin uninstall PLUGIN[@MARKETPLACE](aliasesremove,rm) | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin list(aliasls) | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin marketplace add SOURCE | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin marketplace remove NAME | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin marketplace list | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin marketplace browse NAME | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /plugin marketplace update [NAME](aliasrefresh) | Manage plugins and plugin marketplaces | Review side effects and permissions |
| /pr [view\|create\|fix\|auto\|automerge] | Operate on pull requests for the current branch | Review side effects and permissions |
| /refine TEXT | Rewrite a rough, stream-of-consciousness prompt into a clear one for review (Ctrl+X / then /refine cleans up your current input) | Check command and session context |
| /remote [on\|off] | Show remote status or toggle remote control from GitHub web and mobile | Review side effects and permissions |
| /rename [NAME] | Rename the current session, or auto-generate a name from conversation | Check command and session context |
| /research TOPIC | Run deep research investigation using GitHub search and web sources | Check command and session context |
| /reset-allowed-tools | Reset session tool and exact-path approvals, turn off allow-all, and clear saved approvals for this location | Review side effects and permissions |
| /restart | Restart the CLI, restoring supported live sessions in this process | Review side effects and permissions |
| /resume [SESSION-ID],/continue [SESSION-ID] | Switch sessions by local or cloud history ID, task ID, or name | Check command and session context |
| /review [PROMPT] | Run code review agent to analyze changes | Check command and session context |
| /rubber-duck [PROMPT] | Get an independent critique of your current work from the rubber duck agent | Check command and session context |
| /sandbox [config\|status\|policy [COMMAND]\|enable\|disable] | Manage sandbox settings, including file path permissions, network permissions, and more | Review side effects and permissions |
| /sandbox ca [create\|trust\|rotate\|remove] | Manage sandbox settings, including file path permissions, network permissions, and more | Review side effects and permissions |
| /search [QUERY],/find [QUERY] | Search the conversation timeline (experimental) | Check command and session context |
| /security-review [PROMPT] | Analyze staged and unstaged changes for security vulnerabilities, or the branch diff when the working tree is clean. | Check command and session context |
| /session [info\|checkpoints [n]\|files\|plan\|rename [NAME]\|cleanup\|prune\|delete [ID]\|delete-all],/sessions [info\|checkpoints [n]\|files\|plan\|rename [NAME]\|cleanup\|prune\|delete [ID]\|delete-all] | View and manage sessions. Use subcommands for details. | Review side effects and permissions |
| /settings [--repo\|--local] [show KEY\|KEY\|KEY VALUE],/config [--repo\|--local] [show KEY\|KEY\|KEY VALUE] | Open the settings UI, show, set, or unset a single value ('/settings unset &lt;key&gt;' removes it). Use '--repo'/'--local' to target repo settings. | Review side effects and permissions |
| /share [link\|off\|file\|html\|gist\|research] [...],/export [...] | Open sharing actions for this session, or export with file, html, gist, research, or link | Review side effects and permissions |
| /skills | Manage skills for enhanced capabilities | Review side effects and permissions |
| /skills list | Manage skills for enhanced capabilities | Review side effects and permissions |
| /skills info NAME | Manage skills for enhanced capabilities | Review side effects and permissions |
| /skills add [--project] &lt;FILE\|URL\|DIRECTORY&gt; | Manage skills for enhanced capabilities | Review side effects and permissions |
| /skills remove &lt;NAME\|DIRECTORY&gt; | Manage skills for enhanced capabilities | Review side effects and permissions |
| /skills reload | Manage skills for enhanced capabilities | Review side effects and permissions |
| /statusline,/footer | Configure status line items | Check command and session context |
| /subagents,/agents | Configure each subagent's model and settings, or turn it on or off | Check command and session context |
| /tasks | View running subagents and background shell commands, check their status, and open their live transcript or recent output | Check command and session context |
| /terminal-setup | Configure terminal for multiline input support (shift+enter) | Check command and session context |
| /theme [default\|github\|dim\|high-contrast\|colorblind] | Open the color mode picker. /theme &lt;mode&gt; is deprecated; use /settings theme &lt;mode&gt; | Check command and session context |
| /tuikit [colors\|icons\|select\|tabbar] | Not listed in captured 1.0.109 primary-command help | Check command and session context |
| /undo,/rewind | Not listed in captured 1.0.109 primary-command help | Check command and session context |
| /update,/upgrade | Update the CLI to the latest version | Review side effects and permissions |
| /usage | Display session usage metrics and statistics | Check command and session context |
| /user [show\|list\|switch] | Manage signed-in accounts | Review side effects and permissions |
| /version | Display version information and check for updates | Check command and session context |
| /vim | Toggle Vim mode for the input (hjkl/w/b/e/ge/0/^/$/gg/G motions, f/F/t/T/;/, char search, i/a/o insert, r/~/J/x/D/C edit, d/c/y operators, y/p/P yank & put, . repeat, u/ctrl+r undo & redo, counts, esc for normal mode) | Check command and session context |
| /voice [on\|off\|models\|devices] | Manage voice mode (dictation transcription via Foundry Local) | Check command and session context |
| /workflows | Not listed in captured 1.0.109 primary-command help | Check command and session context |
| /fork [NAME],/branch [NAME] | Fork the current session into a new session, optionally with a name, and switch to it; the original keeps running in the background. To fork a different session, /resume it first. Use `/fork worktree` to fork into a new worktree based on the current branch. | Review side effects and permissions |
| /worktree [branch\|task] | Create a new git worktree from your configured base ref and switch into it, leaving your uncommitted changes behind. Use `/new worktree` for an empty session or `/fork worktree` to preserve the current context. The deprecated `/worktree new` command still works for now. | Review side effects and permissions |
| /worktree new [PROMPT] | Create a new git worktree from your configured base ref and switch into it, leaving your uncommitted changes behind. Use `/new worktree` for an empty session or `/fork worktree` to preserve the current context. The deprecated `/worktree new` command still works for now. | Review side effects and permissions |
| /move [branch\|task] | Move your uncommitted changes into a new git worktree and switch into it. Pass a branch name, a task to start, or nothing to auto-name. | Review side effects and permissions |
