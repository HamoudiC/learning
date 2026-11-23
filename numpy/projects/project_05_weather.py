r"""PROJECT 5 · Weather station          (levels 1-11)
One temperature per day. When the sensor failed, the reading is np.nan.
Write your setup lines at the top (the imports, and DATA = the data folder). Then write each function: delete  pass  and write your code.
Run:  python projects\project_05_weather.py
"""
# ── your setup lines go here ──



# ─── 1 · WRITE · clean ──────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → missing values, choosing per value;  02_indexing_copies_dtypes.txt → dtypes
#   Gives back a NEW array: every nan replaced by the average of the real readings, rounded to 1 decimal.
#   temps: a 1D float array with some np.nan

def clean(temps):
    pass  # your code here


# ─── 2 · WRITE · moving_average ─────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value;  02_indexing_copies_dtypes.txt → one value, and slices, dtypes
#   Gives back the average of each run of `window` days in a row: days 0-1, then 1-2, ...
#   values: a 1D array    window: how many days in each average

def moving_average(values, window):
    pass  # your code here


# ─── 3 · WRITE · hottest_week ───────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → changing the shape;  03_maths_and_aggregations.txt → per row or per column (axis), one number from many;  00_python_basics.txt → lists, tuples, dicts
#   Gives back (week number, that week's average) for the week with the highest average. Week 0 first.
#   daily: a 1D array, its length a multiple of 7

def hottest_week(daily):
    pass  # your code here


# ─── 4 · WRITE · longest_streak ─────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops, numbers, checks
#   Gives back the most days IN A ROW that were above threshold.
#   values: a 1D array    threshold: a number

def longest_streak(values, threshold):
    pass  # your code here


# ─── 5 · WRITE · summary ────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → missing values, counting and checking;  01_arrays_and_shape.txt → size and shape;  00_python_basics.txt → lists, tuples, dicts, numbers
#   Gives back {"days", "missing", "min", "max", "mean"} of the real readings (mean rounded to 2).
#   temps: a 1D float array, maybe with nan

def summary(temps):
    pass  # your code here


# ─── 6 · WRITE · load_station ───────────────────────────────────────────────────────────────────────
#   Bags: 05_linear_algebra_and_files.txt → files;  02_indexing_copies_dtypes.txt → 2D and 3D
#   Gives back the temp column of a CSV in DATA (header "day,temp"; empty cells become nan).
#   file_name: like "station.csv"

def load_station(file_name):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
