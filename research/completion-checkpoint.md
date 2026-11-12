# Completion work checkpoint

**Updated:** 2026-11-11. **Status:** full reference remains incomplete; technical QA is ongoing. The user approved completion after the partial draft build. The previously generated files in `releases/` are an earlier partial snapshot and do not contain the later tests described here. Do not overwrite or describe them as a finished verified master reference without completing the required review and publication gates.

## New evidence after the partial draft

- Outside the restricted command environment, GitHub CLI was signed in. An authenticated non-interactive Copilot probe in an empty disposable workspace returned the requested response. See [probe evidence](evidence/copilot-authenticated-probe.txt) and V32.
- Four adapted synthetic prompts (K01, K04, K16, K21) ran on Windows CLI 1.0.109. K01 and K16 produced fixture-specific correct observations; K21 proposed plausible assertions independently checked on a synthetic function; K04 introduced unmarked product assumptions and did not meet its full contract. See [outputs](evidence/copilot-recipe-fixtures.txt) and V33. These are not full end-to-end recipe validations.
- Interactive `/plan` in a temporary Windows session reached a review dialog and saved a private plan; the requested target file was absent afterward. The exit-without-running option displayed a potentially confusing “Plan approved” message; the session was interrupted and exited. See [plan check](evidence/copilot-1.0.109-plan-check.md) and V34. Its exit summary displayed 7.8 AI Credits; actual billing depends on the account.
- Shell-level `copilot init` created instructions in a fresh disposable synthetic Git repository; the interactive `/init` command and existing-file behavior remain untested. See [init check](evidence/copilot-1.0.109-init-fixture.txt) and V35.
- Two isolated MCP fixture-add attempts failed with the same storage I/O error, including a retry with isolated appdata. The cause is unknown. Homebrew's GitHub CLI cask and similarly named AWS formula were distinguished; equivalence of GitHub's two installation forms remains untested.

## Remaining work, in order

1. Finish the version-pinned slash/flag/configuration inventory, including aliases, lifecycle labels, permissions and side effects; reconcile local 1.0.109 help against current CLI-specific sources without treating live documentation as 1.0.109 behavior.
2. Test interactive `/init`, existing-instruction behavior, model selection, permission boundaries, plan approval/alternative modes and session recovery in isolated authenticated fixtures. Record observed outcomes and cost where shown. Do not repeat the completed probes without a reason.
3. Resolve or explicitly quarantine MCP setup, real extension provenance and installation/removal; current fixture failure is not proof of general product behavior. Complete model/plan/OS matrices without inferring missing table markers.
4. Review and substantiate every retained cookbook entry with task-specific evidence and acceptance; do not count the 80 draft candidates as verified. Reduce scope where evidence is unavailable rather than fabricating commands or results.
5. Repeat link, security, editorial, accessibility and artifact validation, preserve the quality-gate approval stops, then regenerate the Markdown, DOCX, HTML, PDF, manifest and ZIP only when the publication decision is made. The existing partial package remains available in `releases/`.

Source of truth for all observations and unresolved conflicts: [verification ledger](../reference/verification-ledger.md) and [technical QA checkpoint](gate-4-technical-qa.md). See [source registry](../reference/source-registry.md) for publishers and verification dates.
