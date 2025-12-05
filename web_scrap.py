# scrape_books.py
"""
Scrape book titles, prices, and availability
from https://books.toscrape.com/
Saves results to: books_data.csv
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
        # Title
        title = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Availability
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

    df.to_csv("books_data.csv", index=False)
    print("Scraping Complete!")
    print(df.head(10).to_string(index=False))

if __name__ == "__main__":
    main()