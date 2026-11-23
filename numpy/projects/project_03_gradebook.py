r"""PROJECT 3 · Gradebook          (levels 1-9)
Marks: one row per student, one column per test.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_03_gradebook.py
"""
# ── your import line goes here ──



NAMES = ["Ali", "Sara", "Omar", "Lina"]
MARKS = [[70, 80, 90],
         [95, 88, 92],
         [40, 65, 55],
         [85, 45, 75]]


# ─── 1 · WRITE · averages ───────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays;  03_maths_and_aggregations.txt → per row or per column (axis)
#   Gives back (each student's average, each test's average).
#   marks: one row per student

def averages(marks):
    pass  # your code here


# ─── 2 · WRITE · top_student ────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis), one number from many
#   Gives back the name of the student with the highest average.
#   names: one name per row of marks    marks: one row per student

def top_student(names, marks):
    pass  # your code here


# ─── 3 · WRITE · failed_any ─────────────────────────────────────────────────────────────────────────
#   Bags: 04_masks_sorting_joining.txt → keeping the values that match (masks), counting and checking;  01_arrays_and_shape.txt → making arrays
#   Gives back a list of the students who scored below pass_mark on at least one test.
#   names, marks: as above    pass_mark: the lowest pass

def failed_any(names, marks, pass_mark):
    pass  # your code here


# ─── 4 · WRITE · curve ──────────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → maths on every value, one number from many, maths functions;  02_indexing_copies_dtypes.txt → dtypes
#   Gives back whole-number marks all moved by the same amount so the class average is target, kept in 0-100.
#   marks: one row per student    target: the average you want

def curve(marks, target):
    pass  # your code here


# ─── 5 · WRITE · report_card ────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis);  04_masks_sorting_joining.txt → choosing per value;  00_python_basics.txt → lists, tuples, dicts, loops
#   Gives back {name: letter}: "A" for an average of 85+, "B" 70-84, "C" 50-69, "F" below 50.
#   names, marks: as above

def report_card(names, marks):
    pass  # your code here


# ─── 6 · WRITE · rank_table ─────────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → per row or per column (axis);  04_masks_sorting_joining.txt → sorting;  02_indexing_copies_dtypes.txt → one value, and slices;  00_python_basics.txt → loops, numbers
#   Gives back a list of (place, name, average rounded to 1 decimal), best first.
#   names, marks: as above

def rank_table(names, marks):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
