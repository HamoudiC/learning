r"""PROJECT 8 · k-nearest neighbours: a classifier from scratch          (levels 1-10)
To label a new point: find the k closest training points and take their most common label.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_08_knn_classifier.py
"""
# ── your import line goes here ──



TRAIN = [[1, 1], [1, 2], [2, 1], [6, 6], [6, 7], [7, 6]]
LABELS = ["red", "red", "red", "blue", "blue", "blue"]


# ─── 1 · WRITE · distances ──────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, shapes that fit together (broadcasting), maths functions, per row or per column (axis)
#   Gives back the distance from point to every training point (no loop).
#   train: 2D array, one point per row    point: one point

def distances(train, point):
    pass  # your code here


# ─── 2 · WRITE · nearest ────────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → sorting;  02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back the row numbers of the k closest training points, closest first (ties: lower row first).
#   train, point: as above    k: how many

def nearest(train, point, k):
    pass  # your code here


# ─── 3 · WRITE · classify ───────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → picking and changing;  04_masks_sorting_joining.txt → unique values;  03_maths_and_aggregations.txt → one number from many
#   Gives back the most common label among the k nearest points.
#   train, point, k: as above    labels: one label per training row

def classify(train, labels, point, k):
    pass  # your code here


# ─── 4 · WRITE · accuracy ───────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks), counting and checking
#   Gives back the fraction of positions where predicted and actual match.
#   predicted, actual: 1D arrays, same length

def accuracy(predicted, actual):
    pass  # your code here


# ─── 5 · WRITE · leave_one_out ──────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → picking and changing;  01_arrays_and_shape.txt → making arrays;  00_python_basics.txt → loops, lists, tuples, dicts
#   Gives back the accuracy when each training point is classified using all the OTHER points.
#   train, labels, k: as above

def leave_one_out(train, labels, k):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
