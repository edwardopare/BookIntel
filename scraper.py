import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv
from urllib.parse import urljoin  
from db import save_data

def scrape_book_data(url):
    book = requests.get(url)
    if book.status_code != 200:
        return []
    
    soup = BeautifulSoup(book.content, "html.parser")
    items = soup.find_all("article", class_="product_pod")
    items_data = []

    for item in items:
        try:
            # link 
            link = item.find("h3").find("a")["href"]
            
            # title
            title = item.find("h3").find("a")["title"]
            
            # price
            price_tag = item.find("p", class_="price_color")
            price = price_tag.text.strip() if price_tag else "N/A"
            
            # stock
            stock_tag = item.find("p", class_="instock availability")
            stock = stock_tag.text.strip() if stock_tag else "Unknown"
            
            # rating
            rating_tag = item.find("p", class_="star-rating")
            # Ensure we get the second class (e.g., "Three") safely
            rating = rating_tag["class"][1] if rating_tag and len(rating_tag["class"]) > 1 else "No Rating"
            
            items_data.append({
                "title": title,
                "price": price,
                "stock": stock,
                "rating": rating,
                "link": link
            })
        except Exception as e:
            print(f"Error parsing item: {e}")
            continue

    return items_data

# --- MAIN LOOP ---

def run_scraper():
    all_books = []
    # Start directly with the full URL of the first page
    current_url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

    while current_url:
        print(f"Scraping: {current_url}")
        
        books = scrape_book_data(current_url)
        
        if not books:
            print("No books found on this page. Stopping.")
            break
        
        all_books.extend(books)
        
        # Check for the "Next" button to find the subsequent URL
        response = requests.get(current_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        next_button = soup.find("li", class_="next")
        
        if next_button:
            next_link = next_button.find("a")["href"]
            current_url = urljoin(current_url, next_link)
        else:
            print("No 'Next' button found. Reached last page.")
            current_url = None  

