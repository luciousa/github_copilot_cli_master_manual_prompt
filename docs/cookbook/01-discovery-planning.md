<a id="k01-k15"></a>
# K01–K15. Discovery and planning

Read the [shared recipe contract](00-recipe-contract.md) for prerequisites, model selection, permissions and sources. These prompts are starting points; the evidence ledger identifies the few synthetic checks and their limits.

## K01. Map an unfamiliar monorepo

**Goal/setup:** Identify major packages and entry points; provide a trusted monorepo checkout and its known build manifests.

**Prompt:** “Map the services, packages and entry points in this repository. Cite files and distinguish confirmed relationships from guesses. Do not edit or execute state-changing commands.”

**Result/acceptance:** A map whose cited paths and representative dependency edges a human checks against manifests. **Failure/recovery:** If a package is missed, narrow the search to its manifest and update the map; record inaccessible directories.

## K02. Identify service ownership

**Goal/setup:** Find owners of an API and its dependencies; supply the service name and approved ownership sources.

**Prompt:** “Locate ownership information for [service] and its dependencies. Cite the relevant files, distinguish maintainers from inferred owners, and list gaps. Do not contact anyone.”

**Result/acceptance:** Source-backed ownership candidates and unresolved gaps checked against the team's current directory. **Failure/recovery:** If ownership files are stale or absent, flag the uncertainty and ask the project owner rather than inventing contacts.

## K03. Trace a request across services

**Goal/setup:** Trace a safe example request from frontend to persistence using a checkout with no production payloads.

**Prompt:** “Trace [operation] from its UI entry point through API handlers and persistence. Cite each hop and mark dynamic or uncertain links. Do not run the application.”

**Result/acceptance:** A path-by-path trace verified against routes and call sites. **Failure/recovery:** If a hop cannot be established statically, propose a safe test with approval and mark the trace incomplete.

## K04. Turn a feature brief into acceptance criteria

**Goal/setup:** Make a product brief testable; provide the approved brief and known constraints.

**Prompt:** “Convert [brief] into observable acceptance criteria, including authorization, failure cases and explicit non-goals. Separate assumptions and questions. Do not implement.”

**Result/acceptance:** Criteria reviewed by a product owner and mapped to testable outcomes. **Failure/recovery:** If business rules conflict or are missing, pause for a decision rather than selecting a rule.

**Synthetic check, 2026-11-11:** one adapted authenticated run proposed concrete defaults that the brief did not specify and did not clearly label them as assumptions. Treat its output as a draft for human correction, not a passed acceptance test. [Evidence and limitations](../../reference/verification-ledger.md) V33.

## K05. Identify missing requirements

**Goal/setup:** Expose gaps in an existing contract; supply the contract and relevant stakeholders' documented decisions.

**Prompt:** “Review [contract] for missing inputs, boundary cases, compatibility and operational decisions. Ask prioritized questions and cite existing evidence. Do not propose edits.”

**Result/acceptance:** A prioritized question list with verified evidence and owners. **Failure/recovery:** If answers cannot be found, record them as blockers or assumptions requiring approval.

## K06. Compare implementation approaches

**Goal/setup:** Compare feasible ways to implement a bounded feature; provide requirements, architecture constraints and evidence.

**Prompt:** “Compare at least two approaches to [feature], including tradeoffs, dependencies, migration risk and tests. Cite repository evidence; do not change files.”

**Result/acceptance:** Alternatives evaluated against explicit criteria with a human decision and open risks. **Failure/recovery:** If options rely on invented capabilities, check source and remove unsupported claims.

## K07. Build and review a CLI plan

**Goal/setup:** Produce an implementation plan for a scoped feature; provide approved criteria and confirm the active mode will not auto-continue.

**Prompt:** “Investigate [feature], propose a staged plan with file evidence, tests and rollback, and wait for my review before edits.”

**Result/acceptance:** Reviewed steps, explicit unknowns and a recorded approval decision. **Failure/recovery:** If the session starts editing, stop it and inspect changes and effective mode. See [C3](../commands/03-plan-to-acceptance.md) for the documented autopilot exception.

## K08. Review repository initialization

**Goal/setup:** Evaluate generated guidance for a disposable repository with existing instructions and a known baseline.

**Prompt:** “Before initialization, inventory existing guidance and propose what project-specific facts need verification. Do not modify files.”

**Result/acceptance:** Inspect the actual guidance diff, test referenced commands independently and reject unsupported claims. **Failure/recovery:** If unrelated content changes, preserve the baseline and restore only the affected content. Interactive `/init` was observed once in a disposable Windows 1.0.109 repository; behavior for an existing instructions file remains untested. [CLI reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## K09. Specify a greenfield .NET API

**Goal/setup:** Define an API feature before implementation; provide runtime constraints, consumer needs and authorization rules.

**Prompt:** “Draft a .NET API contract for [feature]: endpoints, inputs, errors, authorization and testable outcomes. Identify decisions that require an owner. Do not create files.”

**Result/acceptance:** A reviewed contract covering valid, invalid and unauthorized requests. **Failure/recovery:** Resolve missing semantics before choosing a framework pattern or coding.

## K10. Specify a React feature with an API contract

**Goal/setup:** Align UI behavior with an existing or proposed API; provide the contract and accessibility requirements.

**Prompt:** “Specify [React feature] against the provided API, including loading, empty, error and keyboard states. Cite existing components; do not implement.”

**Result/acceptance:** UI states and contract assumptions mapped to agreed tests and accessibility checks. **Failure/recovery:** If the API lacks necessary fields, request a contract decision rather than fabricating a response.

## K11. Specify a Vue/Nuxt feature

**Goal/setup:** Define a feature across server and client boundaries; provide the Nuxt version and deployment constraints.

**Prompt:** “Plan [feature] in this Nuxt project, identifying server/client boundaries, data loading, error states and tests with file evidence. Do not edit.”

**Result/acceptance:** A version-appropriate plan with data and rendering assumptions confirmed by maintainers. **Failure/recovery:** If routing or framework conventions are unclear, inspect the project and record uncertainty.

## K12. Define a Python service boundary

**Goal/setup:** Specify input, output and failure behavior of a new Python service using an approved data classification.

**Prompt:** “Describe the boundary for [service], including input validation, failure and retry expectations, observability and tests. State assumptions; do not create code.”

**Result/acceptance:** An agreed interface and failure contract with representative acceptance cases. **Failure/recovery:** Escalate unresolved delivery or retry semantics before implementation.

## K13. Plan a database schema change

**Goal/setup:** Assess an additive or breaking schema change using a non-production schema and migration policy.

**Prompt:** “Plan [schema change], identifying compatibility, migration ordering, validation, rollback limits and data-safety risks. Do not access or modify a database.”

**Result/acceptance:** A database-owner-reviewed migration and rollback strategy with safe test data and verification criteria. **Failure/recovery:** If rollback may lose data, stop for an explicit recovery decision; never assume a reversible migration.

## K14. Plan a cross-platform developer workflow

**Goal/setup:** Compare a development task across Windows PowerShell and POSIX environments; supply supported shell and tool versions.

**Prompt:** “Identify platform-sensitive steps in [workflow] and propose separately testable PowerShell and POSIX approaches. Do not run or install anything.”

**Result/acceptance:** Platform owners validate paths, quoting and tool availability on both environments before commands are published. **Failure/recovery:** Mark untested OS variants unavailable instead of copying syntax across shells.

## K15. Define a change budget and stop conditions

**Goal/setup:** Bound a risky refactor; provide allowed files, review checkpoints and time or usage constraints.

**Prompt:** “Propose the smallest staged change for [task], list allowed and excluded areas, review checkpoints, test gates and conditions requiring a new decision. Do not edit.”

**Result/acceptance:** Human-approved scope and explicit triggers for stopping. **Failure/recovery:** If the work exceeds the budget, pause, inspect the actual state and obtain a revised scope.
