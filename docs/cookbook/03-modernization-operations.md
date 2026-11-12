<a id="k31-k45"></a>
# K31–K45. Modernization and operations

Read the [shared recipe contract](00-recipe-contract.md) for prerequisites, model selection, permissions and sources. Adapt each prompt to the project and validate its result; these workflows have not been tested end to end.

## K31. Plan a framework upgrade

**Goal/setup:** Assess a framework upgrade using the current manifest, target version and compatibility constraints.

**Prompt:** “Analyze the upgrade from [current] to [target]. Cite affected dependencies and project files; propose stages, tests and rollback. Do not install or edit.”

**Result/acceptance:** A maintainer confirms target-version support and approves a staged test plan. **Failure/recovery:** If support or dependency compatibility is unclear, consult versioned vendor evidence before proceeding.

## K32. Evaluate dependency updates and advisories

**Goal/setup:** Review a supplied advisory and lockfile in a trusted checkout; use a redacted advisory when required.

**Prompt:** “Map [advisory] to the dependency tree, identify affected versions and propose minimal remediation with evidence. Do not access registries or update packages.”

**Result/acceptance:** Verify applicability and fixed versions against the authoritative advisory; approve changes and tests separately. **Failure/recovery:** If the affected path is uncertain, record it and ask the dependency owner rather than asserting exposure or safety.

## K33. Migrate a legacy API endpoint

**Goal/setup:** Supply old and proposed endpoint contracts, known consumers and deprecation policy.

**Prompt:** “Plan migration of [endpoint], including consumer compatibility, authentication, staged rollout and contract tests. Cite existing code; do not edit or call the API.”

**Result/acceptance:** Consumers and owners approve the compatibility window and test cases. **Failure/recovery:** If consumers are unknown, inventory them before removal and maintain a documented rollback or forward-recovery path.

## K34. Plan a database migration and verification

**Goal/setup:** Use a non-production schema, safe fixture and database owner's recovery requirements.

**Prompt:** “Plan [migration], preconditions, validation queries in conceptual terms, locking risks and recovery. Do not connect to or modify a database.”

**Result/acceptance:** Owner-reviewed plan is rehearsed with approved test data and verified backups before any deployment decision. **Failure/recovery:** If integrity or recovery cannot be demonstrated, stop and revise; do not improvise production rollback.

## K35. Modernize a test suite in stages

**Goal/setup:** Provide existing test conventions, baseline results and proposed target toolchain.

**Prompt:** “Propose an incremental modernization of [suite] preserving meaningful coverage. Identify dependencies, flaky tests and verification gates. Do not change or run tests.”

**Result/acceptance:** Each authorized stage retains failure-detecting coverage and reports skipped or changed tests. **Failure/recovery:** If baseline failures or removed assertions obscure behavior, isolate the stage and restore coverage before continuing.

## K36. Investigate a failing CI job

**Goal/setup:** Supply redacted job output, workflow definition and a safe reproduction environment.

**Prompt:** “Analyze [CI failure], cite relevant workflow and source files, and propose discriminating checks. Do not access secrets, start jobs or edit files.”

**Result/acceptance:** A cause is supported by logs or approved reproduction; tests confirm the selected remedy. **Failure/recovery:** Record inaccessible logs and avoid repeated external job runs without approval.

## K37. Propose a CI pipeline change

**Goal/setup:** Provide the workflow, runner restrictions and allowed permissions.

**Prompt:** “Plan [pipeline change], including least-privilege permissions, triggers, test strategy and rollback. Do not modify or run workflows.”

**Result/acceptance:** A reviewer verifies triggers, permissions and a safe test strategy before a separate change approval. **Failure/recovery:** Disable or revert only the approved change under the team's procedure if validation reveals unintended triggers.

## K38. Review a Docker build for reproducibility

**Goal/setup:** Supply Dockerfile, build context and allowed dependency sources without secrets.

**Prompt:** “Review this container build for unpinned inputs, secret exposure and reproducibility gaps. Cite lines and propose checks; do not build or pull images.”

**Result/acceptance:** Reviewer verifies source provenance and compares approved builds with documented inputs. **Failure/recovery:** If dependencies are mutable or unavailable, report the limitation and preserve the existing working build.

## K39. Plan an Azure deployment change

**Goal/setup:** Provide approved infrastructure definitions, a non-production target and deployment policy, with no credentials in context.

**Prompt:** “Review [Azure change] for permissions, state, network, rollout and recovery implications. Propose a non-production validation plan; do not connect to Azure or deploy.”

**Result/acceptance:** Cloud owner verifies the plan, predicted scope and rollback using authorized tools and test environment. **Failure/recovery:** If the plan affects unknown resources, stop and obtain an inventory before any apply.

## K40. Plan an AWS deployment change

**Goal/setup:** Supply infrastructure definitions, account boundaries and non-production policy without credentials.

**Prompt:** “Analyze [AWS change] for IAM scope, stateful resources, network and recovery risks. Propose tests and approval points; do not access AWS or modify resources.”

**Result/acceptance:** Cloud owner reviews the precise account, role, resource diff and recovery plan before any separate execution approval. **Failure/recovery:** Halt on unexpected account or resource scope and investigate without applying changes.

## K41. Add observability to a service

**Goal/setup:** Identify the service, approved telemetry platform and data-classification rules.

**Prompt:** “Propose observability for [operation], including useful signals, failure cases and sensitive-data exclusions. Cite existing patterns; do not change code or contact services.”

**Result/acceptance:** Reviewers verify signals, redaction, performance and tests against operational needs. **Failure/recovery:** If logs contain sensitive data, stop emission and follow the incident and retention process.

## K42. Investigate a redacted operational log

**Goal/setup:** Provide a sanitized, time-bounded excerpt and known system context.

**Prompt:** “Analyze these redacted logs for evidence-backed hypotheses and missing information. Do not infer a root cause without corroboration or access external systems.”

**Result/acceptance:** An operator verifies timestamps, correlation and hypotheses against approved evidence. **Failure/recovery:** If redaction removed essential context, request a safer summary from the log owner rather than raw secrets.

## K43. Prepare a release checklist

**Goal/setup:** Provide release criteria, actual change scope and deployment ownership.

**Prompt:** “Build a release checklist for [change] covering tests, dependencies, approvals, monitoring and recovery. Mark all unverified items as pending; do not publish or deploy.”

**Result/acceptance:** Release owner checks each item against evidence and explicitly decides outstanding risks. **Failure/recovery:** A missing approval or failed gate pauses release; do not mark it complete by inference.

## K44. Update change-focused documentation

**Goal/setup:** Provide approved diff, affected documentation and verified behavior.

**Prompt:** “Identify documentation changes required by this diff; cite code and tests, and flag claims needing confirmation. Propose edits only.”

**Result/acceptance:** After edit approval, a reviewer checks examples, links and behavior against the actual implementation. **Failure/recovery:** Remove or label claims that lack evidence; do not invent command output.

## K45. Audit an operational runbook

**Goal/setup:** Provide a sanitized runbook, owner and current recovery objectives.

**Prompt:** “Review [runbook] for stale assumptions, missing decision points, permissions and rollback. Cite the source of each concern; do not execute steps.”

**Result/acceptance:** Operator verifies procedures in an approved exercise and signs off on unresolved gaps. **Failure/recovery:** Mark untested procedures as unverified and route urgent issues to the runbook owner.
