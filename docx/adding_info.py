from docx import Document

document = Document()

t = document.add_heading("Title",0)
p = document.add_paragraph("this is a paragraph \n")
p.add_run("and another \n")
p.add_run("This text is bold \n").bold = True
p.add_run("This text is italic ").italic = True


l1 = document.add_paragraph("This is item 1", style="List Bullet")
l2 = document.add_paragraph("This is item 2", style="List Bullet")
l3 = document.add_paragraph("This is item 3", style="List Bullet")
l4 = document.add_paragraph("This is item 4", style="List Bullet")
l5 = document.add_paragraph("This is item 5", style="List Bullet")

table_header = ["Name", "Age", "Job"]

some_data = [
    ["John", 46, "Programmer"],
    ["Bob", 18, "Student"],
    ["Joe", 25, "Accountant"],
    ["Kevin", 32, "Fast Food manager"]
]

table = document.add_table(rows=1, cols=3)

for i in range(3):
    table.rows[0].cells[i].text = table_header[i]

for name,age,job in some_data:
    cells = table.add_row().cells
    cells[0].text = name
    cells[1].text = str(age)
    cells[2].text = job

document.add_page_break()

document.add_heading("Heading on new page",1)

table_header = ["Name", "Age", "Job"]

more_data = [
    ["Bill", 28, "Archeologist"],
    ["Charlie", 26, "Scientist"],
    ["Fred", 21, "Shop Owner"],
    ["George", 21, "Shop Owner"],
]

table = document.add_table(rows=1, cols=3)

for i in range(3):
    table.rows[0].cells[i].text = table_header[i]

for name,age,job in more_data:
    cells = table.add_row().cells
    cells[0].text = name
    cells[1].text = str(age)
    cells[2].text = job

document.add_picture("shrek-gifgod.gif")
document.save("Test.docx")

