"""Command-line entry point for the Word reference builder."""
from __future__ import annotations

import argparse
from datetime import date
import glob
import html
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile
from xml.etree import ElementTree

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")
ANCHOR = re.compile(r'^<a id="([^"]+)"></a>\s*$', re.M)
PLACEHOLDER = re.compile(r"<([A-Za-z][A-Za-z0-9_-]*)>")


def load_config(path: Path) -> dict:
    with path.open("rb") as stream:
        config = tomllib.load(stream)
    if not config.get("document", {}).get("title") or not config["document"].get("author"):
        raise ValueError("Configuration must specify document.title and document.author")
    if not config.get("sources", {}).get("groups"):
        raise ValueError("Configuration must specify sources.groups")
    return config


def discover(root: Path, groups: list[str]) -> list[Path]:
    files, seen = [], set()
    for pattern in groups:
        matches = sorted(Path(p).resolve() for p in glob.glob(str(root / pattern), recursive=True))
        matches = [p for p in matches if p.is_file() and p.suffix.lower() == ".md"]
        if not matches:
            raise ValueError(f"Source pattern matched no Markdown files: {pattern}")
        for p in matches:
            if not p.is_relative_to(root.resolve()):
                raise ValueError(f"Source is outside the project: {p}")
            if p in seen:
                raise ValueError(f"Source included more than once: {p}")
            seen.add(p)
            files.append(p)
    return files


def check_coverage(root: Path, files: list[Path]) -> None:
    """Fail rather than silently omitting a guide or reference Markdown file."""
    expected = {p.resolve() for directory in (root / "docs", root / "reference")
                if directory.exists() for p in directory.rglob("*.md") if p.is_file()}
    missing = sorted(expected - set(files))
    if missing:
        paths = ", ".join(p.relative_to(root.resolve()).as_posix() for p in missing)
        raise ValueError("Guide or reference files missing from source order: " + paths)


def anchor(root: Path, path: Path) -> str:
    return "source-" + re.sub(r"[^a-z0-9]+", "-", path.relative_to(root.resolve()).as_posix().lower()).strip("-")


def convert_links(line: str, source: Path, root: Path, anchors: dict[Path, str], excluded: list[str]) -> str:
    def replace(m: re.Match) -> str:
        label, target = m.groups()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        split = urlsplit(target)
        resolved = (source.parent / unquote(split.path)).resolve()
        if resolved in anchors:
            return f"[{label}](#{split.fragment or anchors[resolved]})"
        try:
            relative = resolved.relative_to(root.resolve()).as_posix()
        except ValueError:
            relative = "external local file"
        excluded.append(f"{source.relative_to(root.resolve()).as_posix()}: {target}")
        return f"{label} (source repository: {relative})"
    return LINK.sub(replace, line)


def consolidate(root: Path, files: list[Path]) -> tuple[str, list[str]]:
    root = root.resolve()
    anchors = {p: anchor(root, p) for p in files}
    if len(set(anchors.values())) != len(anchors):
        raise ValueError("Two source paths map to the same document anchor")
    excluded, parts = [], []
    for p in files:
        text = p.read_text(encoding="utf-8-sig")
        text = ANCHOR.sub(lambda m: f"[]{{#{m.group(1)}}}\n\n", text)
        output, fenced, fence_char = [], False, ""
        for line in text.splitlines(keepends=True):
            match = re.match(r"^\s*(`{3,}|~{3,})", line)
            if match:
                marker = match.group(1)[0]
                if not fenced:
                    fenced, fence_char = True, marker
                elif marker == fence_char:
                    fenced = False
                output.append(line)
                continue
            if not fenced:
                # Preserve Pandoc-style placeholders such as <directory> as text.
                chunks = re.split(r"(`[^`\n]*`)", line)
                for i in range(0, len(chunks), 2):
                    chunks[i] = PLACEHOLDER.sub(lambda m: html.escape(m.group(0)), chunks[i])
                    chunks[i] = convert_links(chunks[i], p, root, anchors, excluded)
                line = "".join(chunks)
            output.append(line)
        parts.append(f"[]{{#{anchors[p]}}}\n\n" + "".join(output))
    return "\n\n".join(parts), excluded


def add_field(paragraph, instruction: str):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    code = OxmlElement("w:instrText"); code.set(qn("xml:space"), "preserve"); code.text = instruction
    separate = OxmlElement("w:fldChar"); separate.set(qn("w:fldCharType"), "separate")
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    for element in (begin, code, separate, end): run._r.append(element)


def internal_link(paragraph, bookmark: str, text: str):
    link = OxmlElement("w:hyperlink"); link.set(qn("w:anchor"), bookmark)
    run = OxmlElement("w:r"); props = OxmlElement("w:rPr")
    style = OxmlElement("w:rStyle"); style.set(qn("w:val"), "Hyperlink"); props.append(style)
    run.append(props); element = OxmlElement("w:t"); element.text = text; run.append(element)
    link.append(run); paragraph._p.append(link)


def style_document(doc: Document, config: dict):
    settings = config["document"]
    normal = doc.styles["Normal"]
    normal.font.name = settings.get("body_font", "Calibri")
    normal.font.size = Pt(float(settings.get("body_size", 10.5)))
    normal.paragraph_format.space_after = Pt(5)
    color = RGBColor.from_string(settings.get("accent", "173A5E"))
    for level in range(1, 7):
        style = doc.styles[f"Heading {level}"]
        style.font.name = settings.get("heading_font", "Calibri")
        style.font.color.rgb = color
        style.font.bold = True
        style.paragraph_format.keep_with_next = True
    for section in doc.sections:
        section.top_margin = Inches(.85); section.bottom_margin = Inches(.8)
        section.left_margin = Inches(.85); section.right_margin = Inches(.85)
        section.different_first_page_header_footer = True
        header = section.header.paragraphs[0]
        header.text = "COPILOT CLI MASTER REFERENCE  |  VERSION-AWARE EDITION"
        header.style = doc.styles["Normal"]; header.runs[0].font.size = Pt(8)
        footer = section.footer.paragraphs[0]; footer.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        footer.add_run(settings["author"] + "  |  "); add_field(footer, " PAGE ")


def add_cover_and_toc(doc: Document, config: dict) -> int:
    settings = config["document"]
    body = doc._body._element
    first = body[0]
    heading_rows = []
    for p in doc.paragraphs:
        if not p.style.name.startswith("Heading "):
            continue
        level = int(p.style.name.split()[-1])
        if level > int(settings.get("toc_depth", 3)) or not p.text.strip():
            continue
        bookmarks = p._p.xpath(".//w:bookmarkStart")
        if bookmarks:
            heading_rows.append((level, p.text, bookmarks[0].get(qn("w:name"))))
    def prepend(p):
        first.addprevious(p._p)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(100)
    r = p.add_run(settings["title"]); r.bold = True; r.font.size = Pt(30)
    r.font.name = settings.get("heading_font", "Calibri"); r.font.color.rgb = RGBColor.from_string(settings.get("accent", "173A5E")); prepend(p)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(settings.get("subtitle", "VERSION-AWARE REFERENCE")); r.bold = True; r.font.size = Pt(13); prepend(p)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(26); p.add_run("Author: " + settings["author"]); prepend(p)
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("Evidence reviewed: " + str(settings.get("evidence_date", "not stated"))); prepend(p)
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(36)
    p.add_run("Evidence and limitations are recorded in the verification ledger. Availability, behavior and costs vary by version, account, platform and policy; most complete recipe workflows have not been tested.").italic = True; prepend(p)
    p = doc.add_paragraph(); p.add_run().add_break(); p.runs[0].add_break(); p.paragraph_format.page_break_before = True; prepend(p)
    p = doc.add_paragraph("Contents", style="Title"); prepend(p)
    p = doc.add_paragraph("Contents are linked. Update the table in Word after editing to refresh page numbers."); p.runs[0].italic = True; prepend(p)
    # A TOC field with a cached, clickable fallback. Word can replace the cached
    # content with a paginated table; other readers still show working links.
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(0)
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    code = OxmlElement("w:instrText"); code.set(qn("xml:space"), "preserve"); code.text = f' TOC \\o "1-{settings.get("toc_depth", 3)}" \\h \\z \\u '
    sep = OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"), "separate")
    r = p.add_run(); r._r.append(begin); r._r.append(code); r._r.append(sep)
    for level, title, bookmark in heading_rows:
        internal_link(p, bookmark, "    " * (level - 1) + title)
        p.add_run().add_break()
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end"); p.add_run()._r.append(end); prepend(p)
    p = doc.add_paragraph(); p.paragraph_format.page_break_before = True; prepend(p)
    return len(heading_rows)


def validate_document(path: Path, title: str, author: str) -> tuple[int, int, int]:
    """Validate metadata, contents field and internal bookmark targets."""
    document = Document(path)
    if document.core_properties.title != title or document.core_properties.author != author:
        raise ValueError("Generated document metadata does not match the configuration")
    if not any(author in paragraph.text for paragraph in document.paragraphs[:10]):
        raise ValueError("The configured author was not found on the cover")
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with ZipFile(path) as archive:
        xml = ElementTree.fromstring(archive.read("word/document.xml"))
    bookmarks = {element.get(qn("w:name")) for element in xml.findall(".//w:bookmarkStart", ns)}
    # Word can split an external URL into a relationship and an anchor. Only
    # hyperlinks without an external relationship target local bookmarks.
    links = [element.get(qn("w:anchor")) for element in xml.findall(".//w:hyperlink", ns)
             if element.get(qn("w:anchor")) and not element.get(qn("r:id"))]
    missing = sorted(set(links) - bookmarks)
    if missing:
        raise ValueError("Generated document has missing bookmark targets: " + ", ".join(missing[:10]))
    instructions = [element.text or "" for element in xml.findall(".//w:instrText", ns)]
    if not any("TOC " in instruction for instruction in instructions):
        raise ValueError("Generated document is missing an updateable contents field")
    headings = sum(paragraph.style.name.startswith("Heading ") for paragraph in document.paragraphs)
    return headings, len(document.tables), len(links)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the modular guide as a Word document.")
    parser.add_argument("--config", type=Path, default=ROOT / "document.toml")
    parser.add_argument("--output", type=Path, help="Override the configured output path")
    parser.add_argument("--markdown", type=Path, help="Also save consolidated Markdown to this path")
    parser.add_argument("--no-word", action="store_true", help="Skip optional Microsoft Word field update")
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        files = discover(ROOT, config["sources"]["groups"])
        check_coverage(ROOT, files)
        markdown, excluded = consolidate(ROOT, files)
        if args.markdown:
            args.markdown.parent.mkdir(parents=True, exist_ok=True)
            args.markdown.write_text(f"# {config['document']['title']}\n\nAuthor: {config['document']['author']}\n\nEvidence date: {config['document']['evidence_date']}\n\n" + markdown, encoding="utf-8")
        pandoc = shutil.which("pandoc")
        if not pandoc:
            raise RuntimeError("Pandoc was not found on PATH. Install Pandoc and try again.")
        output = (args.output or ROOT / config["document"]["output"]).resolve()
        report = (ROOT / config["document"]["report"]).resolve()
        if output.suffix.lower() != ".docx": raise ValueError("Output must have a .docx extension")
        output.parent.mkdir(parents=True, exist_ok=True); report.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="reference-builder-") as temp:
            temp = Path(temp); source = temp / "guide.md"; intermediate = temp / "guide.docx"
            source.write_text(markdown, encoding="utf-8")
            subprocess.run([pandoc, str(source), "--from=markdown", "--to=docx", "--standalone", "--output", str(intermediate)], check=True, cwd=ROOT)
            doc = Document(intermediate)
            doc.core_properties.title = config["document"]["title"]
            doc.core_properties.author = config["document"]["author"]
            doc.core_properties.subject = config["document"].get("subtitle", "Version-aware reference")
            style_document(doc, config); toc_count = add_cover_and_toc(doc, config)
            settings = doc.settings._element
            update = OxmlElement("w:updateFields"); update.set(qn("w:val"), "true"); settings.append(update)
            doc.save(output)
        word_result = "Skipped; clickable cached contents remain available."
        if not args.no_word and sys.platform == "win32":
            helper = Path(__file__).with_name("word_update.py")
            try:
                with tempfile.TemporaryDirectory(prefix="reference-word-update-") as temp:
                    candidate = Path(temp) / "candidate.docx"
                    shutil.copy2(output, candidate)
                    result = subprocess.run([sys.executable, str(helper), str(candidate)], capture_output=True, text=True, timeout=45)
                    if result.returncode == 0:
                        Document(candidate)
                        shutil.copy2(candidate, output)
                        word_result = result.stdout.strip()
                    else:
                        details = (result.stderr.strip() or result.stdout.strip() or "Word update failed").splitlines()[-1]
                        word_result = "Unavailable: " + details
            except subprocess.TimeoutExpired:
                word_result = "Unavailable: Word automation timed out; clickable cached contents remain."
        headings, table_count, internal_links = validate_document(
            output, config["document"]["title"], config["document"]["author"])
        report.write_text("# Word reference build report\n\n" +
            f"- Built: {date.today().isoformat()}\n- Author: {config['document']['author']}\n- Output: {output}\n" +
            f"- Sources: {len(files)}\n- Heading paragraphs: {headings}\n- Tables: {table_count}\n- Cached contents links: {toc_count}\n" +
            f"- Validation: DOCX reopened; title and author metadata, cover author, updateable contents field, and {internal_links} internal bookmark links checked.\n" +
            f"- Word field update: {word_result}\n- Excluded local references rendered as text: {len(excluded)}\n" +
            "- Evidence: see the verification ledger for tested scenarios and remaining platform, integration and recipe limitations.\n\n## Included sources\n\n" +
            "\n".join(f"- `{p.relative_to(ROOT).as_posix()}`" for p in files) +
            "\n\n## Excluded local links\n\n" + ("\n".join(f"- `{x}`" for x in excluded) or "None") + "\n", encoding="utf-8")
        print(f"Created: {output}\nReport: {report}\nWord field update: {word_result}")
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
