r"""PROJECT 9 · A moving-average backtest on gold prices          (levels 1-10)
The core of your Gold Strategy Lab: returns, moving averages, a crossover signal, and how it would have done.
A backtest, not an auto-trader.
Write your import line at the top. Then write each function: delete  pass  and write your code.
Run:  python projects\project_09_gold_backtest.py
"""
# ── your import line goes here ──



PRICES = [100.0, 102.0, 101.0, 105.0, 107.0, 104.0, 108.0, 110.0]      # 8 daily closing prices


# ─── 1 · WRITE · daily_returns ──────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value;  02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back each day's return: (today - yesterday) / yesterday. One shorter than prices.
#   prices: a 1D float array

def daily_returns(prices):
    pass  # your code here


# ─── 2 · WRITE · moving_average ─────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value;  02_indexing_copies_dtypes.txt → one value, and slices, dtypes
#   Gives back the average of each run of `window` prices in a row.
#   prices: a 1D float array    window: how many days

def moving_average(prices, window):
    pass  # your code here


# ─── 3 · WRITE · crossover_signals ──────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices, dtypes;  03_maths_and_aggregations.txt → maths on every value
#   Gives back 1 on each day the fast average is above the slow one, else 0 (from day slow-1 on).
#   prices: a 1D float array    fast, slow: window lengths, fast < slow

def crossover_signals(prices, fast, slow):
    pass  # your code here


# ─── 4 · WRITE · strategy_returns ───────────────────────────────────────────────────────────────────
#   Bags: 02_indexing_copies_dtypes.txt → one value, and slices;  03_maths_and_aggregations.txt → maths on every value
#   Gives back signal × the NEXT day's return for every signal but the last (no looking ahead).
#   prices, fast, slow: as above

def strategy_returns(prices, fast, slow):
    pass  # your code here


# ─── 5 · WRITE · equity_curve ───────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value
#   Gives back the money after each day: start × (1 + r1) × (1 + r2) × ...
#   returns: daily returns (0.1 = +10%)    start: the money at the beginning

def equity_curve(returns, start):
    pass  # your code here


# ─── 6 · WRITE · max_drawdown ───────────────────────────────────────────────────────────────────────
#   Bags: 03_maths_and_aggregations.txt → running totals, maths on every value, one number from many
#   Gives back the worst fall from a previous high, as a fraction (0.25 = 25%).
#   equity: money over time

def max_drawdown(equity):
    pass  # your code here


# ─── 7 · WRITE · report ─────────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → lists, tuples, dicts, numbers;  02_indexing_copies_dtypes.txt → one value, and slices
#   Gives back {"strategy_return", "buy_and_hold", "max_drawdown"}, each rounded to 4 decimals.
#   buy_and_hold = last price / the price on day slow-1, minus 1.
#   prices, fast, slow: as above    start: the starting money

def report(prices, fast, slow, start):
    pass  # your code here


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
