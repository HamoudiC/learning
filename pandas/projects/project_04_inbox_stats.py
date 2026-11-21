r"""PROJECT 4 · Inbox statistics          (levels 1-9)
data/emails.csv is a small inbox: when each email came, who sent it, the subject and its size.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_04_inbox_stats.py
"""
# ── your setup lines go here ──



EMAILS = pd.read_csv(DATA / "emails.csv")


# ─── 1 · WRITE · emails_per_sender ──────────────────────────────────────────────────────────────────
#   Bags: 05_grouping_and_combining.txt → counting;  01_series_and_dataframes.txt → back to plain Python
#   Gives back {sender: how many emails}, most first.
#   df: an emails table

def emails_per_sender(df):
    pass  # your code here


# ─── 2 · WRITE · busiest_hour ───────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  05_grouping_and_combining.txt → counting
#   Gives back the hour of the day (0-23) when the most emails arrived.
#   df: an emails table (the "sent" column is text)

def busiest_hour(df):
    pass  # your code here


# ─── 3 · WRITE · search ─────────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str);  03_selecting_and_changing.txt → keeping the rows that match
#   Gives back the subjects that contain word, upper or lower case.
#   df: an emails table    word: the word to look for

def search(df, word):
    pass  # your code here


# ─── 4 · WRITE · domain_counts ──────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str);  05_grouping_and_combining.txt → counting
#   Gives back {domain (the part after @): how many emails}.
#   df: an emails table

def domain_counts(df):
    pass  # your code here


# ─── 5 · WRITE · biggest ────────────────────────────────────────────────────────────────────────────
#   Bags: 03_selecting_and_changing.txt → sorting;  01_series_and_dataframes.txt → back to plain Python
#   Gives back the subjects of the n biggest emails, biggest first.
#   df: an emails table    n: how many

def biggest(df, n):
    pass  # your code here


# ─── 6 · WRITE · per_day ────────────────────────────────────────────────────────────────────────────
#   Bags: 06_dates_and_reshaping.txt → real dates;  05_grouping_and_combining.txt → one answer per group
#   Gives back {"YYYY-MM-DD": how many emails that day}.
#   df: an emails table

def per_day(df):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
