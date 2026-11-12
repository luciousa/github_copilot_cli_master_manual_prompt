<a id="f2-setup"></a>
# F2. Setup and lifecycle

**Outcomes:** identify prerequisites, choose a documented installation channel and diagnose startup without assuming that access to one Copilot surface implies CLI access. **Prerequisites:** an eligible GitHub account and the ability to install software under your organization's policies.

GitHub's installation page states that Copilot CLI is available with all Copilot plans, subject to the organization's CLI policy when applicable. It lists an active Copilot subscription, PowerShell 6 or later on Windows, and Node.js 22 or later for npm installation. These are documentation findings as of 2026-11-11; account-specific entitlements were not audited. Windows CLI 1.0.109 ran authenticated synthetic checks. [Installation documentation](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli).

## Choose and maintain an installation

The official installation page describes WinGet for Windows, Homebrew for macOS/Linux, npm across platforms, and an install script for macOS/Linux. Follow the current official instructions for your platform and organization, inspect the publisher and installation method, and record the version, channel and install source for reproducibility. Review updates and release notes before adopting them in a managed environment.

**Homebrew discrepancy:** the installation page specifies a cask while the [CLI repository](https://github.com/github/copilot-cli) shows a formula-style invocation. Their equivalence and platform behavior have not been established here. The cask command below follows the installation page; it was not tested on macOS or Linux. Check current package metadata before use. See [verification ledger V31](../../reference/verification-ledger.md).

Homebrew's [GitHub Copilot CLI cask](https://formulae.brew.sh/cask/copilot-cli) identifies the package as `copilot-cli`. The separate [Homebrew `copilot` formula](https://formulae.brew.sh/formula/copilot) refers to AWS's ECS/Fargate tool, a different product. Check the exact package identity and current metadata; the cask page retrieved during this research was cached, and neither package was installed for this manual.

## Install and verify

Choose one installation channel and follow your organization's software policy. The commands in this section are sourced from [GitHub's installation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli); version 1.0.109 was also installed and removed through npm in an isolated Windows prefix as described below. Platform-specific WinGet and Homebrew operations were not executed in this research environment.

**Windows PowerShell — WinGet:**

```powershell
winget install GitHub.Copilot
```

**macOS or Linux — Homebrew cask:**

```sh
brew install --cask copilot-cli
```

**Windows PowerShell, macOS or Linux — npm:** Node.js 22 or later is required by GitHub's current guide.

```sh
npm install -g @github/copilot
```

To reproduce the version used in the Windows npm fixture instead of tracking the current package, specify `@github/copilot@1.0.109`. Our test used an isolated npm prefix and clean configuration, successfully ran that version's help, then removed the package. It does not establish macOS/Linux installation behavior. [Test evidence](../../research/evidence/copilot-1.0.109-npm-fixture.txt); [npm package removal](https://docs.npmjs.com/uninstalling-packages-and-dependencies/).

Verify the selected executable and version in a new terminal. Both platforms use the same CLI version command; the path check differs:

```powershell
Get-Command copilot | Select-Object -ExpandProperty Source
copilot --version
```

```sh
command -v copilot
copilot --version
```

The expected result is a path to your intended GitHub Copilot CLI installation and its reported version; compare that version with the current [release history](https://github.com/github/copilot-cli/releases). On Windows, `copilot --version` was executed successfully for 1.0.109; the POSIX path check is standard shell syntax and was not executed here. Multiple installations can resolve to a different executable than expected.

Start the CLI in a trusted working directory with `copilot`. GitHub documents `/login` within an interactive session when authentication is needed; do not type that slash command into the operating-system shell. Follow the on-screen authentication flow and organizational policy without exposing tokens in prompts or transcripts. [Installation and authentication](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli).

For npm-managed installations, GitHub documents reinstalling with the npm command above to update; the selected npm package's corresponding removal command is `npm uninstall -g @github/copilot`. Confirm the installation channel and review the target before removal: this affects the global npm package in the active prefix and does not necessarily remove session data, credentials, or an installation from another package manager. [GitHub installation guide](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/install-copilot-cli); [npm uninstall documentation](https://docs.npmjs.com/uninstalling-packages-and-dependencies/).

## Scenario and validation

A Windows team and a Linux CI team want a repeatable environment. Each records its OS, shell, installed CLI version, package channel, authentication method category and applicable policy. Compare the local built-in help with the versioned release notes; do not copy a command verified only on the other OS. Validate installation and login using the official workflow without sharing credentials. Test a harmless task in a trusted disposable workspace before granting broader access.

**Illustrative prompt — not a shell command:**

> Describe the checks you would perform to confirm this repository's expected development environment. Do not install, update, authenticate, change configuration, or execute commands. Identify assumptions and ask before any action.

Expected result: a proposed checklist for review, not proof that an install or authentication works.

## Troubleshooting and safety

- **Command not found:** check the installation's documented location and shell path, then restart the shell if the installer requires it.
- **Authentication or access denied:** distinguish local login issues from a subscription or organization policy restriction. Use [GitHub's authentication troubleshooting](https://docs.github.com/en/copilot/how-tos/copilot-cli/set-up-copilot-cli/troubleshoot-copilot-cli-auth); do not paste secrets into a support transcript.
- **Startup fails before help:** record the exact error with private paths redacted, installation channel and OS. An executable's presence alone does not prove it runs. An earlier extraction attempt encountered an `EPERM` rename error; a later isolated npm install and version check succeeded (V36).
- **Unexpected update or behavior:** compare the actual version and channel to release notes and managed settings. Do not assume the latest release has the same flags as an older installation.

**Common mistake:** treating a web page's current examples as proof of support in every installed version. Verify local help and feature availability before use.
