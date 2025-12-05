import requests
import pandas as pd

data_list = []

# Loop through first 10 products
for i in range(1, 11):
    url = f"https://fakestoreapi.com/products/{i}"
    response = requests.get(url)
    data = response.json()

    title = data.get("title")
    price = data.get("price")
    category = data.get("category")
    rating = data.get("rating", {}).get("rate")

    data_list.append({
        "Title": title,
        "Price": price,
        "Category": category,
        "Rating": rating
    })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Save to CSV file
df.to_csv("product_data.csv", index=False)
print("Product data collected and saved successfully!")
print(df.head())