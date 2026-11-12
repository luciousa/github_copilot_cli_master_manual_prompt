"""Build the explicitly partial reference from the project's Markdown sources."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "releases"
GROUPS = [
    "docs/fundamentals", "docs/commands", "docs/models", "docs/context",
    "docs/agents", "docs/extensions", "docs/security", "docs/cookbook",
    "docs/appendices",
]
FILES = [p for group in GROUPS for p in sorted((ROOT / group).glob("*.md"))]
FILES += [ROOT / "reference" / n for n in (
    "command-index.md", "commands-1.0.109.md", "configuration-index.md",
    "options-1.0.109.md", "compatibility-models.md", "source-registry.md",
    "verification-ledger.md",
)]
FILES += [ROOT / "research" / n for n in (
    "gate-4-technical-qa.md", "gate-5-editorial-review.md",
)]

def anchor(path):
    relative = path.relative_to(ROOT).as_posix().lower()
    return "source-" + re.sub(r"[^a-z0-9]+", "-", relative).strip("-")

ANCHORS = {p.resolve(): anchor(p) for p in FILES}
LINK = re.compile(r"\]\(([^)]+)\)")

def fix_links(text, source):
    def convert(match):
        target = match.group(1)
        if target.startswith(("http:", "https:", "mailto:", "#")):
            return match.group(0)
        path, sep, fragment = target.partition("#")
        resolved = (source.parent / path).resolve()
        if resolved in ANCHORS:
            return "](#" + (fragment if sep and fragment else ANCHORS[resolved]) + ")"
        try:
            relative = resolved.relative_to(ROOT).as_posix()
            return "](../" + relative + ("#" + fragment if sep else "") + ")"
        except ValueError:
            return match.group(0)
    return LINK.sub(convert, text)

RELEASE.mkdir(exist_ok=True)
header = """---
title: "GitHub Copilot CLI Advanced Vibe Coding Master Reference"
subtitle: "PARTIAL DRAFT — NOT AN EXHAUSTIVE OR FULLY VERIFIED REFERENCE"
date: "Evidence reviewed 2026-11-11"
lang: en-US
---

# Read this first

This is a **partial draft**, authorized for packaging with the evidence currently available. Windows CLI 1.0.109 reported its version and help; limited disposable instruction, skill and plugin fixture tests were performed. Interactive behavior, account-specific model access and the 80 candidate recipes have not been verified end to end. An MCP fixture configuration failed. Command and configuration catalogs, compatibility matrices and integration procedures are incomplete. Unverified executable steps are not approved for use. See the verification ledger and technical QA checkpoint below for evidence and open conflicts.

"""
parts = [header]
for file in FILES:
    text = file.read_text(encoding="utf-8-sig")
    # Standalone HTML anchor lines immediately before headings are interpreted
    # as raw HTML blocks by Pandoc. Convert them to native Pandoc spans so the
    # following headings remain navigable and appear in the table of contents.
    text = re.sub(r'^<a id="([^"]+)"></a>\s*$', r'[]{#\1}\n\n', text, flags=re.MULTILINE)
    parts.append("\n[]{#" + ANCHORS[file.resolve()] + "}\n\n" + fix_links(text, file) + "\n")
(RELEASE / "master-reference.md").write_text("\n".join(parts), encoding="utf-8")
print(f"Consolidated {len(FILES)} Markdown sources into {RELEASE / 'master-reference.md'}")
