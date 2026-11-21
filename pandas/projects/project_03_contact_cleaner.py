r"""PROJECT 3 · Contact list cleaner          (levels 1-6)
Clean data/contacts_messy.csv step by step: tidy text, fix phones, remove duplicates, print cards.
Write your setup lines at the top (the imports, and DATA = the data folder).
Then write each function: delete  pass  and write your code.
Run:  python projects\project_03_contact_cleaner.py
"""
# ── your setup lines go here ──



CONTACTS = pd.read_csv(DATA / "contacts_messy.csv")


# ─── 1 · WRITE · tidy_text ──────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str), missing values;  03_selecting_and_changing.txt → new and changed columns
#   Gives back a NEW table: names Title Case, emails lowercase, cities Title Case, missing city "Unknown"
#   (all with spaces trimmed).
#   df: a contacts table

def tidy_text(df):
    pass  # your code here


# ─── 2 · WRITE · fix_phones ─────────────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → text in a column (.str), missing values
#   Gives back a NEW table with every phone as digits only ("" if missing).
#   df: a contacts table

def fix_phones(df):
    pass  # your code here


# ─── 3 · WRITE · remove_duplicates ──────────────────────────────────────────────────────────────────
#   Bags: 04_cleaning.txt → duplicates, missing values;  03_selecting_and_changing.txt → keeping the rows that match
#   Gives back only the first row for each email (rows with no email are kept), numbered 0, 1, 2...
#   df: a contacts table whose emails are already lowercase

def remove_duplicates(df):
    pass  # your code here


# ─── 4 · WRITE · clean_contacts ─────────────────────────────────────────────────────────────────────
#   Bags: your own three functions above
#   Gives back the fully cleaned table: tidy_text, then fix_phones, then remove_duplicates.
#   df: a contacts table

def clean_contacts(df):
    pass  # your code here


# ─── 5 · WRITE · contact_card ───────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → text;  04_cleaning.txt → missing values
#   Gives back one line of text for a person: "Name <email> phone", or "Name (no email) phone".
#   name, phone: strs    email: a str, or a missing value (NaN)

def contact_card(name, email, phone):
    pass  # your code here


# ─── 6 · WRITE · all_cards ──────────────────────────────────────────────────────────────────────────
#   Bags: 00_python_basics.txt → loops, lists;  01_series_and_dataframes.txt → columns, rows and cells
#   Gives back a list with one card per person in the cleaned table.
#   df: a contacts table (messy)

def all_cards(df):
    pass  # your code here


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "ladder"))
    import check
    check.level(globals())
