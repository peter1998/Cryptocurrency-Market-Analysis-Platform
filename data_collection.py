import requests

def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    response = requests.get(url)
    data = response.json()
    return data

# For testing, print the data
print(fetch_data())
