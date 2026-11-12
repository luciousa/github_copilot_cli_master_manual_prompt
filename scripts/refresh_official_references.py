"""Refresh dated factual CLI signatures and model tables from GitHub Docs.

This is a research tool, not part of the offline Word build. It deliberately
records online documentation separately from locally tested CLI behavior.
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
import re
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
URLS = {
    "commands": "https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference",
    "models": "https://docs.github.com/en/copilot/reference/ai-models/supported-models",
    "pricing": "https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing",
}


def fetch(url):
    response = requests.get(url, timeout=30, headers={"User-Agent": "CopilotReferenceResearch/1.0"})
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def table_for(soup, identifier):
    heading = soup.find(id=identifier)
    if not heading:
        raise ValueError(f"Official documentation section missing: {identifier}")
    table = heading.find_next("table")
    if not table or not table.select("tbody tr"):
        raise ValueError(f"Official documentation table missing or empty: {identifier}")
    return table


def cell_text(cell):
    """Read text and GitHub's accessible support icons, including footnotes."""
    parts = []
    for child in cell.descendants:
        if getattr(child, "name", None) == "svg":
            label = child.get("aria-label")
            if label:
                parts.append("[" + label + "]")
        elif isinstance(child, str) and child.parent.name not in ("svg", "path", "script", "style"):
            if child.strip():
                note = child.find_parent("sup")
                parts.append("[note " + child.strip() + "]" if note else child.strip())
    return re.sub(r"\s+", " ", " ".join(parts)).strip() or "Not stated"


def escape(text):
    return text.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;").replace("\n", " ")


def markdown_table(headers, rows):
    return "| " + " | ".join(map(escape, headers)) + " |\n|" + "---|" * len(headers) + "\n" + "".join(
        "| " + " | ".join(escape(str(cell)) for cell in row) + " |\n" for row in rows
    )


def table_rows(table):
    headers = [cell.get_text(" ", strip=True) for cell in table.select("thead th")]
    rows = []
    for tr in table.select("tbody tr"):
        cells = tr.find_all(["th", "td"], recursive=False)
        if len(cells) != len(headers):
            raise ValueError("Official table structure changed; refusing to generate ambiguous rows")
        rows.append([cell_text(cell) for cell in cells])
    return headers, rows


def local_summaries():
    path = ROOT / "research/evidence/copilot-1.0.109-commands.txt"
    if not path.exists():
        raise FileNotFoundError(path)
    found = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        match = re.match(r"^\s{4}(/[-a-z]+)\s{2,}(.+)$", line)
        if match:
            found[match.group(1)] = match.group(2).strip()
    return found


def classify(name):
    critical = {
        "/allow-all", "/autopilot", "/delegate", "/downgrade", "/exit",
        "/experimental", "/extensions", "/fork", "/init", "/login", "/logout",
        "/mcp", "/move", "/permissions", "/plugin", "/pr", "/remote",
        "/reset-allowed-tools", "/restart", "/rewind", "/sandbox", "/session",
        "/settings", "/share", "/skills", "/update", "/user", "/worktree",
        "/after", "/every", "/collect-debug-logs", "/clear", "/config", "/new",
        "/add-dir", "/model", "/fleet", "/computer", "/index", "/lsp", "/memory",
    }
    return "Review side effects and permissions" if name in critical else "Check command and session context"


def main():
    command_soup = fetch(URLS["commands"])
    model_soup = fetch(URLS["models"])
    stamp = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d %H:%M %Z")
    summaries = local_summaries()
    table = table_for(command_soup, "slash-commands-in-the-interactive-interface")
    command_rows = []
    for tr in table.select("tbody tr"):
        cell = tr.find(["th", "td"], recursive=False)
        if cell is None:
            raise ValueError("Unexpected command row without a first cell")
        signature = cell.get_text("", strip=True)
        match = re.search(r"/[a-z][a-z-]*", signature)
        if not match:
            raise ValueError("Cannot identify command in row: " + signature)
        primary = match.group()
        local = summaries.get(primary)
        # Local help is software-provided, version-specific evidence. Its
        # first-line family summary is not claimed to document each subcommand.
        detail = local if local else "Not listed in captured 1.0.109 primary-command help"
        command_rows.append([signature, detail, classify(primary)])
    command_doc = f"""# GitHub Copilot CLI slash-command catalog

**Documentation accessed:** {stamp}. **Local help baseline:** Windows CLI 1.0.109. The signatures below come from the [live GitHub CLI reference]({URLS['commands']}#slash-commands-in-the-interactive-interface); the middle column is the first-line **command-family** summary from [captured 1.0.109 help](../research/evidence/copilot-1.0.109-commands.txt), not proof that the exact live signature exists in 1.0.109. Features, aliases, arguments and lifecycle status can change. Check target-version interactive help and policy before use; untested syntax is **Unverified—do not execute**.

The online table contained {len(command_rows)} entries at access. Rows represent documented variants or subcommands, not unique commands; local help is not a complete account-specific inventory. Examples and details, prerequisites and version-specific exceptions are in the source reference. Inspect the requested action before approval: commands can change settings, create or remove files, transmit data, delegate work or alter external resources. The side-effect column is a conservative review flag, not a safety certification.

""" + markdown_table(["Live documented syntax and aliases", "1.0.109 local family summary", "Review"], command_rows)
    (ROOT / "reference/slash-command-catalog.md").write_text(command_doc, encoding="utf-8")

    specs = [
        ("supported-ai-models-in-copilot", "Published model lifecycle"),
        ("supported-ai-models-per-client", "Support by client"),
        ("supported-ai-models-per-copilot-plan", "Support by paid plan"),
        ("models-with-extended-capabilities", "Extended capabilities"),
    ]
    sections = []
    for key, title in specs:
        headers, rows = table_rows(table_for(model_soup, key))
        if len(rows) < 5:
            raise ValueError(f"Unexpectedly few entries in {key}")
        sections.append(f"## {title}\n\n" + markdown_table(headers, rows))
    intro = f"""# Published Copilot model compatibility snapshot

**Accessed:** {stamp}. **Source:** [GitHub supported models]({URLS['models']}). These tables transcribe published model names, status, surface/plan support and accessible icon labels. `Included`, `Not included`, `Supported` and other bracketed terms are source labels; `Not stated` means the HTML did not state a value and must not be interpreted as a denial. Markers such as `[note 2]` refer to footnotes in the linked source. The tables are not a local account picker, a guarantee of entitlement or a statement of which models CLI 1.0.109 can select. Organization policy, location and session type can further restrict availability.

GitHub notes Free and Student access through automatic selection in the source's plan notes. Read the linked source for plan footnotes, fallback, retirement, policy and pricing caveats. [Current published pricing]({URLS['pricing']}) varies with token usage, model, context tier and billing arrangement; it is intentionally linked rather than frozen into this frequently changing matrix. Legacy premium-request billing differs from usage-based credits. No performance ranking below is an independent benchmark.

"""
    (ROOT / "reference/models-live-matrix.md").write_text(intro + "\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"Refreshed {len(command_rows)} slash-reference rows and {len(specs)} model tables at {stamp}.")


if __name__ == "__main__":
    main()
