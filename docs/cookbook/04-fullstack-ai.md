<a id="k46-k60"></a>
# K46–K60. Full-stack and AI systems

Read the [shared recipe contract](00-recipe-contract.md) for prerequisites, model selection, evidence and review. Adapt each prompt and validate the resulting plan; these workflows have not been tested end to end.

## K46. Implement a .NET API feature

**Goal/setup:** Add a bounded API feature using an approved contract, safe fixtures and existing C# conventions.

**Prompt:** “Plan [API feature] against the supplied contract. Cite handlers, validation, authorization and tests; identify compatibility risks. Do not edit.”

**Result/acceptance:** After approval, review the diff and test valid, invalid and unauthorized requests. **Failure/recovery:** Stop on contract mismatch; preserve existing changes and revise the plan.

## K47. Connect a React interface to an endpoint

**Goal/setup:** Supply the verified endpoint contract and existing UI conventions.

**Prompt:** “Plan [React interaction] using [endpoint], including loading, empty, failure and accessibility states. Cite existing code; do not edit or call the service.”

**Result/acceptance:** Approved implementation passes UI and contract tests using safe fixtures. **Failure/recovery:** If the actual API response differs, resolve the contract instead of hiding the mismatch.

## K48. Implement a Nuxt server/client feature

**Goal/setup:** Provide the project's Nuxt version, target route, data contract and safe test environment.

**Prompt:** “Plan [Nuxt feature] with explicit server/client responsibilities, rendering states and tests. Cite project patterns; do not edit or access external services.”

**Result/acceptance:** After approval, validate server/client behavior, error handling and relevant tests. **Failure/recovery:** If execution context or hydration differs from assumptions, stop and verify the framework-specific behavior.

## K49. Add a bounded Node worker

**Goal/setup:** Define input, output, retry and idempotency expectations for a non-production worker.

**Prompt:** “Plan [worker] with bounded retries, idempotency, observability and failure tests. Identify existing queues and code; do not install, run or edit.”

**Result/acceptance:** Owner approves failure semantics; tests demonstrate retry limits and duplicate handling. **Failure/recovery:** If processing could duplicate writes, stop until idempotency and recovery are defined.

## K50. Add a Python data-processing feature

**Goal/setup:** Supply representative non-sensitive input, expected output and resource constraints.

**Prompt:** “Plan [processing feature], validation, error reporting and edge-case tests. Cite existing Python modules; do not process production data or edit.”

**Result/acceptance:** Approved implementation matches fixtures and handles invalid input within resource limits. **Failure/recovery:** Quarantine unexpected output and inspect the smallest failing fixture without exposing data.

## K51. Coordinate a frontend/API contract

**Goal/setup:** Provide API and frontend repositories or paths, owners and current contract.

**Prompt:** “Compare the proposed [contract change] with frontend and API consumers. List compatibility risks, staged changes and contract tests; do not edit either service.”

**Result/acceptance:** Both owners approve the versioning and rollout plan; contract tests cover both sides. **Failure/recovery:** If deployment ordering is unsafe, revise the compatibility window before changes.

## K52. Plan an event-driven multi-service change

**Goal/setup:** Supply event schema, consumers, delivery assumptions and non-production fixtures.

**Prompt:** “Trace [event] across producer and consumers; propose schema evolution, idempotency and failure tests. Do not publish messages or modify services.”

**Result/acceptance:** Service owners confirm version compatibility, duplicate handling and a safe rollout. **Failure/recovery:** If a consumer is unidentified or replay is unsafe, pause and inventory dependencies.

## K53. Add a SQL query with performance checks

**Goal/setup:** Provide non-production schema, representative safe data and access-control requirements.

**Prompt:** “Propose a query approach for [requirement], including tenant filtering, edge cases and an approved performance-test plan. Do not connect to a database.”

**Result/acceptance:** Database owner verifies correctness and isolation with approved fixtures and compares measured plans under representative conditions. **Failure/recovery:** Stop on incorrect access or unacceptable measurement; do not run speculative production queries.

## K54. Design a containerized multi-service development flow

**Goal/setup:** Provide service definitions, local dependencies, supported OSs and safe configuration placeholders.

**Prompt:** “Plan a local container workflow for [services], identifying startup dependencies, health checks, secrets handling and platform differences. Do not build or start containers.”

**Result/acceptance:** Approved workflow starts and stops in isolated test environments on supported platforms without embedding secrets. **Failure/recovery:** Stop unexpected containers and preserve diagnostic output using the team's approved process.

## K55. Design a feature-flag rollout

**Goal/setup:** Provide flag ownership, default behavior, target population and rollback policy.

**Prompt:** “Plan a feature flag for [change], including default-off behavior if required, authorization, monitoring, rollback and removal criteria. Do not alter flag services.”

**Result/acceptance:** Owner validates both flag states, failure behavior and a reversible rollout in a test environment. **Failure/recovery:** If monitoring or disablement fails, stop rollout and follow the approved incident plan.

## K56. Specify a RAG ingestion workflow

**Goal/setup:** Provide an approved document corpus, classification, indexing requirements and retention policy.

**Prompt:** “Plan ingestion for [corpus], covering source provenance, access boundaries, chunking assumptions, updates, deletion and tests. Do not read unapproved documents or connect to a vector store.”

**Result/acceptance:** Data owner approves ingestion and deletion semantics; test fixtures show updates and access restrictions. **Failure/recovery:** Stop ingestion on unapproved content or failed deletion and contain affected data using policy.

## K57. Evaluate retrieval quality

**Goal/setup:** Provide a fixed, non-sensitive evaluation set with relevance judgments and a frozen index configuration.

**Prompt:** “Design a repeatable retrieval evaluation for this dataset, including baseline, relevant-document judgments, failure categories and measurement limitations. Do not call external models.”

**Result/acceptance:** Reviewed evaluation reports dataset, configuration, measured results and missed cases; compare like-for-like. **Failure/recovery:** If labels or corpus versions drift, invalidate the comparison and rebaseline.

## K58. Add evidence checks to RAG answers

**Goal/setup:** Provide safe retrieved documents, citation requirements and an answer test set.

**Prompt:** “Propose checks that connect answer claims to supplied passages and identify unsupported claims. Include adversarial and missing-evidence tests; do not contact external services.”

**Result/acceptance:** Reviewers verify citations actually support claims and unsupported answers are handled as specified. **Failure/recovery:** If a citation is misleading or absent, reject or qualify the answer and investigate retrieval.

## K59. Design an agent tool boundary

**Goal/setup:** Define the agent's task, approved tools, data classification and external-action policy.

**Prompt:** “Map [agent task] to minimum tool capabilities, sensitive inputs, approval points and failure handling. Distinguish enforced controls from prompt instructions. Do not invoke tools.”

**Result/acceptance:** Security owner validates tool permissions and tests denied as well as allowed actions in isolation. **Failure/recovery:** If a tool has broader access than required, disable it or narrow the credential before use.

## K60. Test an AI workflow against prompt injection

**Goal/setup:** Use an approved isolated test environment and synthetic adversarial documents without real credentials.

**Prompt:** “Design tests for untrusted document text that attempts to change [workflow's] authorized task. Define expected tool denials, evidence and escalation; do not execute the text.”

**Result/acceptance:** Authorized tests verify observed actions against the policy and document gaps; a passed set does not prove immunity. **Failure/recovery:** Stop on unexpected external access, preserve safe evidence and follow the incident process. See [S2](../security/02-threats-response.md).
