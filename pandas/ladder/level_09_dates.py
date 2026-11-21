r"""LEVEL 9 · Dates and time series
Run:  python ladder\level_09_dates.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · parts of dates ────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates

sales = pd.read_csv(DATA / "sales.csv", parse_dates=["date"])

#   1a. The month (a number) of each order.
# your code here

#   1b. The weekday name of each order.
# your code here

#   1c. How many days there are between the first and the last order.
# your code here


# ─── 2 · DO · per month, per period ─────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → dates as the row labels

sales = pd.read_csv(DATA / "sales.csv", parse_dates=["date"])
gold = pd.read_csv(DATA / "gold_daily.csv", parse_dates=["Date"], index_col="Date")

#   2a. The total units of each month (one value per month).
# your code here

#   2b. The gold rows from February 2026.
# your code here


# ─── 3 · DO · over time ─────────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time

gold = pd.read_csv(DATA / "gold_daily.csv", parse_dates=["Date"], index_col="Date")

#   3a. The Close column moved down one day (each day shows yesterday's close).
# your code here

#   3b. The day-to-day change of Close, as a fraction.
# your code here

#   3c. The average Close of each 3 days in a row.
# your code here


# ─── 4 · WRITE · monthly_revenue ────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates, dates as the row labels;  05_grouping_and_combining.txt → one answer per group
#   Gives back a plain list of the total revenue (units × price) of each month, in order.
#   df: a sales table with real dates

def monthly_revenue(df):
    pass  # your code here


# ─── 5 · WRITE · orders_per_weekday ─────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  05_grouping_and_combining.txt → counting
#   Gives back a dict {weekday name: how many orders}.
#   df: a sales table with real dates

def orders_per_weekday(df):
    pass  # your code here


# ─── 6 · WRITE · daily_returns ──────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time;  04_cleaning.txt → missing values
#   Gives back each day's change of Close as a fraction, rounded to 4, without the first (empty) day.
#   prices: a gold table with a Close column

def daily_returns(prices):
    pass  # your code here


# ─── 7 · WRITE · above_average_days ─────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → over time;  03_selecting_and_changing.txt → keeping the rows that match
#   Gives back how many days closed ABOVE their own `window`-day rolling average.
#   prices: a gold table with a Close column    window: how many days in the average

def above_average_days(prices, window):
    pass  # your code here


# ─── 8 · FIX · send_hours ───────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  02_files.txt → reading
#   Should give back a plain list of the hour each email was sent. It crashes: fix it.

def send_hours(path):
    emails = pd.read_csv(path)
    return emails["sent"].dt.hour.tolist()


if __name__ == "__main__":
    import check
    check.level(globals())
