# Partial draft build report

**Built:** 2026-11-11. **Status:** partial draft, not a verified or exhaustive master reference. This package was authorized after the user chose to use the evidence available and approved a partial-draft build.

## Artifacts

- `master-reference.md`: consolidated from 42 canonical Markdown sources, including the source registry, verification ledger and QA records.
- `master-reference.docx`: generated with Pandoc 3.13, including a Word table-of-contents field.
- `master-reference.html`: generated with Pandoc 3.13 and embedded print styling.
- `master-reference.pdf`: generated from the HTML with PyMuPDF 1.28.0; 82 pages with a linked contents list and page-number footer.
- `manifest.md`: SHA-256 hashes and sizes of the above files. The companion ZIP includes the modular sources, evidence, build scripts and these release files.

## Validation and limitations

- HTML: 188 contents links, no missing internal fragment targets and no duplicate IDs under the automated check.
- DOCX: opens with `python-docx`, contains 188 headings, 22 tables, a table-of-contents field and 274 hyperlink elements; no Unicode replacement characters found in paragraph text. The document was not visually checked in Microsoft Word; the contents field may need updating in the reader.
- PDF: 82 pages; 2,728 links checked, with no out-of-range internal page destinations; all HTML level-one and level-two heading texts were found in extracted PDF text. Sample pages were rendered for visual inspection. Some table/background rendering artifacts remain; accessibility and every page's formatting were not independently audited.
- Edge and Chrome headless PDF attempts failed in this environment; PyMuPDF supplied the PDF. DOCX has not been checked for printed headers/footers or accessibility conformance.
- Relative links from consolidated files to evidence outside the combined document depend on the accompanying directory layout. External source links were accessed selectively through the web tool; a command-environment check could not connect to 39 unique external URLs, so comprehensive external link/redirect validation remains incomplete.
- CLI 1.0.109 version/help and limited isolated instruction, skill and plugin fixture behavior were verified on Windows. Interactive CLI workflows, model entitlements, MCP lifecycle and all 80 candidate recipes remain unverified. The command and configuration catalogs, model/plan matrix and integration lifecycle instructions are incomplete. Documentation conflicts remain in the verification ledger.

## Rebuild

The source order and link rewriting are in `scripts/build_partial_reference.py`; PDF generation is in `scripts/build_partial_pdf.py`. The HTML and DOCX conversions use Pandoc and the CSS file in `scripts/`. Re-run all validation after any source or tool change. No release should be represented as complete until the unresolved technical and editorial checks are performed or clearly disclosed.
