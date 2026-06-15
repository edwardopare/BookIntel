# view_db.py
from db import load_from_db
import pandas as pd

# Set display options to see all columns clearly
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Load data
df = load_from_db("books_table")

# Display first 10 rows
if not df.empty:
    print("\n--- First 10 Rows of books_table ---")
    print(df.head(10))
    print(f"\nTotal rows in DB: {len(df)}")
else:
    print("No data found.")   