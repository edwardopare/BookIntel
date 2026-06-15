import sqlite3
import pandas as pd
from sqlalchemy import create_engine

DB_NAME = "books.db"

# db connection
def get_db_connection():
    return create_engine(f"sqlite:///{DB_NAME}")

# create table if not exists
def save_data(data,table_name="books_table",if_exists="replace"):
    df = pd.DataFrame(data)
    engine = get_db_connection()
    
    try:
        df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
        print("Data saved to database successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        engine.dispose()
        
# load data from db
def load_from_db(table_name="books_table"):
    conn = sqlite3.connect(DB_NAME)
    try:
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        return df
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()  
    finally:
        conn.close()
        