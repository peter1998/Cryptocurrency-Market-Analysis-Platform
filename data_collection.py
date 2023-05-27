import requests
import time


def fetch_data():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
    for i in range(5):  # Try the request up to 5 times
        try:
            response = requests.get(url)
            # Raise an exception if the response contains an HTTP error status code
            response.raise_for_status()
            data = response.json()
            return data  # If the request was successful, return the data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            time.sleep(2**i)  # Wait 2^i seconds before trying again
    return None  # If the request failed all 5 times, return None


# For testing, print the data
data = fetch_data()
if data is not None:
    print(data)
else:
    print("Failed to fetch data")
