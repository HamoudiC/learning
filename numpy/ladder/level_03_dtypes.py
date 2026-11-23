r"""LEVEL 3 · dtypes: what kind of values an array holds          (your notebook)
Run:  python ladder\level_03_dtypes.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · what kind of values ───────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes

whole = np.array([1, 2, 3])
decimals = np.array([1.5, 2.0])
flags = np.array([True, False])
names = np.array(["Bob", "Joe", "Will"])

#   1a. The dtype of whole.
# your code here

#   1b. The dtype of names.
# your code here

#   1c. The one-letter kind of decimals' dtype.
# your code here

#   1d. The one-letter kind of flags' dtype.
# your code here


# ─── 2 · DO · converting ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes

prices = np.array([1.1, 2.9, -1.9])
codes = np.array(["10", "20", "30"])
switches = np.array([0, 2, 0])

#   2a. prices as whole numbers, with the decimals cut off.
# your code here

#   2b. prices rounded to the nearest whole number, stored as ints.
# your code here

#   2c. codes as ints (so you could add them up).
# your code here

#   2d. switches as True / False values.
# your code here


# ─── 3 · DO · choosing the dtype when you make it ───────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes

numbers = [1, 2, 3]

#   3a. An array of numbers, stored as decimals (floats) from the start.
# your code here

#   3b. An array of numbers, stored as bytes (dtype 'S').
# your code here


# ─── 4 · WRITE · to_whole ───────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes
#   Gives back a NEW int array: each value ROUNDED to the nearest whole number (not cut off).
#   arr: an array of decimals

def to_whole(arr):
    pass  # your code here


# ─── 5 · WRITE · is_text ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes;  00_python_basics.txt → checks
#   Gives back True if the array holds text, False if not.
#   arr: any array

def is_text(arr):
    pass  # your code here


# ─── 6 · WRITE · parse_numbers ──────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes;  01_arrays_and_shape.txt → making arrays
#   Gives back an int array of the numbers in the text.
#   text: numbers separated by commas, like "3,10,7"

def parse_numbers(text):
    pass  # your code here


# ─── 7 · FIX · average_price ────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → dtypes;  03_maths_and_aggregations.txt → one number from many
#   Should give back the average of a list of prices. It crashes: fix it.

def average_price(prices):
    arr = np.array(prices + ["total"])
    return arr[:-1].mean()


if __name__ == "__main__":
    import check
    check.level(globals())
