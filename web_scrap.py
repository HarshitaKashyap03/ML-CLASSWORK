# scrape_books.py
"""
Scrape book titles, prices, and availability
from https://books.toscrape.com/
Saves results to:
1. books_data.csv
2. scrape_output.txt
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://books.toscrape.com/"

def fetch_page():
    response = requests.get(URL)
    response.raise_for_status()
    return response.text

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    titles = []
    prices = []
    availability = []

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()

        titles.append(title)
        prices.append(price)
        availability.append(stock)

    return pd.DataFrame({
        "Title": titles,
        "Price": prices,
        "Availability": availability
    })

def main():
    print("Fetching books webpage...")
    html = fetch_page()

    print("Parsing books...")
    df = parse_books(html)

    # Save CSV
    df.to_csv("books_data.csv", index=False)

    # Save OUTPUT to another file
    with open("scrape_output.txt", "w") as f:
        f.write("===== BOOK SCRAPING OUTPUT =====\n\n")
        f.write("Website: https://books.toscrape.com/\n")
        f.write(f"Total books scraped: {len(df)}\n\n")
        f.write("First 10 books:\n\n")
        f.write(df.head(10).to_string(index=False))

    print("Scraping Complete!")
    print(df.head(10).to_string(index=False))
    print("\nOutput saved in scrape_output.txt")

if __name__ == "__main__":
    main()
