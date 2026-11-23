r"""LEVEL 4 · Choosing rows: by position, by label, by condition
Run:  python ladder\level_04_choosing_rows.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · by position or by label ───────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → by position or by label;  01_series_and_dataframes.txt → columns, rows and cells

sales = pd.read_csv(DATA / "sales.csv")

#   1a. The third row, by position.
# your code here

#   1b. The first 3 rows.
# your code here

#   1c. The order_id of the rows labelled 0 to 2.
# your code here


# ─── 2 · DO · keeping the rows that match ───────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match

sales = pd.read_csv(DATA / "sales.csv")

#   2a. The orders with more than 3 units.
# your code here

#   2b. The orders from the South region.
# your code here

#   2c. The North orders with at least 2 units.
# your code here

#   2d. The Laptop and Monitor orders.
# your code here

#   2e. How many orders have a price over 100.
# your code here


# ─── 3 · DO · old labels stay ───────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  01_series_and_dataframes.txt → looking at a table

sales = pd.read_csv(DATA / "sales.csv")

#   3a. The row labels of the North orders, as a plain list.
# your code here

#   3b. The North orders, with the rows numbered 0, 1, 2... again.
# your code here


# ─── 4 · WRITE · orders_in ──────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  01_series_and_dataframes.txt → columns, rows and cells
#   Gives back that region's orders, with only the columns order_id, product, units, and rows numbered 0, 1, 2...
#   df: a sales table    region: like "East"

def orders_in(df, region):
    pass  # your code here


# ─── 5 · WRITE · big_orders ─────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  01_series_and_dataframes.txt → back to plain Python
#   Gives back a plain list of the order_ids with at least min_units units.
#   df: a sales table    min_units: a number

def big_orders(df, min_units):
    pass  # your code here


# ─── 6 · WRITE · products_in ────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  05_grouping_and_combining.txt → counting;  01_series_and_dataframes.txt → back to plain Python;  00_python_basics.txt → lists, tuples, dicts
#   Gives back a sorted plain list of the different products sold in any of those regions.
#   df: a sales table    regions: a list of region names

def products_in(df, regions):
    pass  # your code here


# ─── 7 · WRITE · cheap_in_region ────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match
#   Gives back how many orders are in that region AND have a price of max_price or less.
#   df: a sales table    region: a region    max_price: a number

def cheap_in_region(df, region, max_price):
    pass  # your code here


# ─── 8 · FIX · laptops_or_monitors ──────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match
#   Should give back the order_ids of every Laptop or Monitor order. It crashes: fix it.

def laptops_or_monitors(df):
    return df[(df["product"] == "Laptop") or (df["product"] == "Monitor")]["order_id"].tolist()


if __name__ == "__main__":
    import check
    check.level(globals())
