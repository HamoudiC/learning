r"""LEVEL 7 · Maths on whole arrays and broadcasting          (what comes next)
Run:  python ladder\level_07_maths_and_broadcasting.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · maths on every value ──────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value

prices = np.array([7, 8, 9])

#   1a. prices with 7 taken off each one.
# your code here

#   1b. Each price squared.
# your code here

#   1c. Each price divided by 2.
# your code here

#   1d. Each price divided by 2, with the decimals dropped.
# your code here

#   1e. Whether each price is more than 7 (True / False for each).
# your code here


# ─── 2 · DO · maths functions ───────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths functions

values = np.array([1, 16, 25])
signed = np.array([-3, 0, 3])
marks = np.array([-5, 5, 15])

#   2a. The square root of each value.
# your code here

#   2b. signed without any minus signs.
# your code here

#   2c. marks squashed so nothing is below 0 or above 10.
# your code here


# ─── 3 · DO · different shapes together ─────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → shapes that fit together (broadcasting)

table = np.array([[1, 2, 3], [4, 5, 6]])
per_column = np.array([10, 20, 30])
per_row = np.array([[100], [200]])
counts = np.array([1, 2, 3])

#   3a. table with per_column added to every row.
# your code here

#   3b. table with per_row added to every column.
# your code here

#   3c. A 3 × 3 times table: counts as a column multiplied by counts as a row.
# your code here


# ─── 4 · WRITE · celsius_to_fahrenheit ──────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value
#   Gives back the temperatures in °F, the same shape:  F = C × 9 / 5 + 32.
#   temps: an array of °C

def celsius_to_fahrenheit(temps):
    pass  # your code here


# ─── 5 · WRITE · distances_from ─────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → shapes that fit together, maths functions, per row or per column
#   Gives back the straight-line distance from each point to centre, without a loop.
#   points: shape (n, 2), one (x, y) per row    centre: one point (x, y)

def distances_from(points, centre):
    pass  # your code here


# ─── 6 · WRITE · multiplication_grid ────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → shapes that fit together;  01_arrays_and_shape.txt → ready-made arrays
#   Gives back an n × n times table: row i, column j holds (i + 1) × (j + 1). No loop.
#   n: a whole number

def multiplication_grid(n):
    pass  # your code here


# ─── 7 · WRITE · scale_to_unit ──────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many
#   Gives back the values squashed into 0..1:  (value - smallest) / (biggest - smallest).
#   values: a 1D array (not all the same)

def scale_to_unit(values):
    pass  # your code here


# ─── 8 · FIX · square_roots ─────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths functions
#   Should give back the square root of every value in the array. It crashes: fix it.

import math

def square_roots(arr):
    return math.sqrt(arr)


if __name__ == "__main__":
    import check
    check.level(globals())
