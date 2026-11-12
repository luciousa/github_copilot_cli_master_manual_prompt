from zipfile import ZipFile
import shutil

import pytest
from docx import Document
from lxml import etree
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from reference_builder import cli


def test_discovery_preserves_order_and_rejects_missing_and_duplicates(tmp_path):
    (tmp_path / "a").mkdir(); (tmp_path / "b").mkdir()
    (tmp_path / "a" / "2.md").write_text("# Two", encoding="utf-8")
    (tmp_path / "a" / "1.md").write_text("# One", encoding="utf-8")
    (tmp_path / "b" / "3.md").write_text("# Three", encoding="utf-8")
    assert [p.name for p in cli.discover(tmp_path, ["b/*.md", "a/*.md"])] == ["3.md", "1.md", "2.md"]
    with pytest.raises(ValueError, match="matched no"):
        cli.discover(tmp_path, ["missing/*.md"])
    with pytest.raises(ValueError, match="more than once"):
        cli.discover(tmp_path, ["a/*.md", "a/1.md"])


def test_consolidation_preserves_code_and_rewrites_links(tmp_path):
    (tmp_path / "docs").mkdir(); (tmp_path / "reference").mkdir(); (tmp_path / "research").mkdir()
    source = tmp_path / "docs" / "one.md"; target = tmp_path / "reference" / "two.md"
    source.write_text('# Héllo\n\n[Other](../reference/two.md) [Evidence](../research/log.txt) [Web](https://example.org)\n\n- --arg <directory>\n\n```md\n[Keep](../research/log.txt) <directory>\n```\n', encoding="utf-8")
    target.write_text('# Target\n\n| A | B |\n|---|---|\n| 1 | 2 |\n', encoding="utf-8")
    markdown, excluded = cli.consolidate(tmp_path, [source.resolve(), target.resolve()])
    assert '[Other](#source-reference-two-md)' in markdown
    assert 'Evidence (source repository: research/log.txt)' in markdown
    assert '[Web](https://example.org)' in markdown
    assert '&lt;directory&gt;' in markdown
    assert '[Keep](../research/log.txt) <directory>' in markdown
    assert 'Héllo' in markdown and '| 1 | 2 |' in markdown
    assert len(excluded) == 1


def test_coverage_rejects_omitted_guide_files(tmp_path):
    (tmp_path / "docs").mkdir(); (tmp_path / "reference").mkdir()
    included = tmp_path / "docs" / "one.md"; included.write_text("# One", encoding="utf-8")
    omitted = tmp_path / "reference" / "two.md"; omitted.write_text("# Two", encoding="utf-8")
    with pytest.raises(ValueError, match="reference/two.md"):
        cli.check_coverage(tmp_path, [included.resolve()])
    cli.check_coverage(tmp_path, [included.resolve(), omitted.resolve()])


@pytest.mark.skipif(shutil.which("pandoc") is None, reason="Pandoc is required")
def test_build_creates_cover_toc_bookmarks_and_tables(tmp_path, monkeypatch):
    (tmp_path / "docs").mkdir(); (tmp_path / "reference").mkdir()
    (tmp_path / "docs" / "chapter.md").write_text('# Chapter\n\n[Reference](../reference/ref.md)\n\n```python\nprint("café")\n```\n', encoding="utf-8")
    (tmp_path / "reference" / "ref.md").write_text('# Reference\n\n| A | B |\n|---|---|\n| 1 | 2 |\n', encoding="utf-8")
    config = tmp_path / "document.toml"
    config.write_text('[document]\ntitle="Example guide"\nauthor="Test Author"\noutput="out/book.docx"\nreport="out/report.md"\n[sources]\ngroups=["docs/*.md", "reference/*.md"]\n', encoding="utf-8")
    monkeypatch.setattr(cli, "ROOT", tmp_path)
    assert cli.main(["--config", str(config), "--no-word"]) == 0
    output = tmp_path / "out" / "book.docx"; doc = Document(output)
    assert doc.core_properties.title == "Example guide"
    assert doc.core_properties.author == "Test Author"
    assert any("Test Author" in p.text for p in doc.paragraphs)
    assert any("café" in p.text for p in doc.paragraphs)
    assert len(doc.tables) == 1
    assert "Test Author" in doc.sections[0].footer.paragraphs[0].text
    with ZipFile(output) as archive:
        xml = etree.fromstring(archive.read("word/document.xml"))
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        anchors = set(xml.xpath("//w:bookmarkStart/@w:name", namespaces=ns))
        links = xml.xpath("//w:hyperlink/@w:anchor", namespaces=ns)
        fields = xml.xpath("//w:instrText/text()", namespaces=ns)
        assert links and set(links) <= anchors
        assert any("TOC " in x for x in fields)
    report = (tmp_path / "out" / "report.md").read_text(encoding="utf-8")
    assert "Sources: 2" in report and "Test Author" in report
    # Word represents fragments in external URLs as an anchor plus a
    # relationship; that fragment is not a bookmark within this document.
    doc = Document(output)
    link = OxmlElement("w:hyperlink")
    link.set(qn("w:anchor"), "external-fragment")
    link.set(qn("r:id"), "rIdExternal")
    doc.paragraphs[-1]._p.append(link)
    doc.save(output)
    cli.validate_document(output, "Example guide", "Test Author")
