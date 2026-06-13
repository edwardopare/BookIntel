import sqlite3
import pandas as pd

DB_NAME = "books.db"

# db connection
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

# create table if not exists
def save_data(data,table_name="books_table",if_exists="replace"):
    #convert data to dataframe
    df = pd.DataFrame(data)
    # save to database
    conn = get_db_connection()
    try:
        df.to_sql(table_name, conn, if_exists=if_exists, index=False)
        print("Data saved to database successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        