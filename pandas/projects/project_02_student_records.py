r"""PROJECT 2 · Student records          (levels 1-8)
Join data/students.csv with data/programs.csv and answer an advisor's questions.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_02_student_records.py
"""
# ── your setup lines go here ──



STUDENTS = pd.read_csv(DATA / "students.csv")
PROGRAMS = pd.read_csv(DATA / "programs.csv")


# ─── 1 · WRITE · with_programs ──────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables
#   Gives back every student with their program's school and credits_needed (NaN if not found).
#   students, programs: the two tables

def with_programs(students, programs):
    pass  # your code here


# ─── 2 · WRITE · credits_remaining ──────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  01_series_and_dataframes.txt → maths and filtering;  00_python_basics.txt → lists, tuples, dicts
#   Gives back {name: credits still needed}, for students whose program is in programs.
#   students, programs: the two tables

def credits_remaining(students, programs):
    pass  # your code here


# ─── 3 · WRITE · honours ────────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match, sorting
#   Gives back the names with a gpa of min_gpa or more, highest gpa first.
#   students: the students table    min_gpa: a number

def honours(students, min_gpa):
    pass  # your code here


# ─── 4 · WRITE · at_risk ────────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  01_series_and_dataframes.txt → back to plain Python
#   Gives back the names with a gpa below max_gpa, in file order.
#   students: the students table    max_gpa: a number

def at_risk(students, max_gpa):
    pass  # your code here


# ─── 5 · WRITE · program_report ─────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  01_series_and_dataframes.txt → maths and filtering
#   Gives back one row per program: program, students (how many), avg_gpa (rounded to 2).
#   students: the students table

def program_report(students):
    pass  # your code here


# ─── 6 · WRITE · progress_percent ───────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  01_series_and_dataframes.txt → maths and filtering;  00_python_basics.txt → lists, tuples, dicts
#   Gives back {name: % of the needed credits done, rounded to 1}, for students whose program is in programs.
#   students, programs: the two tables

def progress_percent(students, programs):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
