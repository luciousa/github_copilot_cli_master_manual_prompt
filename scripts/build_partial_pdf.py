"""Render the partial draft HTML to PDF using the locally installed PyMuPDF."""
from pathlib import Path
import fitz

root = Path(__file__).resolve().parents[1]
html = (root / "releases/master-reference.html").read_text(encoding="utf-8")
css = (root / "scripts/partial-reference.css").read_text(encoding="utf-8")
story = fitz.Story(html=html, user_css=css, em=10)

def rectangle(_number, _filled):
    page = fitz.Rect(0, 0, 595, 842)
    return page, fitz.Rect(45, 48, 550, 790), None

document = story.write_with_links(rectangle)
for index, page in enumerate(document):
    page.insert_text((45, 818), f"PARTIAL DRAFT  |  {index + 1}", fontsize=8, color=(0.3, 0.3, 0.3))
output = root / "releases/master-reference.pdf"
document.save(output, garbage=4, deflate=True)
print(f"Wrote {len(document)} pages to {output}")
