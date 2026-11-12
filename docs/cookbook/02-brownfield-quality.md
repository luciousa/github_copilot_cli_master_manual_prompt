<a id="k16-k30"></a>
# K16–K30. Brownfield, debugging and quality

Read the [shared recipe contract](00-recipe-contract.md) for prerequisites, model selection, permissions and sources. Adapt each prompt to the project and check its acceptance criteria; the evidence ledger records the limited synthetic checks.

## K16. Reproduce a regression

**Goal/setup:** Establish a failing baseline from a redacted issue and safe fixture.

**Prompt:** “Investigate [regression]. Identify likely entry points and a minimal reproducible test, citing evidence. Do not modify files or run commands.”

**Result/acceptance:** After approving a safe test, capture actual reproduction and distinguish pre-existing failures. **Failure/recovery:** If unreproducible, record environment and missing inputs; do not claim a fix.

## K17. Investigate an intermittent test

**Goal/setup:** Examine a flaky test with prior redacted failures and relevant test setup.

**Prompt:** “Analyze [test] for plausible nondeterminism, rank hypotheses by evidence and propose ways to distinguish them. Do not run or edit tests.”

**Result/acceptance:** An approved experiment captures failure frequency and environment without claiming determinism from one pass. **Failure/recovery:** If timing or infrastructure differs, document the uncertainty and revise the experiment.

## K18. Trace a performance bottleneck

**Goal/setup:** Use representative non-sensitive workload data and an agreed measurement baseline.

**Prompt:** “Identify likely bottlenecks in [path], the evidence available, and a controlled measurement plan. Separate hypotheses from measured facts; do not benchmark yet.”

**Result/acceptance:** Approved profiling shows repeatable measurements and no functional regression. **Failure/recovery:** If variance masks the effect, report it and improve the experiment rather than claiming a speedup.

## K19. Diagnose a Node dependency conflict

**Goal/setup:** Provide package manifests, lockfile and a redacted error from a safe checkout.

**Prompt:** “Trace the dependency conflict in [error] through manifests and lockfile. Propose minimal options and compatibility risks. Do not install or change dependencies.”

**Result/acceptance:** A maintainer verifies the dependency chain, chooses a version-compatible remedy and approves installation and tests separately. **Failure/recovery:** Restore only approved lockfile changes if resolution fails; record registry/network constraints.

## K20. Isolate a C# nullability defect

**Goal/setup:** Supply the affected C# path, compiler configuration and a safe failing case.

**Prompt:** “Trace how null reaches [location], cite source and identify a regression test. Do not edit or run the build.”

**Result/acceptance:** A confirmed path and test that fails before and passes after an approved fix. **Failure/recovery:** If null cannot be reproduced, distinguish compiler warnings from runtime evidence and seek more data.

## K21. Add a focused regression test

**Goal/setup:** Provide a confirmed defect and the existing test suite's conventions.

**Prompt:** “Propose the smallest test that fails for [defect] and passes when its intended behavior is restored. Explain fixtures and assertions; do not edit.”

**Result/acceptance:** With approval, demonstrate failure against the defect and success after correction without unrelated failures. **Failure/recovery:** If the test passes before the fix, revise it to detect the actual failure.

## K22. Assess API contract-test gaps

**Goal/setup:** Provide an API contract and current tests, including authorized and unauthorized cases.

**Prompt:** “Compare [API contract] with existing contract tests. Cite missing cases, rank their risk and suggest assertions. Do not change tests.”

**Result/acceptance:** A reviewed coverage map tied to endpoints and observable behavior. **Failure/recovery:** If the contract is stale, resolve the source of truth before generating tests.

## K23. Review a diff for correctness

**Goal/setup:** Provide the exact diff, baseline and task acceptance criteria.

**Prompt:** “Review this diff for actionable correctness defects and regressions. Cite changed lines, explain a triggering case and distinguish uncertainties. Do not modify files.”

**Result/acceptance:** Each finding is reproduced or supported by source; a clean review does not replace tests. **Failure/recovery:** If context is missing, inspect surrounding code and report review limitations.

## K24. Audit authorization paths

**Goal/setup:** Use a safe checkout and an approved authorization matrix; avoid real credentials.

**Prompt:** “Trace authorization for [operation], citing enforcement points and tests. Identify mismatches with the supplied matrix. Do not access production or change policy.”

**Result/acceptance:** Security owner verifies each path, including denied and cross-tenant cases, with appropriate tests. **Failure/recovery:** Treat unknown paths as unverified and escalate; do not assert security based only on agent output.

## K25. Review migration rollback safety

**Goal/setup:** Provide migration code, non-production schema and documented recovery objectives.

**Prompt:** “Review [migration] for irreversible steps, compatibility windows and rollback data loss. Cite code and propose safe validation; do not run it.”

**Result/acceptance:** Database owner validates backup and recovery assumptions in a safe environment. **Failure/recovery:** If rollback cannot be demonstrated, record a forward-recovery plan and require a decision before deployment.

## K26. Refactor a legacy module safely

**Goal/setup:** Identify the module, observable behavior and characterization tests.

**Prompt:** “Propose a staged refactor of [module] preserving behavior and public interfaces. Identify missing characterization tests and stop conditions. Do not edit.”

**Result/acceptance:** After approved implementation, compare behavior and run relevant tests against baseline. **Failure/recovery:** Stop on unexplained behavior change; preserve the diff and isolate the smallest failing increment.

## K27. Extract duplicated service logic

**Goal/setup:** Provide two candidate implementations and their consumers.

**Prompt:** “Compare [implementations], identify semantic differences and propose whether a shared service is appropriate. Cite call sites and tests. Do not edit.”

**Result/acceptance:** Consumers' distinct behavior is covered by tests and the owner accepts any interface change. **Failure/recovery:** If differences are material, retain separate logic or revise the design rather than forcing abstraction.

## K28. Characterize undocumented behavior

**Goal/setup:** Use a safe fixture and a legacy entry point without a reliable specification.

**Prompt:** “Identify observable behavior of [entry point] from code and existing tests; list unknowns and propose characterization tests. Do not run or change anything.”

**Result/acceptance:** Approved tests capture existing behavior, including error cases, without silently endorsing defects as requirements. **Failure/recovery:** Escalate conflicting observations to a domain owner.

## K29. Improve service-boundary error handling

**Goal/setup:** Provide both sides of a service contract and redacted failure examples.

**Prompt:** “Trace errors across [boundary]. Propose consistent responses, retry behavior and logging that avoids sensitive data; cite callers and tests. Do not edit.”

**Result/acceptance:** Reviewed contract and tests cover timeouts, failures and sensitive-data redaction. **Failure/recovery:** If a proposed retry could duplicate writes, stop and resolve idempotency first.

## K30. Validate against acceptance criteria

**Goal/setup:** Supply the approved criteria, final diff and actual test outputs.

**Prompt:** “Map each criterion for [change] to source and test evidence. Mark absent or conflicting evidence and do not infer that tests passed. Do not modify files.”

**Result/acceptance:** A human checks each cited result, unresolved risk and omitted test before acceptance. **Failure/recovery:** For any unsupported criterion, return to implementation or obtain an explicit decision; never mark it complete by inference.
