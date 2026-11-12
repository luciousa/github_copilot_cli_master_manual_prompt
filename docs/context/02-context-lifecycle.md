<a id="x2-context"></a>
# X2. Context lifecycle

**Outcomes:** manage limited context, preserve task decisions and recover safely after compaction or session interruption. **Prerequisites:** [F3](../fundamentals/03-sessions.md) and [X1](01-instructions.md).

GitHub describes context as including messages, instructions, tools and tool results, with capacity varying by model. Its [context guide](https://docs.github.com/en/copilot/concepts/prompting-and-context/context-management) documents CLI `/context` and `/compact`, including automatic compaction. Compaction produces a summary and may lose fine-grained details; a long session is therefore not a complete evidence archive. Syntax, thresholds and behavior are version-dependent and **unverified locally—do not execute** until checked against the target CLI.

## Manage a multi-phase task

1. Provide the minimal relevant task, constraints, file locations and acceptance criteria. Avoid large unrelated logs or secret-bearing data.
2. Ask for a short evidence map and direct the assistant to inspect supporting files only as needed. Large tool output may crowd out later context; GitHub documents output-handling controls whose defaults should be checked for the installed version.
3. Before changing phases or resuming after a long interruption, preserve the approved objective, decisions, changed files, tests and results, unresolved issues and next step in an authorized durable checkpoint.
4. After compaction or resumption, have the assistant restate the contract and uncertainties, then compare that summary against the checkpoint, repository state and actual test output. Correct omissions before new work.
5. For unrelated work, consider a fresh session; transfer only the necessary approved context. A fresh session is a context-management choice, not a proven security isolation boundary.

**Scenario:** a Python ingestion service migration spans three sessions. Record which schema decision was approved, what remains unchanged, test failures and the next migration step. On return, review the working tree and tests before trusting a session summary. GitHub documents session resumption, but behavior varies with version and configuration. [Multiple sessions](https://docs.github.com/en/copilot/how-tos/copilot-cli/use-copilot-cli/work-with-multiple-sessions).

**Illustrative prompt — not a shell command:**

> Reconcile this checkpoint with the visible repository state. List decisions, changed files, verified tests, missing evidence and the next safe step. Do not assume omitted information was completed, and do not make changes.

**Expected result:** a reconciliation that a human can verify. If facts are missing or conflict, consult original sources and tests; do not manufacture continuity. Treat saved session data and checkpoints as potentially sensitive and follow retention policy.
