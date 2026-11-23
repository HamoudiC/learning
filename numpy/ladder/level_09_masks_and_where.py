r"""LEVEL 9 · Masks: picking values that match, np.where, unique, missing values          (what comes next)
Run:  python ladder\level_09_masks_and_where.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · keeping the values that match ─────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks), counting and checking;  03_maths_and_aggregations.txt → maths on every value

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#   1a. Only the even values.
# your code here

#   1b. Only the values bigger than 5.
# your code here

#   1c. Only the values from 3 to 6 (3 and 6 included).
# your code here

#   1d. How many values are odd.
# your code here


# ─── 2 · DO · choosing per value ────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → choosing per value

marks = np.array([45, 80, 62, 91, 38])

#   2a. "pass" or "fail" for each mark (pass is 50 or more).
# your code here

#   2b. A new array where every mark below 50 is raised to 50 and the others stay the same.
# your code here

#   2c. The positions of the marks above 60.
# your code here


# ─── 3 · DO · unique values ─────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → unique values

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])

#   3a. Each name once, in alphabetical order.
# your code here

#   3b. How many times each name appears (in the same order as 3a).
# your code here

#   3c. Whether each name is "Bob" or "Will" (True / False for each).
# your code here


# ─── 4 · DO · missing values ────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → missing values, counting and checking, keeping the values that match (masks)

temps = np.array([18.5, np.nan, 22.0, 25.5, np.nan, 19.0])

#   4a. How many readings are missing.
# your code here

#   4b. The average of the real readings.
# your code here

#   4c. Only the real readings.
# your code here


# ─── 5 · WRITE · passing ────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks)
#   Gives back only the marks that are pass_mark or more, in their order.
#   marks: a 1D array    pass_mark: a number

def passing(marks, pass_mark):
    pass  # your code here


# ─── 6 · WRITE · letter_grades ──────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → choosing per value
#   Gives back a text array: "A" for 80 or more, "B" for 60 to 79, "F" below 60. No loop.
#   marks: a 1D array of marks 0-100

def letter_grades(marks):
    pass  # your code here


# ─── 7 · WRITE · fill_missing ───────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → missing values, choosing per value
#   Gives back a NEW array where every nan is replaced by the average of the real readings.
#   readings: a 1D float array with some np.nan in it

def fill_missing(readings):
    pass  # your code here


# ─── 8 · WRITE · most_common ────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → unique values;  03_maths_and_aggregations.txt → one number from many
#   Gives back the value that appears most often (on a tie: the smallest, or first alphabetically).
#   values: a 1D array, not empty

def most_common(values):
    pass  # your code here


# ─── 9 · FIX · in_range ─────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks)
#   Should give back the values from low to high (both included). It crashes: fix it.

def in_range(arr, low, high):
    return arr[arr >= low and arr <= high]


if __name__ == "__main__":
    import check
    check.level(globals())
