import requests
import pandas as pd

# 1️⃣ Read Excel file into DataFrame
df = pd.read_excel("D:/STUDY AUTO/PandasAPI.xlsx")

# 2️⃣ Loop through each row and send POST request
url = "https://jsonplaceholder.typicode.com/users"

for index, row in df.iterrows():
    payload = {
        "name": row["name"],
        "username": row["username"],
        "email": row["email"],
        "phone": row["phone"]
    }

    # 3️⃣ Send POST request
    response = requests.post(url, json=payload)

    # # 4️⃣ Print response for verification
    # print(f"Row {index + 1} => Status: {response.status_code}, Response: {response.text}")

# Print request & response details
    print(f"\n➡️ Sending data for row {index + 1}: {payload}")
    print(f"✅ Status Code: {response.status_code}")
    print(f"📦 Response: {response.json()}")