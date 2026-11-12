# Gate 3 reference checkpoint

**Status:** appendix drafts added; the exhaustive reference requirement is not yet complete. Awaiting review of this milestone. **Date:** 2026-11-11. K61–K80 and initial indexes approved as drafts by the user's “yes, proceed.”

## Completed

- Added draft extension review, security checklist, prompt and conceptual template library, troubleshooting/FAQ, glossary and preliminary topic index; updated navigation and changelog. The command index now includes 75 primary names extracted from version 1.0.109 help, with the full captured help preserved as evidence.
- Clarified documented configuration precedence and its managed-policy exceptions. All CLI procedures remain locally untested and no install/uninstall procedure is presented as verified.
- Captured version 1.0.109 help for initialization, plugins, MCP and skills. Plugin help describes one included default marketplace; this does not establish the current configuration or resolve the conflicting live pages.
- Captured configuration, environment and plugin/MCP/skill add and remove help; added indexes of 75 primary commands and 75 global option entries from local help, and linked component-specific evidence. These remain discovery references, not verified lifecycle procedures.

## Material remaining work

- The command index and configuration index are **partial**, not exhaustive. The model/compatibility matrix lacks a verified model-by-plan/version inventory. The extension reference lacks vetted individual integrations and verified exact installation/removal instructions. The alphabetical index and final prompt/configuration artifacts are incomplete.
- The initial CLI extraction failure was bypassed with a temporary writable `COPILOT_CACHE_HOME`: CLI 1.0.109 reported its version and built-in help on Windows. Interactive behavior, authentication and recipes remain untested. Current online documentation is accessible, but live pages are not proof of behavior in a particular release. Prior conflicts V16–V18 remain open; V24 records a new help/documentation discrepancy.
- The 80 cookbook entries are candidate drafts, not verified recipes. No runnable examples, OS variants, DOCX/PDF exports or final publication have been validated.

## Recommended next action

Continue the version-pinned catalog using the captured CLI 1.0.109 help and official sources. Record actual results and limitations; do not label these appendices exhaustive or complete until supported by evidence. Present the completed draft and outstanding gaps for approval before Gate 4 technical QA.
