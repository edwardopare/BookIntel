from scraper import run_scraper
from db import save_data

def main():
    #run the scrapper
    data = run_scraper()
    print(f"Scraper returned {len(data)} items.")
    if data:
        print(f"First item keys: {list(data[0].keys())}")
    # save the data
    save_data(data, table_name="books_table", if_exists="replace")
    
    
if __name__ == "__main__":
    main()
    
    