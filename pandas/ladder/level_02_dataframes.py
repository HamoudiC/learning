r"""LEVEL 2 · DataFrames: a whole table
Run:  python ladder\level_02_dataframes.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd


# ─── 1 · DO · looking at a table ────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → looking at a table

people = pd.DataFrame({
    "name": ["Sara", "Omar", "Lina", "Yusuf"],
    "program": ["AI", "AI", "Business", "Design"],
    "gpa": [3.8, 3.1, 3.5, 2.7],
    "credits": [54, 24, 90, 48],
})

#   1a. How many rows and columns people has.
# your code here

#   1b. The column names, as a plain list.
# your code here

#   1c. The first 2 rows.
# your code here

#   1d. The type of the values in the credits column.
# your code here


# ─── 2 · DO · columns ───────────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells, maths and filtering

people = pd.DataFrame({
    "name": ["Sara", "Omar", "Lina", "Yusuf"],
    "program": ["AI", "AI", "Business", "Design"],
    "gpa": [3.8, 3.1, 3.5, 2.7],
    "credits": [54, 24, 90, 48],
})

#   2a. The gpa column.
# your code here

#   2b. A table with only the name and gpa columns.
# your code here

#   2c. Everyone's credits added up.
# your code here

#   2d. The highest gpa.
# your code here


# ─── 3 · DO · rows and cells ────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells, back to plain Python

people = pd.DataFrame({
    "name": ["Sara", "Omar", "Lina", "Yusuf"],
    "program": ["AI", "AI", "Business", "Design"],
    "gpa": [3.8, 3.1, 3.5, 2.7],
    "credits": [54, 24, 90, 48],
})

#   3a. The name in the row labelled 2.
# your code here

#   3b. The whole first row.
# your code here

#   3c. The table as a plain list of dicts, one per row.
# your code here


# ─── 4 · DO · making tables ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → making a DataFrame

names = ["Sara", "Omar"]
ages = [20, 19]
rows = [{"item": "pen", "qty": 3}, {"item": "ink", "qty": 1}]

#   4a. A table with a "name" column (names) and an "age" column (ages).
# your code here

#   4b. A table made from rows.
# your code here


# ─── 5 · WRITE · column_report ──────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells, maths and filtering;  00_python_basics.txt → numbers
#   Gives back {"min": ..., "max": ..., "mean": ...} of one column, as plain numbers, mean rounded to 2.
#   df: a table    column: the name of a number column

def column_report(df, column):
    pass  # your code here


# ─── 6 · WRITE · names_of ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → back to plain Python;  00_python_basics.txt → text
#   Gives back the names joined into one text with ", " between them.
#   df: a table with a "name" column

def names_of(df):
    pass  # your code here


# ─── 7 · FIX · two_columns ──────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells
#   Should give back a table with only the "name" and "gpa" columns. It crashes: fix it.

def two_columns(df):
    return df["name", "gpa"]


if __name__ == "__main__":
    import check
    check.level(globals())
