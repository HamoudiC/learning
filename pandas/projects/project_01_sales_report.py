r"""PROJECT 1 · Sales report          (levels 1-7)
Turn data/sales.csv into the numbers a manager asks for.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_01_sales_report.py
"""
# ── your setup lines go here ──



SALES = pd.read_csv(DATA / "sales.csv")


# ─── 1 · WRITE · add_revenue ────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns
#   Gives back a NEW table with a "revenue" column = units × price.
#   df: a sales table

def add_revenue(df):
    pass  # your code here


# ─── 2 · WRITE · totals_by ──────────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  01_series_and_dataframes.txt → back to plain Python
#   Gives back {value: total revenue} for one column, like region or product.
#   df: a sales table    column: the column to group by

def totals_by(df, column):
    pass  # your code here


# ─── 3 · WRITE · top_products ───────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  03_selecting_and_changing.txt → sorting
#   Gives back a list of the n products with the most revenue, best first.
#   df: a sales table    n: how many

def top_products(df, n):
    pass  # your code here


# ─── 4 · WRITE · month_totals ───────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  05_grouping_and_combining.txt → one answer per group
#   Gives back {"YYYY-MM": total revenue} for each month.
#   df: a sales table (dates as text)

def month_totals(df):
    pass  # your code here


# ─── 5 · WRITE · region_report ──────────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → one answer per group;  03_selecting_and_changing.txt → sorting
#   Gives back one row per region: region, orders, units, revenue, highest revenue first.
#   df: a sales table

def region_report(df):
    pass  # your code here


# ─── 6 · WRITE · save_report ────────────────────────────────────────────────────────────────────────
#   Bags: 02_files.txt → finding files, saving
#   Saves the region report as a CSV in the out folder (no row labels) and gives back its path.
#   df: a sales table    file_name: like "report.csv"

def save_report(df, file_name):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
