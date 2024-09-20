import pandas as pd
from utils import download_dataset

def run() -> None:
    print("Description Statistics\n")
    dataset = download_dataset()
    
    for data in dataset:
        listings = pd.read_csv(data.listings_csv)
        dataframe = listings[["price", "minimum_nights", "maximum_nights", "number_of_reviews", "review_scores_rating"]].describe()
        print(f"\nCity: {data.city.capitalize()}")
        print(dataframe)
