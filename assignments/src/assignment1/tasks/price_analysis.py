import pandas as pd
from utils import download_dataset, AirbnbData
import matplotlib.pyplot as plt

def run() -> None:
    dataset = download_dataset()
    neighborhood_price_relation(dataset)
    roomType_price_relation(dataset)
    neighbourhood_minimum_nights_relation(dataset)

def neighborhood_price_relation(dataset: list[AirbnbData]) -> None:
    print("Neighborhood Price Relation\n")
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()

        # Load the listings data for Montreal
        listings = pd.read_csv(data.listings_csv)

        # Checking if "neighbourhood" and "price" fields exist
        if "host_neighbourhood" in listings.columns and "price" in listings.columns:
            # Clean data: Remove rows with missing values for "host_neighbourhood" and "price"
            listings_cleaned = listings[["host_neighbourhood", "price"]].dropna()
            
            # Convert price to numeric
            listings_cleaned["price"] = listings_cleaned["price"].replace("[$,]", "", regex=True).astype(float)
            
            # Group by neighborhood and calculate the average price and standard deviation
            neighborhood_stats = listings_cleaned.groupby("host_neighbourhood")["price"].agg(["mean"])
            
            # use chart to visualize the data without standard deviation
            neighborhood_stats["mean"].sort_values(ascending=False).plot(kind="bar", figsize=(15, 6))
            plt.title("Average Price by Neighborhood in " + city)
            plt.xlabel("Neighborhood")
            plt.ylabel("Average Price")
            plt.show()
        else:
            print(f"The required fields 'neighbourhood' and 'price' are not in the {city} dataset")

def roomType_price_relation(dataset: list[AirbnbData]) -> None:
    print("Room Type Price Relation\n")
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()

        # Load the listings data for Montreal
        listings = pd.read_csv(data.listings_csv)

        # Checking if "neighbourhood" and "price" fields exist
        if "room_type" in listings.columns and "price" in listings.columns:
            # Clean data: Remove rows with missing values for "host_neighbourhood" and "price"
            listings_cleaned = listings[["room_type", "price"]].dropna()
            
            # Convert price to numeric
            # listings_cleaned["price"] = pd.to_numeric(listings_cleaned["price"], errors="coerce")
            listings_cleaned["price"] = listings_cleaned["price"].replace("[$,]", "", regex=True).astype(float)
            
            # Group by neighborhood and calculate the average price and standard deviation
            roomType_stats = listings_cleaned.groupby("room_type")["price"].agg(["mean"])
            
            # use chart to visualize the data without standard deviation
            roomType_stats["mean"].sort_values(ascending=False).plot(kind="bar", figsize=(15, 6))
            plt.title("Average Price by Room Type in " + city)
            plt.xlabel("Room Type")
            plt.ylabel("Average Price")
            plt.show()
        else:
            print(f"The required fields 'room_type' and 'price' are not in the {city} dataset")
    
    
def neighbourhood_minimum_nights_relation(dataset: list[AirbnbData]) -> None:
    print("Neighbourhood Minimum Nights Relation\n")
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()

        # Load the listings data for Montreal
        listings = pd.read_csv(data.listings_csv)

        # Checking if "neighbourhood" and "price" fields exist
        if "host_neighbourhood" in listings.columns and "minimum_nights" in listings.columns:
            
            # Clean data: Remove rows with missing values for "host_neighbourhood" and "price"
            listings_cleaned = listings[["host_neighbourhood", "minimum_nights"]].dropna()
            
            # Convert price to numeric
            # listings_cleaned["price"] = pd.to_numeric(listings_cleaned["price"], errors="coerce")
            listings_cleaned["minimum_nights"] = listings_cleaned["minimum_nights"].replace("[$,]", "", regex=True).astype(float)
            
            # Group by neighborhood and calculate the average price and standard deviation
            neighborhood_stats = listings_cleaned.groupby("host_neighbourhood")["minimum_nights"].agg(["mean"])
            
            # use chart to visualize the data without standard deviation
            neighborhood_stats["mean"].sort_values(ascending=False).plot(kind="bar", figsize=(15, 6))
            plt.title("Average Minimum Nights by Neighborhood in " + city)
            plt.xlabel("Neighborhood")
            plt.ylabel("Average Minimum Nights")
            plt.show()
        else:
            print(f"The required fields 'neighbourhood' and 'minimum_nights' are not in the the {city} dataset")
