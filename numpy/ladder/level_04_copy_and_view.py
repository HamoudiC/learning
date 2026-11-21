r"""LEVEL 4 · Same array, view, or copy?          (your notebook + what comes next)
Run:  python ladder\level_04_copy_and_view.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np


# ─── 1 · DO · does it share? ────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy;  picking and changing

nums = np.array([10, 20, 30, 40, 50])

#   1a. Whether a copy of nums shares memory with nums (True or False).
# your code here

#   1b. Whether a view of nums shares memory with nums.
# your code here

#   1c. Whether the slice of nums from position 1 to 3 shares memory with nums.
# your code here

#   1d. Whether nums picked at the positions [0, 4] shares memory with nums.
# your code here


# ─── 2 · DO · who changes? ──────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy;  picking and changing

temps = np.array([20, 21, 22, 23])
backup = np.array([1, 2, 3])

#   2a. Make a view of temps, set the view's first value to 99, then give back temps.
# your code here

#   2b. Make a copy of backup, set the copy's first value to 0, then give back backup.
# your code here

#   2c. Take the slice of temps from position 1 to the end, set that slice's first value to -1, then give back temps.
# your code here


# ─── 3 · WRITE · with_first_zeroed ──────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy;  picking and changing
#   Gives back a NEW array like arr with its first value set to 0. The array you're given must not change.
#   arr: a 1D array

DATA = np.array([5, 6, 7])

def with_first_zeroed(arr):
    pass  # your code here


# ─── 4 · WRITE · capped ─────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy;  03_maths_and_aggregations.txt → maths functions
#   Gives back a NEW array where every value above top becomes top. The array you're given must not change.
#   arr: a 1D array    top: a number

MARKS = np.array([1, 9, 3])

def capped(arr, top):
    pass  # your code here


# ─── 5 · FIX · normalised ───────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy
#   Should give back a NEW array: each value divided by the biggest, without changing the array it's given.
#   It changes it: fix it.

PRICES = np.array([2.0, 4.0, 1.0])

def normalised(arr):
    result = arr
    result /= arr.max()
    return result


if __name__ == "__main__":
    import check
    check.level(globals())
