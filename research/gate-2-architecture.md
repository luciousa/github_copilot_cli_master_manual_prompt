# Gate 2: proposed architecture

**Status:** approved by the user's “go on”; first draft batch authorized. **Baseline:** 2026-11-11, [feature inventory](../reference/feature-inventory.md), [source registry](../reference/source-registry.md), and [verification ledger](../reference/verification-ledger.md). This is a design and candidate inventory, not a finished manual or evidence that proposed recipes work. Stable IDs below are planning identifiers; final links will use explicit anchors and be validated.

## Audience, progression, and dependencies

The audience is experienced software developers who already know basic Copilot and their development stacks. The manual teaches supervised CLI workflows, not language, framework, Git, or general AI fundamentals. The main path is **F → C → M → X → A → E → S → K**, with security boundaries introduced in F and revisited throughout rather than deferred until S. Reference appendices are available from every stage.

- **F Fundamentals** establishes environment, trust, and sessions. **C Commands** depends on F and teaches the plan/approval loop.
- **M Models** and **X Context** depend on F/C and can be read in either order. Model guidance separates verified facts from dated editorial judgment.
- **A Agents** depends on C/X; **E Extensions** depends on X and builds on A. **S Security** builds on all earlier sections and is a prerequisite to using powerful examples in K.
- **K Cookbook** combines earlier material; each recipe links to only its relevant prerequisites, references and evidence. Appendices provide lookup paths independent of reading order.

## Hierarchical table of contents

### F. Fundamentals (`docs/fundamentals/`)

- **F1 — Orientation and operating model:** CLI scope and supported surfaces; supervised task lifecycle; availability and feature labels; quick navigation.
- **F2 — Setup and lifecycle:** prerequisites by OS and plan; installation and updates; authentication; organization policy; terminal differences; troubleshooting and environment verification.
- **F3 — Sessions and configuration:** interactive versus non-interactive operation; configuration scope; sessions, continuity and recovery; diagnostics and observability; tool permissions and trust boundaries.

### C. Commands and planning (`docs/commands/`)

- **C1 — Command literacy:** shell commands, CLI subcommands and flags, interactive slash commands, arguments, discovery and version-specific help.
- **C2 — Repository initialization:** `/init`, intended output and side effects, review of generated instructions, existing-file behavior, version/OS limitations and validation.
- **C3 — Plan to accepted change:** `/plan`, requirements clarification, plan inspection, approval, implementation, tests, review and acceptance; explicit comparison with any verified autonomous transition.
- **C4 — Interactive and automation reference:** verified command families, configuration and session operations; examples linked to the exhaustive catalogs in R1–R2.

### M. Models and evaluation (`docs/models/`)

- **M1 — Selection and availability:** model controls, plan and organization restrictions, switching and fallback, context and latency as published, quotas and pricing with dated sources.
- **M2 — Task-based decisions:** planning, coding, research, debugging, architecture, tests, security and documentation; evidence versus judgment; dated matrix and escalation patterns.
- **M3 — Repeatable evaluation:** representative tasks, controlled conditions, acceptance criteria, quality and cost recording, limitations and responsible comparison.

### X. Context and prompting (`docs/context/`)

- **X1 — Instructions and discovery:** repository and user conventions, `AGENTS.md`, `copilot-instructions.md` and other verified files; matching, merging, inheritance, conflicts and inspection.
- **X2 — Context lifecycle:** repository discovery, context budgeting, session continuity, isolation, compaction and recovery where supported; sensitive data boundaries.
- **X3 — Task contracts:** specifications, acceptance criteria, constraints, prompt patterns, evidence requests, checkpoints, drift prevention and reusable templates.

### A. Agents and supervised workflows (`docs/agents/`)

- **A1 — Supervised autonomy:** decomposition, approvals, risk tiers, planning, checkpoints, observability, intervention and recovery.
- **A2 — Custom agents and delegation:** supported agent definitions, tool restrictions, context and instruction inheritance, handoffs, delegation and parallelism only where verified.
- **A3 — End-to-end delivery:** feature request through discovery, specification, plan, controlled implementation, testing, review and final acceptance; multi-service and long-running variants.

### E. Extensions (`docs/extensions/`)

- **E1 — Mechanism selection:** instructions, skills, agents, hooks, MCP, connectors, plugins, marketplaces and other verified mechanisms; scopes and lifecycle comparison.
- **E2 — Discovery and maintenance:** provenance and trust, setup, verification, upgrades, removal, failure recovery and interoperability; native versus third-party and preview labels.
- **E3 — Curated toolkit:** evidence-backed candidates for full-stack work, with benefits, permissions, maintenance and exact verified installation/removal linked to R4. No candidate is included merely for popularity.

### S. Security and governance (`docs/security/`)

- **S1 — Permissions and isolation:** approvals, least privilege, tools, filesystem and network access, sandbox capabilities and limits, OS differences and external safeguards.
- **S2 — Threats and response:** prompt injection, secrets, untrusted repositories and MCP responses, supply chain, incident containment, recovery and audit evidence.
- **S3 — Enterprise operating policy:** data handling, privacy, organization policy, compliance considerations, risk-tiered autonomy, review and adaptable policy templates. Cite current authoritative policy; do not imply compliance certification.

### K. Cookbook (`docs/cookbook/`)

- **K1 — Discovery, planning and greenfield:** K01–K15.
- **K2 — Brownfield, debugging and quality:** K16–K30.
- **K3 — Modernization and operations:** K31–K45.
- **K4 — Full-stack and AI systems:** K46–K60.
- **K5 — Context, governance and recovery:** K61–K80.
- Every recipe uses the agreed contract: goal; prerequisites/version; context setup; model rationale; verified commands and separately labeled prompts; approval boundaries; expected result; tests/acceptance; failure/recovery; sources. PowerShell and POSIX variants appear when materially different. Candidates may be merged, replaced or omitted if unsupported or redundant.

### R. Reference appendices (`docs/appendices/` and `reference/`)

- **R1 — Slash command catalog:** exhaustive verified CLI commands, aliases, arguments, behavior, prerequisites, side effects, versions and citations; interactive-only context explicit.
- **R2 — CLI and configuration reference:** subcommands, flags, configuration files and scopes, environment settings, defaults and diagnostics.
- **R3 — Compatibility and model matrices:** OS, plan, policy, version and lifecycle status; dated model availability, costs where published and evidence limitations.
- **R4 — Extension and integration catalog:** vetted marketplaces, plugins, skills, MCP servers and agents; provenance, scope, exact verified install, verification, upgrade and uninstall; unsupported/unverified quarantine.
- **R5 — Security checklist and policies:** risk tiers, review checklist, trust boundaries, privacy, incident procedure and policy templates.
- **R6 — Prompt and configuration library:** copy-ready prompts, instruction, agent, skill and configuration examples; executable versus conceptual labeling and trust boundaries.
- **R7 — Troubleshooting and FAQ:** symptoms, diagnosis, platform differences, recovery, anti-patterns and decision trees.
- **R8 — Glossary and alphabetical index:** terms and stable cross-references.
- **R9 — Evidence and maintenance:** source registry, verification ledger, release changelog, known conflicts, verification procedure and update cadence.

Each major chapter will have learning outcomes, prerequisites, concepts, use cases, supported procedures, a realistic scenario, copy-ready examples, expected results, limitations, mistakes, validation, troubleshooting, security notes and nearby citations. Shared topics link to a canonical explanation rather than duplicate it.

## Candidate recipe inventory

These 80 candidates are intentionally distinct by goal and acceptance criteria, not verified claims or a promise to retain a numerical quota. Every candidate must pass the recipe contract and relevance review before publication.

| IDs | Proposed distinct goals |
|---|---|
| K01–K05 | K01 map an unfamiliar monorepo; K02 identify service ownership; K03 trace a request across services; K04 turn a feature brief into acceptance criteria; K05 identify missing requirements. |
| K06–K10 | K06 compare implementation approaches; K07 build and review a CLI plan; K08 initialize repository guidance and review proposed changes; K09 specify a greenfield .NET API; K10 specify a React feature with API contract. |
| K11–K15 | K11 specify a Vue/Nuxt feature; K12 design a Python service boundary; K13 plan a database schema change; K14 plan a cross-platform developer workflow; K15 define a change budget and stop conditions. |
| K16–K20 | K16 reproduce a reported regression; K17 investigate an intermittent test; K18 trace a performance bottleneck; K19 diagnose a Node dependency conflict; K20 isolate a C# nullability defect. |
| K21–K25 | K21 add focused regression tests; K22 assess missing API contract tests; K23 review an existing diff for correctness; K24 audit authorization paths; K25 inspect data migration rollback safety. |
| K26–K30 | K26 refactor a legacy module with behavior preserved; K27 extract a shared service from duplication; K28 characterize undocumented behavior before edits; K29 improve error handling across a service boundary; K30 validate a change against acceptance criteria. |
| K31–K35 | K31 plan a framework upgrade; K32 evaluate dependency updates and advisories; K33 migrate a legacy API endpoint; K34 introduce a database migration with verification; K35 modernize a test suite in stages. |
| K36–K40 | K36 investigate a failing CI job; K37 propose a CI pipeline change; K38 review a Docker build for reproducibility; K39 plan an Azure deployment change; K40 plan an AWS deployment change. |
| K41–K45 | K41 add observability to a service; K42 investigate a production-like log excerpt safely; K43 prepare a release checklist; K44 generate a change-focused documentation update; K45 audit and revise an operational runbook. |
| K46–K50 | K46 implement a .NET API feature; K47 connect a React interface to an existing endpoint; K48 implement a Nuxt server/client feature; K49 add a Node worker with bounded failure handling; K50 add a Python data-processing feature. |
| K51–K55 | K51 coordinate an API and frontend contract; K52 plan an event-driven multi-service change; K53 add a SQL query with performance checks; K54 containerize a multi-service development flow; K55 design a safe feature flag rollout. |
| K56–K60 | K56 specify a RAG ingestion workflow; K57 evaluate retrieval quality with a fixed dataset; K58 add citations and evidence checks to a RAG response; K59 design an agent tool boundary; K60 test a multi-step AI workflow against prompt injection. |
| K61–K65 | K61 create a scoped repository instruction; K62 audit conflicting instructions; K63 write a task contract; K64 carry a session across a context limit; K65 resume work from an evidence-backed checkpoint. |
| K66–K70 | K66 evaluate a candidate skill's provenance; K67 define a narrowly scoped custom agent; K68 review MCP server access; K69 test extension removal and cleanup; K70 delegate independent review only where supported. |
| K71–K75 | K71 recover from an incorrect edit; K72 recover from failing tests after a change; K73 stop a repetitive agent loop; K74 reject an unsafe proposed command; K75 recover after interrupted execution. |
| K76–K80 | K76 quarantine an injected instruction; K77 rotate a suspected exposed secret using an approved external process; K78 compare model outcomes on a fixed task; K79 document a risk-tiered approval decision; K80 conduct a final evidence-based acceptance review. |

## Requirements-to-coverage matrix

| Requirement | Primary coverage | Cross-reference / acceptance evidence |
|---|---|---|
| Positioning, setup, authentication, platform, configuration, diagnostics | F1–F3 | R2–R3; OS/plan caveats and verified procedures |
| Interactive operation, every verified slash command, `/init`, `/plan`, approval loop | C1–C4 | R1–R2; V05–V06; complete command-to-evidence mapping |
| Models, controls, quotas, costs, switching and evaluation | M1–M3 | R3, K78; dated claims and separation of evaluation from judgment |
| Marketplaces, plugins, skills, MCP, agents and toolkit | E1–E3, A2 | R4, K66–K70; trust, lifecycle, provenance and verified install/removal |
| Context, instruction conventions, scope, precedence, prompts and continuity | X1–X3 | C2, R6, K61–K65; CLI-specific evidence and unresolved conflicts |
| Supervised agent workflows, delegation, checkpoints, end-to-end delivery | A1–A3 | C3, K04–K15, K70, K80; support and approvals explicit |
| Security, privacy, governance, audit and incident response | S1–S3 | R5, K71–K77, K79; built-in versus external controls identified |
| Cookbook coverage, distinctness and recovery | K1–K5 | K01–K80; each retained recipe meets the full recipe contract |
| Do/don't, anti-patterns, troubleshooting, FAQs, glossary and optimization | F–S contextual guidance; R7–R8 | Cross-linked symptom, decision tree and glossary entries |
| Exhaustive appendices and stable navigation | R1–R9 | Command/model/extension matrices, source ledger, index, changelog and link audit |
| Chapter standards, realistic full-stack examples and citations | F1–S3 and K | Per-chapter editorial checklist; PowerShell/POSIX where materially different |
| Publication package, canonical Markdown, navigable source, exports and manifest | Publication plan below | Build and validation logs; actual delivered artifacts only |
| Source, version and conflict policy; quality gates | R9 and all substantive claims | S01–S18 plus new verified sources; technical and editorial QA before release |

## Publication and implementation plan

1. Keep modular Markdown canonical: root `README.md`, grouped chapters under `docs/`, tested or explicitly conceptual artifacts under `examples/`, structured references under `reference/`, and gate checkpoints under `research/`. Maintain `CHANGELOG.md` as changes are approved. Preserve existing files and update the source registry and verification ledger alongside drafts.
2. Assign stable F/C/M/X/A/E/S/K/R identifiers and explicit anchor IDs; use relative links in source. Maintain one canonical entry per command, model or integration and link to it from chapters and recipes. Generate an index from reviewed identifiers and check for duplicate or broken targets.
3. After Gate 2 approval, draft in grouped batches: (a) F/C and evidence refresh, (b) M/X, (c) A/E, (d) S and security pass, (e) K/R and cross-reference completion. Request approval at batch milestones; each report identifies files, evidence, unresolved items and next batch. Batch boundaries may be adjusted only with user agreement.
4. Gate 4 reconciles all commands, flags, configuration, model claims and extension procedures with dated evidence and, when possible, version-pinned CLI tests in disposable environments. Record environment, versions and unexecuted checks. Quarantine unverified executable instructions and resolve or flag conflicts.
5. Gate 5 checks completeness against this matrix, uniqueness and usefulness of recipes, accessibility, terminology, trust boundaries, link consistency, and evidence for technical claims. Keep unsupported or speculative features labeled; no numerical recipe count overrides quality.
6. Gate 6 consolidates canonical Markdown into `releases/master-reference.md` and attempts DOCX and PDF generation from that source with a cover, date/version, linked TOC, readable code, tables, cross-references, headers and footers where supported. Validate actual outputs, page rendering and navigation, create a manifest and changelog, and package only completed artifacts. Pandoc 3.13 is available; PDF engine and export fidelity remain unverified (V11). Report unavailable formats rather than claiming them.
7. Preserve approval stops between Gate 2, draft milestones, technical QA, editorial/security QA and publication. Approval of this architecture authorizes the first draft batch, not later gates or publication.

## Gate 2 decision

Approve or request changes to the structure, learning progression, candidate recipe coverage and publication plan. Upon approval, start only the first draft batch and carry forward Gate 1 verification gaps.
