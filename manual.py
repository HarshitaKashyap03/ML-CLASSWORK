import pandas as pd

data = {
    "name": ["Ritika", "Samar", "Devansh", "Kunal", "Pooja", "Neeraj", "Sanya", "Tarun", "Vaishali"],
    "age": [22, 18, 24, 20, 19, 23, 25, 21, 28],
    "gender": ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'M', 'F'],
    "Education": ["BBA", "12th", "BCA", "B.Tech", "BA", "M.Tech", "MBA", "PhD", "MA"]
}

df = pd.DataFrame(data)

df.to_csv("manual_data.csv", index=False)

print("Saved Data Successfully!")
print(df.head())