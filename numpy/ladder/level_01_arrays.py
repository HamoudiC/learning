r"""LEVEL 1 · Arrays: making them, ndim, shape, size          (your notebook)
Run it after every task, from the numpy folder:   python ladder\level_01_arrays.py

  DO     Under each task, delete  # your code here  and write your code on that line.
         Use the data above the tasks. Look things up in the bags named at the top of each section.
  WRITE  Write the function: delete  pass  and write your code.
  FIX    The function is broken. Fix it.
  ✅ done   ❌ not right yet   ⬜ not started
"""
import numpy as np


# ─── 1 · DO · making arrays ─────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays

ages = [19, 22, 20, 21]
point = (3, 4)
grid = [[1, 2, 3], [4, 5, 6]]

#   1a. Make an array from the list ages.
ages = np.array(ages)

#   1b. Make an array from the tuple point.
point = np.array(point)

#   1c. Make a 2D array from grid.
grid = np.array(grid)

#   1d. Turn your 2D array from 1c back into a plain list.
grid.tolist()


# ─── 2 · DO · how many dimensions ───────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays, size and shape

today = np.array(31)
week = np.array([30, 32, 29, 31, 33, 35, 34])
two_weeks = np.array([[30, 32, 29, 31, 33, 35, 34], [28, 27, 30, 31, 29, 30, 32]])

#   2a. How many dimensions week has.
week.ndim

#   2b. How many dimensions two_weeks has.
two_weeks.ndim

#   2c. How many dimensions today has.
today.ndim

#   2d. Make an array from week that has at least 3 dimensions.
week = np.array([30, 32, 29, 31, 33, 35, 34], ndmin=3)


# ─── 3 · DO · shape and size ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → size and shape

seats = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])

#   3a. The shape of seats.
seats.shape

#   3b. How many seats there are altogether.
seats.size

#   3c. How many rows of seats there are.
len(seats)

#   3d. How many seats are in each row.
seats.ndim


# ─── 4 · DO · maths on a whole array ────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value;  00_python_basics.txt → lists, tuples, dicts

prices = np.array([10, 20, 30])
discounts = np.array([1, 2, 3])
pair = [1, 2]

#   4a. Every price doubled.
for i in prices:
    i *= 2
prices

#   4b. Every price with 5 added.
# your code here

#   4c. Each price minus its own discount (the first minus the first, the second minus the second...).
# your code here

#   4d. The list pair repeated twice, still as a plain list.
# your code here


# ─── 5 · WRITE · describe ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → size and shape;  00_python_basics.txt → text
#   Gives back a sentence about an array, in this form:   <ndim>D array, shape <shape>, <size> values
#   arr: any array

def describe(arr):
    pass  # your code here


# ─── 6 · WRITE · doubled ────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays;  03_maths_and_aggregations.txt → maths on every value
#   Gives back an ARRAY with every number doubled (no loop).
#   numbers: a plain list of numbers

def doubled(numbers):
    pass  # your code here


# ─── 7 · FIX · add_bonus ────────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays;  03_maths_and_aggregations.txt → maths on every value
#   Should give back an array with bonus added to every mark. It crashes: fix it.
#   marks: a plain list of numbers    bonus: a number

def add_bonus(marks, bonus):
    return marks + bonus


if __name__ == "__main__":
    import check
    check.level(globals())
