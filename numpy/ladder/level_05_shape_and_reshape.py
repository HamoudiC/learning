r"""LEVEL 5 · Shape and reshape          (your notebook + what comes next)
Run:  python ladder\level_05_shape_and_reshape.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · reshape ───────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape, size and shape

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

#   1a. nums as 3 rows of 4.
# your code here

#   1b. nums as 2 blocks, each with 3 rows of 2.
# your code here

#   1c. nums as 6 rows, letting numpy work out how many columns.
# your code here

#   1d. The shape you get when nums is made into 4 columns (numpy works out the rows).
# your code here


# ─── 2 · DO · turn it, flatten it ───────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape

table = np.array([[1, 2, 3], [4, 5, 6]])

#   2a. table with its rows and columns swapped.
# your code here

#   2b. table as one flat row, as a copy.
# your code here

#   2c. table's values poured, in order, into 3 rows of 2 (NOT swapped).
# your code here


# ─── 3 · WRITE · as_rows ────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape
#   Gives back the values as a 2D array with per_row values in each row.
#   values: a 1D array    per_row: values in each row (it always divides evenly)

def as_rows(values, per_row):
    pass  # your code here


# ─── 4 · WRITE · fits ───────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → size and shape, changing the shape
#   Gives back True if arr could be reshaped to that shape, False if not. It must not crash.
#   arr: any array    shape: a tuple of ints, like (3, 4)

def fits(arr, shape):
    pass  # your code here


# ─── 5 · WRITE · swap_rows_and_columns ──────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape
#   Gives back the table with row i turned into column i.
#   table: a 2D array

def swap_rows_and_columns(table):
    pass  # your code here


# ─── 6 · FIX · weekly ───────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape
#   Should give back one ROW per week, 7 values in each row. The rows come out wrong: fix it.
#   days: a 1D array, its length a multiple of 7

def weekly(days):
    return days.reshape(7, -1)


if __name__ == "__main__":
    import check
    check.level(globals())
