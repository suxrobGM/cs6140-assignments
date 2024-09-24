import pandas as pd
import matplotlib.pyplot as plt
from utils import download_dataset, AirbnbData

def run() -> None:
    dataset = download_dataset()
    review_scores_rating_neighbourhood_cleansed(dataset)

# review_scores_rating and neighbourhood_cleansed
def review_scores_rating_neighbourhood_cleansed(dataset: list[AirbnbData]) -> None:
    print("Review Scores Rating and Neighbourhood Cleansed\n")
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()
        listings = pd.read_csv(data.listings_csv)

        # Checking if "neighbourhood" and "price" fields exist
        if "review_scores_rating" in listings.columns and "neighbourhood_cleansed" in listings.columns:
            # Clean data: Remove rows with missing values for "host_neighbourhood" and "price"
            listings_cleaned = listings[["review_scores_rating", "neighbourhood_cleansed"]].dropna()
            
            # Convert price to numeric
            listings_cleaned["review_scores_rating"] = listings_cleaned["review_scores_rating"].replace("[$,]", "", regex=True).astype(float)
            
            # Group by neighborhood and calculate the average price and standard deviation
            neighborhood_stats = listings_cleaned.groupby("neighbourhood_cleansed")["review_scores_rating"].agg(["mean"])
            
            # use chart to visualize the data without standard deviation
            neighborhood_stats["mean"].sort_values(ascending=False).plot(kind="bar", figsize=(15, 6))
            plt.title("Review Scores Rating by Neighbourhood Cleansed in " + city)
            plt.xlabel("Neighbourhood Cleansed")
            plt.ylabel("Review Scores Rating")
            plt.show()
        else:
            print(f"The required fields 'neighbourhood' and 'price' are not in the {city} dataset")
