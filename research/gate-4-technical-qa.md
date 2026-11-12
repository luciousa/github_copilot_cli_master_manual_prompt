# Gate 4 technical QA checkpoint

**Status: reviewed with unresolved limitations; not a technical pass.** **Date:** 2026-11-11. After the gaps were explained, the user directed “use what you found.” Proceed with editorial review using the available evidence, while retaining all unresolved technical limitations below; do not describe the manual or Gate 4 as fully verified.

## Checks and corrections

| Area | Evidence and outcome | Status |
|---|---|---|
| Target CLI | CLI 1.0.109 on Windows reported version and built-in help using a temporary cache. Outside the restricted environment an isolated authenticated probe succeeded (V32), interactive `/plan` produced a review dialog and private plan (V34), and shell-level `copilot init` created instructions in a synthetic Git repository (V35). | Authenticated connectivity, one manual planning scenario and one fresh-repository initialization observed; slash `/init`, existing instructions, other modes and entitlements remain untested. |
| Command/options indexes | The 75-name command and 75-entry option indexes derive from version-specific help; [full command help](evidence/copilot-1.0.109-commands.txt) and [global help](evidence/copilot-1.0.109-help.txt) are preserved. | Partial; aliases, subcommands, versions, side effects and interactive behavior are not exhaustively reconciled. |
| Instructions and integrations | Reopened official references. In disposable Windows profiles, instruction listing found two fixture files, and minimal local skill and plugin fixtures were added, listed and removed. Plugin install printed a direct-install deprecation warning. MCP fixture add failed with a storage I/O error twice, including with isolated appdata. See V27–V28. | Limited fixture behavior tested; imports, actual agent loading, marketplaces, real components, MCP lifecycle and permissions remain untested. |
| Model and billing | Reopened official pricing and model-support sources; source snapshots differed in freshness and the retrieved plan-table markers were incomplete (V29). Version-specific entitlement and actual account pricing remain unknown. No benchmark was claimed. | Partial; model-by-plan/version matrix and account-specific checks outstanding; do not infer missing table cells. |
| Recipe format and samples | Checked 80 entries structurally and lexically. Four adapted synthetic read-only prompts ran; K01 and K16 produced useful fixture-specific observations, K21 proposed a test whose core assertion was independently checked, and K04 included unmarked assumptions (V33). | No full end-to-end recipe is verified; model identity, substantive distinctness, per-recipe sources and acceptance remain outstanding. |
| Links and anchors | Checked local file and Markdown anchor targets in 53 Markdown files: zero missing under the check's slug rules. Direct HTTP requests to all 39 unique external URLs produced connection errors; selected sources were accessible via the web tool. | Local check passed; automated external link/redirect/anchor validation unavailable from the command environment, not proven broken. |
| Safety and stale claims | Updated F3 to reflect successful version/help execution, and clarified that documented plan-mode protection is not airtight. Executable integration and recipe steps remain quarantined. | Corrections made; complete line-by-line security and editorial review remains pending. |

## Required work before Gate 4 can pass

1. Reconcile the complete slash-command and flag inventory, aliases, arguments, lifecycle status and side effects against target-version help and applicable official versioned evidence. Account for live documentation drift and note untestable features.
2. Validate `/init`, `/plan`, instruction discovery/merging, model selection, permissions, session restoration and any other claimed procedures in disposable, appropriately authorized environments. Record actual results, target OS/version and unavailable entitlements. Do not treat help output as a behavioral test.
3. Evaluate and test exact plugin, marketplace, skill, MCP and agent installation/removal workflows and provenance before presenting any copy-ready instructions. Otherwise leave them quarantined.
4. Complete the model/plan/version and OS compatibility matrices using current primary sources, and distinguish account-observed availability from general documentation. Refresh published rates and release dates before publication.
5. Verify each retained recipe against a suitable real or disposable project and its full contract; check distinctness, citations and test evidence. Merge or omit unsupported entries rather than padding the count.
6. Repeat external URL and anchor checks from a permitted network and reconcile all recorded documentation conflicts. Re-run local checks after any edits.

## Safety and execution boundary

Version/help and static checks were followed by local fixture-only skill and plugin installation/removal, two unsuccessful inert MCP configuration attempts, one authenticated harmless probe, four synthetic read-only prompts and a limited interactive `/plan` check in disposable profiles. No real external integration, sandbox test, migration or external write was performed. The user authorized a partial-draft export; the [build report](../releases/BUILD-REPORT.md) records its limitations. That snapshot predates the newer authenticated evidence. A fully verified release remains premature until the technical gaps above are addressed or explicitly accepted as limitations.
