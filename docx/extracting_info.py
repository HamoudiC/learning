from docx.api import Document
from docx.shared import Pt

document = Document("test.docx")

for p in document.paragraphs:
    if p.style.name.startswith("Heading") or p.style.name == "Title":
        print(p.text)

for table in document.tables:
    print("\nNEW TABLE")
    for row in table.rows:
        print("|".join([cell.text for cell in row.cells]))

all_text = ""

for p in document.paragraphs:
    all_text += p.text
    all_text += "\n"

print("\nALL TEXT")
print(all_text)

all_16pt_text = ""

for p in document.paragraphs:
    for run in p.runs:
        if run.font.size == Pt(16):
            all_16pt_text += run.text
            all_16pt_text += "\n"
            break

print("\nALL 16PX TEXT")
print(all_16pt_text)