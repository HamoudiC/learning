r"""LEVEL 8 · Combining tables: merge and concat
Run:  python ladder\level_08_combining.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
Open data/students.csv and data/programs.csv first: which program is missing from each?
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · joining two tables ────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  04_cleaning.txt → missing values

students = pd.read_csv(DATA / "students.csv")
programs = pd.read_csv(DATA / "programs.csv")

#   1a. students joined with programs on program, keeping only the students whose program is found.
# your code here

#   1b. students joined with programs, keeping every student.
# your code here

#   1c. students joined with programs, keeping every row of both.
# your code here

#   1d. How many students have no school after joining like in 1b.
# your code here


# ─── 2 · DO · one table under another ───────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  01_series_and_dataframes.txt → looking at a table

students = pd.read_csv(DATA / "students.csv")

#   2a. The first 2 students and the last student in one table, numbered 0, 1, 2.
# your code here


# ─── 3 · WRITE · with_school ────────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables
#   Gives back every student with their program's school and credits_needed added (NaN if not found).
#   students, programs: the two tables

def with_school(students, programs):
    pass  # your code here


# ─── 4 · WRITE · credits_left ───────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  01_series_and_dataframes.txt → maths and filtering;  00_python_basics.txt → lists, tuples, dicts
#   Gives back a dict {name: credits still needed}, for the students whose program is in programs.
#   students, programs: the two tables

def credits_left(students, programs):
    pass  # your code here


# ─── 5 · WRITE · programs_with_no_students ──────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  03_selecting_and_changing.txt → keeping the rows that match
#   Gives back a plain list of the programs nobody is studying.
#   students, programs: the two tables

def programs_with_no_students(students, programs):
    pass  # your code here


# ─── 6 · WRITE · stack_terms ────────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables;  03_selecting_and_changing.txt → new and changed columns
#   Gives back one table of both terms, numbered 0, 1, 2..., with a "term" column saying "fall" or "spring".
#   fall, spring: two tables with the same columns

def stack_terms(fall, spring):
    pass  # your code here


# ─── 7 · FIX · everyone_with_school ─────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → joining tables
#   Should give back ALL the students with their school. One student goes missing: fix it.

def everyone_with_school(students, programs):
    return pd.merge(students, programs, on="program")


if __name__ == "__main__":
    import check
    check.level(globals())
