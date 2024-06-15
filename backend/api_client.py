import requests
import time
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

API_ENDPOINT = "https://mc-api.marketcheck.com/v2/stats/car"
API_KEY = api_key

def fetch_price(year, make, model):
    """
    Fetches car price data from the API for a given year, make, and model.
    Assumes the car is new as the dataset includes 2024 models.
    """
    # response = requests.get(API_ENDPOINT, params=params)
    response = requests.get(API_ENDPOINT + f'?api_key={API_KEY}?ymm=${year}|{make}|{model}')

    if response.status_code == 200:
        return response.json()
    else:
        return None

def handle_requests(df):
    """
    Handles API requests respecting the rate limit.
    """
    for index, row in df.iterrows():
        if (index + 1) % MAX_REQUESTS_PER_SECOND == 0:
            time.sleep(1)  # Sleep for 1 second after every 5 requests
        price_data = fetch_price(row['year'], row['make'], row['model'])
        if price_data:
            save_to_firebase(price_data)
        else:
            print(f"Failed to fetch data for {row['year']} {row['make']} {row['model']}")

    if response.status_code == 200:
        return response.json()
    else:
        return None

def handle_requests(df):
    """
    Handles API requests respecting the rate limit.
    """
    for index, row in df.iterrows():
        if (index + 1) % MAX_REQUESTS_PER_SECOND == 0:
            time.sleep(1)  # Sleep for 1 second after every 5 requests
        price_data = fetch_price(row['year'], row['make'], row['model'])
        if price_data:
            save_to_firebase(price_data)
        else:
            print(f"Failed to fetch data for {row['year']} {row['make']} {row['model']}")
