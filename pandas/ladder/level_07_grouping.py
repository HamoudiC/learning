r"""LEVEL 7 · Grouping and summarising
Run:  python ladder\level_07_grouping.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · one answer per group ──────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group

sales = pd.read_csv(DATA / "sales.csv")
sales = sales.assign(revenue=sales["units"] * sales["price"])

#   1a. The total units for each region.
# your code here

#   1b. The total revenue for each product.
# your code here

#   1c. The product with the most revenue.
# your code here

#   1d. How many orders (rows) each product has.
# your code here


# ─── 2 · DO · several answers at once ───────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group

sales = pd.read_csv(DATA / "sales.csv")

#   2a. For each region: a column "orders" (how many order_ids) and a column "units" (total units).
# your code here

#   2b. The same table, with region as a normal column and the rows numbered 0, 1, 2...
# your code here


# ─── 3 · DO · counting ──────────────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → counting

sales = pd.read_csv(DATA / "sales.csv")

#   3a. How many orders each region has, most first.
# your code here

#   3b. How many different products there are.
# your code here

#   3c. A count table: one row per region, one column per product.
# your code here


# ─── 4 · WRITE · units_by_region ────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  01_series_and_dataframes.txt → back to plain Python
#   Gives back a dict {region: total units}.
#   df: a sales table

def units_by_region(df):
    pass  # your code here


# ─── 5 · WRITE · best_product ───────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group
#   Gives back the name of the product with the most revenue.
#   df: a sales table with a revenue column

def best_product(df):
    pass  # your code here


# ─── 6 · WRITE · region_summary ─────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group
#   Gives back one row per region with the columns region, orders (how many), revenue (total).
#   df: a sales table with a revenue column

def region_summary(df):
    pass  # your code here


# ─── 7 · WRITE · average_gpa_by_program ─────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  01_series_and_dataframes.txt → maths and filtering
#   Gives back a dict {program: average gpa rounded to 2}.
#   students: a students table

def average_gpa_by_program(students):
    pass  # your code here


# ─── 8 · FIX · busiest_region ───────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group
#   Should give back the region with the most orders. It gives the wrong one: fix it.

def busiest_region(df):
    counts = df.groupby("region").size().reset_index()
    return counts["region"].max()


if __name__ == "__main__":
    import check
    check.level(globals())
