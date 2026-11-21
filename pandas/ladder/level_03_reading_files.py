r"""LEVEL 3 · Reading and writing files
Run:  python ladder\level_03_reading_files.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
Open data/sales.csv in VS Code and look at it before you start.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"
OUT = Path(__file__).parent.parent / "out"


# ─── 1 · DO · reading a CSV ─────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → reading;  01_series_and_dataframes.txt → looking at a table
#   Bags: 04_cleaning.txt → missing values

sales_file = DATA / "sales.csv"

#   1a. sales_file read into a table.
# your code here

#   1b. How many rows and columns the sales file has.
# your code here

#   1c. How many values are missing in the units column of the sales file.
# your code here

#   1d. Only the region and units columns, read straight from the file.
# your code here

#   1e. Only the first 5 rows, read straight from the file.
# your code here


# ─── 2 · DO · other options ─────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → reading;  01_series_and_dataframes.txt → columns, rows and cells

sales_file = DATA / "sales.csv"
students_file = DATA / "students.csv"

#   2a. The product of order 1003, reading the file with order_id as the row labels.
# your code here

#   2b. The students file's column names, as a plain list.
# your code here


# ─── 3 · WRITE · load ───────────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → finding files, reading
#   Gives back a CSV file from the data folder as a table.
#   file_name: like "students.csv"

def load(file_name):
    pass  # your code here


# ─── 4 · WRITE · save_csv ───────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → finding files, saving
#   Saves df in the OUT folder as a CSV without the row labels (make OUT if it isn't there),
#   and gives back the path it saved to.
#   df: a table    file_name: like "test.csv"

def save_csv(df, file_name):
    pass  # your code here


# ─── 5 · WRITE · excel_round_trip ───────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → saving, reading
#   Saves df as an Excel file in OUT (no row labels), and gives back the table read back from that file.
#   df: a table    file_name: like "test.xlsx"

def excel_round_trip(df, file_name):
    pass  # your code here


# ─── 6 · FIX · copy_file ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → saving
#   Should copy a data file to OUT and give back the copy read back in, matching the original.
#   The copy gets an extra column: fix it.

def copy_file(file_name):
    OUT.mkdir(exist_ok=True)
    pd.read_csv(DATA / file_name).to_csv(OUT / file_name)
    return pd.read_csv(OUT / file_name)


if __name__ == "__main__":
    import check
    check.level(globals())
