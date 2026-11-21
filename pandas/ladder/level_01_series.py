r"""LEVEL 1 · Series: one labelled column
Run it after every task, from the pandas folder:   python ladder\level_01_series.py

  DO     Under each task, delete  # your code here  and write your code on that line.
         Use the data above the tasks. Look things up in the bags named at the top of each section.
  WRITE  Write the function: delete  pass  and write your code.
  FIX    The function is broken. Fix it.
  ✅ done   ❌ not right yet   ⬜ not started
"""
import numpy as np
import pandas as pd


# ─── 1 · DO · making a Series ───────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → making a Series

points = [10, 20, 30]
labels = ["a", "b", "c"]
stock = {"tea": 2, "milk": 1}

#   1a. A Series of points.
# your code here

#   1b. A Series of points, labelled with labels and named "pts".
# your code here

#   1c. A Series made from the dict stock.
# your code here

#   1d. The labels of a Series made from stock, as a plain list.
# your code here


# ─── 2 · DO · label or position ─────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → label or position

s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="pts")

#   2a. The value labelled "b".
# your code here

#   2b. The first value, by its position.
# your code here

#   2c. The last value, by its position.
# your code here

#   2d. The values labelled "a" to "b" (both included).
# your code here

#   2e. The first two values, by position.
# your code here


# ─── 3 · DO · maths and filtering ───────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → maths and filtering

s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="pts")

#   3a. s with 1 added to every value.
# your code here

#   3b. Only the values over 15.
# your code here

#   3c. The total of s.
# your code here

#   3d. The label of the biggest value.
# your code here

#   3e. How many values are 20 or more.
# your code here


# ─── 4 · DO · lining up by label ────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → maths and filtering

shop_a = pd.Series([1, 2], index=["x", "y"])
shop_b = pd.Series([10, 20], index=["y", "x"])
shop_c = pd.Series([5], index=["z"])

#   4a. shop_a plus shop_b.
# your code here

#   4b. shop_a plus shop_c, counting a missing item as 0.
# your code here


# ─── 5 · WRITE · price_list ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → making a Series
#   Gives back a Series of the prices, labelled by item, named "price".
#   items: a list of names    prices: a list of prices, the same length

def price_list(items, prices):
    pass  # your code here


# ─── 6 · WRITE · over_budget ────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → maths and filtering, back to plain Python
#   Gives back a plain list of the items that cost more than budget.
#   prices: a Series labelled by item    budget: a number

def over_budget(prices, budget):
    pass  # your code here


# ─── 7 · WRITE · with_tax ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → maths and filtering
#   Gives back each price × (1 + rate), rounded to 2 decimals (same labels and name).
#   prices: a Series    rate: like 0.05 for 5%

def with_tax(prices, rate):
    pass  # your code here


# ─── 8 · WRITE · total_stock ────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → maths and filtering
#   Gives back the total of each item across both shops (an item missing from a shop counts as 0).
#   shop_a, shop_b: Series of stock labelled by item

def total_stock(shop_a, shop_b):
    pass  # your code here


# ─── 9 · FIX · first_price ──────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → label or position
#   Should give back the first price, whatever the labels are. It crashes: fix it.

def first_price(prices):
    return prices[0]


if __name__ == "__main__":
    import check
    check.level(globals())
