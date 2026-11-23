r"""LEVEL 5 · Changing data: new columns, sorting, renaming
Run:  python ladder\level_05_changing_data.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · new and changed columns ───────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns

sales = pd.read_csv(DATA / "sales.csv")
sizes = {"Mouse": "S", "Keyboard": "M", "Monitor": "L", "Laptop": "L"}

#   1a. A NEW table: sales with a "revenue" column (units × price). sales itself must not change.
# your code here

#   1b. The size of each order's product, looked up in sizes.
# your code here

#   1c. Each order's units times 10.
# your code here


# ─── 2 · DO · sorting ───────────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → sorting

sales = pd.read_csv(DATA / "sales.csv")

#   2a. sales sorted by price, cheapest first.
# your code here

#   2b. The 2 most expensive orders.
# your code here

#   2c. sales sorted by region (A to Z), and within each region by units, biggest first.
# your code here


# ─── 3 · DO · renaming, dropping, types ─────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → renaming, dropping, types

sales = pd.read_csv(DATA / "sales.csv")

#   3a. sales with the units column renamed to qty.
# your code here

#   3b. sales without the date and price columns.
# your code here

#   3c. The order_id column as text.
# your code here

#   3d. The price column with missing prices filled with 0, as whole numbers.
# your code here


# ─── 4 · WRITE · add_revenue ────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns
#   Gives back a NEW table with a "revenue" column = units × price. The table you're given must not change.
#   df: a table with units and price columns

SALES = pd.DataFrame({"product": ["Keyboard", "Mouse"], "units": [2, 5], "price": [45.0, 20.0]})

def add_revenue(df):
    pass  # your code here


# ─── 5 · WRITE · top_n_by ───────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → sorting, keeping the rows that match
#   Gives back the n rows with the biggest values in that column, biggest first, numbered 0, 1, 2...
#   df: a table    column: a number column    n: how many rows

def top_n_by(df, column, n):
    pass  # your code here


# ─── 6 · WRITE · size_labels ────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns;  00_python_basics.txt → checks
#   Gives back a NEW table with a "size" column: "bulk" when units is 3 or more, otherwise "single".
#   df: a sales table

def size_labels(df):
    pass  # your code here


# ─── 7 · WRITE · tidy_columns ───────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → renaming, dropping, types;  00_python_basics.txt → loops
#   Gives back a NEW table whose column names are stripped, lowercase, with spaces turned into "_".
#   df: a table with messy column names

def tidy_columns(df):
    pass  # your code here


# ─── 8 · FIX · zero_first_units ─────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns
#   Should give back a copy of df with the first row's units set to 0. Nothing changes: fix it.

def zero_first_units(df):
    result = df.copy()
    result["units"][0] = 0
    return result


if __name__ == "__main__":
    import check
    check.level(globals())
