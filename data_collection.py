import requests
import time
import pandas as pd
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def fetch_current_market_data():
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


def fetch_historical_data(crypto_id, days):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days={days}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df['time'] = pd.to_datetime(df['prices'].apply(lambda x: x[0]), unit='ms')
    df['current_price'] = df['prices'].apply(lambda x: x[1])
    df['market_cap'] = df['market_caps'].apply(lambda x: x[1])
    # Add this line if the API provides 'total_volume' data
    df['total_volume'] = df['total_volumes'].apply(lambda x: x[1])

    return df


# Fetch the current market data
market_data = fetch_current_market_data()
print(market_data)
# Convert the market data to a DataFrame
df = pd.DataFrame(market_data)  # Renamed to df

# Print the first few rows of the market DataFrame
print(df.head())

# Fetch historical data for Bitcoin over the past 30 days
df_historical = fetch_historical_data('bitcoin', 30)

# Print the first few rows of the historical DataFrame
print(df_historical.head())
