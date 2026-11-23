r"""LEVEL 6 · Cleaning: missing values, text, duplicates
Run:  python ladder\level_06_cleaning.py
Under each task, delete  # your code here  and write your code. Functions: delete  pass  and write your code.
Open data/contacts_messy.csv in VS Code and look at it before you start.
"""
import numpy as np
import pandas as pd
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"


# ─── 1 · DO · missing values ────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → missing values

contacts = pd.read_csv(DATA / "contacts_messy.csv")

#   1a. How many values are missing in each column.
# your code here

#   1b. Only the rows with nothing missing.
# your code here

#   1c. Only the rows that have an email.
# your code here

#   1d. The city column with every missing city written as "unknown".
# your code here


# ─── 2 · DO · text ──────────────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str)

contacts = pd.read_csv(DATA / "contacts_messy.csv")

#   2a. The names with the spaces at both ends removed.
# your code here

#   2b. The names with the spaces removed and Each Word Capitalised.
# your code here

#   2c. The emails in lowercase.
# your code here

#   2d. The phone numbers with only their digits left.
# your code here

#   2e. The part of each email before the @.
# your code here


# ─── 3 · DO · duplicates and numbers ────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → duplicates, text that should be numbers, text in a column (.str)

contacts = pd.read_csv(DATA / "contacts_messy.csv")
amounts = pd.Series(["12", "x", "3.5"])

#   3a. True / False for each contact: does its email (in lowercase) repeat an earlier one?
# your code here

#   3b. amounts as numbers, with the ones that aren't numbers missing.
# your code here


# ─── 4 · WRITE · missing_report ─────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → missing values;  01_series_and_dataframes.txt → maths and filtering, back to plain Python
#   Gives back a dict {column: how many missing}, only for the columns with at least 1 missing.
#   df: any table

def missing_report(df):
    pass  # your code here


# ─── 5 · WRITE · clean_names ────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str)
#   Gives back the names with the spaces trimmed and Each Word Capitalised.
#   names: a Series of names

def clean_names(names):
    pass  # your code here


# ─── 6 · WRITE · clean_phones ───────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str), missing values;  01_series_and_dataframes.txt → back to plain Python
#   Gives back a plain list of the phones as digits only; a missing phone becomes "".
#   phones: a Series of phone numbers

def clean_phones(phones):
    pass  # your code here


# ─── 7 · WRITE · unique_people ──────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str), duplicates, missing values;  03_selecting_and_changing.txt → keeping the rows that match, new and changed columns
#   Gives back the contacts with emails in lowercase and only the first row for each email kept
#   (rows with no email are all kept), numbered 0, 1, 2...
#   df: a contacts table

def unique_people(df):
    pass  # your code here


# ─── 8 · FIX · fill_cities ──────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → missing values
#   Should give back a table where every missing city is "unknown". The cities stay missing: fix it.

def fill_cities(df):
    result = df.copy()
    result["city"].fillna("unknown")
    return result


if __name__ == "__main__":
    import check
    check.level(globals())
