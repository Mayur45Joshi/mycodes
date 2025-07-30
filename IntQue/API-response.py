import requests

# Sample JSON payload
payload = {
    "weather": [
        {"city": "Delhi", "temperature": 42},
        {"city": "Mumbai", "temperature": 34},
        {"city": "Chennai", "temperature": 41},
        {"city": "Bangalore", "temperature": 29}
    ]
}

# Fake API endpoint (replace with your actual endpoint)
url = "https://example.com/api/weather"

# Send POST request
response = requests.post(url, json=payload)


# Assume the response has the same structure
if response.status_code == 200:
    data = response.json()

    # Filter cities with temperature > 40°C
    hot_cities = [entry["city"] for entry in data["weather"] if entry["temperature"] > 40]

    print("Cities with temperature > 40°C:", hot_cities)
else:
    print("Failed to fetch data. Status code:", response.status_code)
