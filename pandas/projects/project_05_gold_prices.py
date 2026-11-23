r"""PROJECT 5 · Gold prices with pandas          (levels 1-9)
60 days of daily gold prices (data/gold_daily.csv). The same ideas as the numpy backtest, the pandas way:
dates as the index, rolling averages, resampling, and shift() so nothing looks ahead.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_05_gold_prices.py
"""
# ── your setup lines go here ──



GOLD = pd.read_csv(DATA / "gold_daily.csv", parse_dates=["Date"], index_col="Date")


# ─── 1 · WRITE · add_returns ────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time;  03_selecting_and_changing.txt → new and changed columns
#   Gives back a NEW table with a "Return" column: each day's % change of Close.
#   df: a gold table

def add_returns(df):
    pass  # your code here


# ─── 2 · WRITE · best_and_worst_day ─────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time, real dates;  01_series_and_dataframes.txt → maths and filtering;  00_python_basics.txt → lists, tuples, dicts
#   Gives back ("YYYY-MM-DD" of the biggest daily rise, "YYYY-MM-DD" of the biggest daily fall).
#   df: a gold table

def best_and_worst_day(df):
    pass  # your code here


# ─── 3 · WRITE · weekly_close ───────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → dates as the row labels
#   Gives back the last Close of each week (a Series).
#   df: a gold table

def weekly_close(df):
    pass  # your code here


# ─── 4 · WRITE · monthly_range ──────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → dates as the row labels, real dates;  05_grouping_and_combining.txt → one answer per group
#   Gives back one row per month ("YYYY-MM" labels) with the month's highest High and lowest Low.
#   df: a gold table

def monthly_range(df):
    pass  # your code here


# ─── 5 · WRITE · add_signals ────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time;  03_selecting_and_changing.txt → new and changed columns, renaming, dropping, types
#   Gives back a NEW table with fast_ma, slow_ma (rolling means of Close) and signal (1 if fast > slow, else 0).
#   df: a gold table    fast, slow: window lengths

def add_signals(df, fast, slow):
    pass  # your code here


# ─── 6 · WRITE · backtest ───────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time;  01_series_and_dataframes.txt → label or position, maths and filtering;  00_python_basics.txt → lists, tuples, dicts, numbers
#   Gives back {"strategy", "buy_and_hold", "days_in_market"} from day `slow` on: the strategy earns each
#   day's return only if YESTERDAY's signal was 1 (shift(1)). Returns rounded to 4.
#   df: a gold table    fast, slow: window lengths

def backtest(df, fast, slow):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
