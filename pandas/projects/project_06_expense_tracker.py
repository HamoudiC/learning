r"""PROJECT 6 · Expense tracker          (levels 1-10)
Sort a bank statement (data/bank_statement.csv) into categories, then see where the money goes.
Spending is negative, income is positive.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_06_expense_tracker.py
"""
# ── your setup lines go here ──



STATEMENT = pd.read_csv(DATA / "bank_statement.csv")
CATEGORIES = {"groceries": ["CARREFOUR", "LULU"], "transport": ["ENOC"], "food delivery": ["TALABAT"],
              "bills": ["DEWA"], "subscriptions": ["NETFLIX", "SPOTIFY"], "income": ["SALARY"]}


# ─── 1 · WRITE · categorise ─────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops, text, checks
#   Gives back the category whose keyword appears in the description, or "other".
#   description: one statement line    categories: {category: [keywords]}

def categorise(description, categories):
    pass  # your code here


# ─── 2 · WRITE · add_categories ─────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → new and changed columns
#   Gives back a NEW table with a "category" column.
#   df: a statement    categories: as above

def add_categories(df, categories):
    pass  # your code here


# ─── 3 · WRITE · spending_by_category ───────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → keeping the rows that match;  05_grouping_and_combining.txt → one answer per group;  01_series_and_dataframes.txt → maths and filtering, back to plain Python
#   Gives back {category: total spent, as a positive number rounded to 2}. Income isn't spending.
#   df: a statement    categories: as above

def spending_by_category(df, categories):
    pass  # your code here


# ─── 4 · WRITE · monthly_summary ────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  05_grouping_and_combining.txt → one answer per group;  03_selecting_and_changing.txt → new and changed columns, keeping the rows that match;  01_series_and_dataframes.txt → maths and filtering
#   Gives back one row per month: month ("YYYY-MM"), income, spent (positive), saved (income - spent), rounded to 2.
#   df: a statement

def monthly_summary(df):
    pass  # your code here


# ─── 5 · WRITE · category_by_month ──────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → reshaping, real dates;  03_selecting_and_changing.txt → keeping the rows that match, new and changed columns;  01_series_and_dataframes.txt → maths and filtering
#   Gives back a table of spending: one row per category, one column per month (missing = 0), rounded to 2.
#   df: a statement    categories: as above

def category_by_month(df, categories):
    pass  # your code here


# ─── 6 · WRITE · over_budget ────────────────────────────────────────────────────────────────────────
#   Bags: 01_series_and_dataframes.txt → columns, rows and cells, back to plain Python;  00_python_basics.txt → loops, lists, tuples, dicts, checks
#   Gives back a sorted list of (month, category) where the spending was MORE than its budget.
#   df: a statement    categories: as above    budgets: {category: monthly limit}

def over_budget(df, categories, budgets):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
