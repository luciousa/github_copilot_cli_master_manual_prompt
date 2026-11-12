# Gate 3, batch 1 checkpoint

**Status:** first batch approved by the user's “proceed”; batch 2 drafted separately. **Date:** 2026-11-11. Gate 2 was approved by the user's “go on.”

## Completed

- Drafted F1–F3 and C1–C4, with navigation in the root README and an unreleased changelog.
- Refreshed the official CLI reference, best-practices, installation, operation and custom-instruction documentation on 2026-11-11. Sources remain cataloged as S01, S03, S05, S07 and S14 in the [source registry](../reference/source-registry.md).
- Labeled CLI invocations unverified locally; no copy-ready installation commands or fabricated runtime results were added. Prompts are marked illustrative and separated from executable shell syntax.

## Open verification and editorial work

- Local CLI extraction failed during Gate 1, so its version, help, `/init`, `/plan`, permission prompts, session restoration and actual behavior remain untested. No authentication or installation was performed. Recheck as described in [verification ledger](../reference/verification-ledger.md).
- Resolve the documented Homebrew discrepancy, identify version-specific prerequisites and verify differences between PowerShell and POSIX examples before publishing executable procedures.
- Enumerate and cross-check all slash commands, configuration, aliases and flags in Gate 4; C4 is explicitly an orientation, not an exhaustive catalog.
- Complete model, context, agent, extension, security, cookbook and appendix chapters; complete the chapter-level scenario and technical/editorial QA on the whole manual. No PDF, DOCX or consolidated release has been generated.

## Next batch after approval

Draft M1–M3 (models and evaluation) and X1–X3 (context and prompting), refreshing authoritative evidence for model availability, policies, instruction discovery, session context and cost. Separate documented facts from judgment and continue to quarantine unverified executable examples. Stop for review at the next batch milestone.
