import pandas as pd 
from db import load_from_db, save_data

def data_cleaning():
    # Load data
    df = load_from_db()
    print(df.head(10))
    
    if __name__ == "__main__":
        data_cleaning()
    
    # # clean data
    # df = df.dropna()  # Remove rows with missing values
    # df["id"] = df.index + 1  
    # df["price"] = df["price"].str.replace("£", "").astype(float)  # Convert price to float
    # df["stock"] = df["stock"].str.contains("In stock")  # Convert stock availability to boolean
    
    # # Save cleaned data back to the database
    # save_data(df, table_name="cleaned_books_table", if_exists="replace")

