import requests
import time
import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def fetch_current_market_data(per_page=100):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page={per_page}"
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


def fetch_historical_data(id, days):
    data = cg.get_coin_market_chart_by_id(id=id, vs_currency='usd', days=days)
    df = pd.DataFrame(data['prices'], columns=['time', 'price'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    return df


# Fetch the current market data
market_data = fetch_current_market_data()

# Convert the market data to a DataFrame
df = pd.DataFrame(market_data)  # Renamed to df

# Print the first few rows of the market DataFrame
print(df.head())

# Fetch historical data for Bitcoin over the past 30 days
df_historical = fetch_historical_data('bitcoin', 30)

# Print the first few rows of the historical DataFrame
print(df_historical.head())
