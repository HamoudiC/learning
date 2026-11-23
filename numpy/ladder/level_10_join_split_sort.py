r"""LEVEL 10 · Joining, splitting, sorting          (what comes next)
Run:  python ladder\level_10_join_split_sort.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · joining ───────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → joining and splitting

a = np.array([1, 2])
b = np.array([3, 4])

#   1a. a and then b, in one row.
# your code here

#   1b. a on top of b (2 rows).
# your code here

#   1c. a and b as two columns.
# your code here


# ─── 2 · DO · splitting ─────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → joining and splitting

days = np.arange(14)

#   2a. days cut into 2 equal weeks (a list of 2 arrays).
# your code here

#   2b. days cut just before position 3 and just before position 10 (a list of 3 arrays).
# your code here


# ─── 3 · DO · sorting ───────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → sorting;  02_indexing_copies_dtypes.txt → one value, and slices;  03_maths_and_aggregations.txt → one number from many

scores = np.array([72, 95, 60, 88])
people = np.array(["Ali", "Sara", "Omar", "Lina"])

#   3a. scores sorted, smallest first (scores itself must not change).
# your code here

#   3b. scores sorted, biggest first.
# your code here

#   3c. people in order of their score, lowest first.
# your code here

#   3d. The name of the person with the top score.
# your code here


# ─── 4 · WRITE · join_classes ───────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → joining and splitting
#   Gives back one table: class_a's rows, then class_b's rows.
#   class_a, class_b: 2D score tables with the same number of columns

def join_classes(class_a, class_b):
    pass  # your code here


# ─── 5 · WRITE · ranking ────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → sorting;  02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back the names in order of score, HIGHEST first.
#   names: a 1D text array    scores: numbers, the same length (no ties)

def ranking(names, scores):
    pass  # your code here


# ─── 6 · WRITE · top_n ──────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → sorting;  02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back the n biggest values, biggest first. The array you're given must not change.
#   values: a 1D array    n: how many

VALUES = np.array([5, 1, 9, 3, 7])

def top_n(values, n):
    pass  # your code here


# ─── 7 · WRITE · into_weeks ─────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → joining and splitting;  00_python_basics.txt → lists, tuples, dicts, numbers
#   Gives back a list of arrays, one per week (7 values in each).
#   days: a 1D array, its length a multiple of 7

def into_weeks(days):
    pass  # your code here


# ─── 8 · FIX · sorted_copy ──────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → sorting
#   Should give back a sorted copy and leave the array alone. It does neither: fix it.

AGES = np.array([40, 18, 25])

def sorted_copy(arr):
    return arr.sort()


if __name__ == "__main__":
    import check
    check.level(globals())
