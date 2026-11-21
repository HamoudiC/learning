r"""LEVEL 10 · Reshaping tables and handing them on
Run:  python ladder\level_10_reshaping_and_output.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · wide and long ─────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → reshaping

wide = pd.DataFrame({"name": ["A", "B"], "math": [90, 70], "art": [60, 80]})
long = pd.DataFrame({"name": ["A", "B", "A", "B"], "subject": ["math", "math", "art", "art"],
                     "mark": [90, 70, 60, 80]})

#   1a. wide as a long table with the columns name, subject, mark (one row per mark).
# your code here

#   1b. long as a wide table: one row per name, one column per subject.
# your code here


# ─── 2 · DO · pivot tables ──────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → reshaping

sales = pd.read_csv(DATA / "sales.csv")

#   2a. The total units: one row per region, one column per product, 0 where there were none.
# your code here


# ─── 3 · DO · handing it on ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → back to plain Python;  02_files.txt → saving

wide = pd.DataFrame({"name": ["A", "B"], "math": [90, 70], "art": [60, 80]})

#   3a. wide as a plain list of dicts, one per row.
# your code here

#   3b. wide as JSON text, one object per row.
# your code here


# ─── 4 · WRITE · marks_long ─────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → reshaping
#   Gives back one row per (name, subject, mark), with those three columns.
#   wide_marks: a table with a name column and one column per subject

def marks_long(wide_marks):
    pass  # your code here


# ─── 5 · WRITE · units_table ────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → reshaping;  01_series_and_dataframes.txt → columns, rows and cells
#   Gives back a dict {product: total units} for one region, from a pivot table (missing = 0).
#   df: a sales table    region: a region name

def units_table(df, region):
    pass  # your code here


# ─── 6 · WRITE · as_records ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells, looking at a table, back to plain Python
#   Gives back the first n rows as a plain list of dicts, with only the columns you ask for.
#   df: a table    columns: a list of column names    n: how many rows

def as_records(df, columns, n):
    pass  # your code here


# ─── 7 · FIX · subjects_of ──────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → looking at a table;  00_python_basics.txt → lists, tuples, dicts
#   Should give back the subject names of a wide marks table (every column except name). It gives None: fix it.

def subjects_of(wide_marks):
    return wide_marks.columns.tolist().remove("name")


if __name__ == "__main__":
    import check
    check.level(globals())
