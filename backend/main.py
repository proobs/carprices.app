import pandas as pd
import time
from api_client import fetch_price
from firebase_client import save_to_firebase

def main():
    # Load data
    df = pd.read_csv('./data/car_models.csv')

    # Process each entry
    for index, row in df.iterrows():
        print(f"Processing {row['year']} {row['make']} {row['model']}...")

        # Fetch price data from the API
        price_data = fetch_price(row['year'], row['make'], row['model'])
        if price_data:
            # Save the data to Firebase
            save_to_firebase(price_data)
        else:
            print(f"Failed to fetch data for {row['year']} {row['make']} {row['model']}")

if __name__ == '__main__':
    main()
