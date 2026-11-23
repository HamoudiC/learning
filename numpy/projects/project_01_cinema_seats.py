r"""PROJECT 1 · Cinema seats          (only needs levels 1-5: your notebook)
Each value in the hall is a seat's ticket number. 0 means the seat is booked.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_01_cinema_seats.py
"""
import numpy as np


SEATS = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
HALL = np.array([[11, 12, 13, 14],
                 [21, 22, 23, 24],
                 [31, 32, 33, 34]])          # rows A, B, C


# ─── 1 · WRITE · make_hall ──────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays, changing the shape
#   Gives back the seats as a 2D array, per_row seats in each row.
#   seat_numbers: a plain list of numbers    per_row: seats in one row

def make_hall(seat_numbers, per_row):
    n = SEATS.copy()
    n = np.array([SEATS])
    n.reshape()

# ─── 2 · WRITE · seat_at ────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D;  00_python_basics.txt → text
#   Gives back the ticket number at a seat label like "B3".
#   hall: 2D array of seats    label: row letter + seat number (A = first row, 1 = first seat)

def seat_at(hall, label):
    pass  # your code here


# ─── 3 · WRITE · book ───────────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → same, view or copy, picking and changing;  00_python_basics.txt → text
#   Gives back a NEW hall with that seat set to 0. The hall you're given must not change.
#   hall: 2D array of seats    label: like "B3"

def book(hall, label):
    pass  # your code here


# ─── 4 · WRITE · free_in_row ────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D;  00_python_basics.txt → text, loops, checks
#   Gives back how many seats in that row are not booked (not 0).
#   hall: 2D array of seats    letter: a row letter like "A"

def free_in_row(hall, letter):
    pass  # your code here


# ─── 5 · WRITE · aisle_seats ────────────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → 2D and 3D
#   Gives back (the first seat of every row, the last seat of every row).
#   hall: 2D array of seats

def aisle_seats(hall):
    pass  # your code here


# ─── 6 · WRITE · seat_labels ────────────────────────────────────────────────────────────────────────
#   Bags: 01_arrays_and_shape.txt → making arrays, changing the shape;  00_python_basics.txt → text, lists, tuples, dicts, loops
#   Gives back a 2D text array of labels: "A1", "A2", ... in row A, "B1", ... in row B.
#   rows: how many rows    per_row: seats in each row

def seat_labels(rows, per_row):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
