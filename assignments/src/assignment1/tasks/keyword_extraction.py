import os
import pandas as pd
from utils import download_dataset

# List of keywords to search for in the reviews
KEYWORDS = ["clean", "comfortable", "noisy", "spacious", "friendly"]

def run() -> None:
    print("Keyword Extraction\n")
    print("Keywords to search for in the reviews:", KEYWORDS)
    dataset = download_dataset()
    
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()
        reviews = pd.read_csv(data.reviews_csv)

        # Ensure comments are string type (handle NaN cases)
        reviews["comments"] = reviews["comments"].fillna("").astype(str)

        # Create binary features for each keyword
        for keyword in KEYWORDS:
            reviews[f"contains_{keyword}"] = reviews["comments"].apply(lambda text: is_keyword_present(text, keyword))

        # Display the first few rows with the new keyword features
        print(f"Keyword features for {city}:")
        print(reviews[["comments"] + [f"contains_{keyword}" for keyword in KEYWORDS]].head())

        # Save the new DataFrame with keyword features to a CSV
        csv_path = os.path.abspath(f"../../dataset/assignment1/{data.city}_reviews_with_keywords.csv")
        reviews.to_csv(csv_path, index=False)
        print(f"Saved CSV with keyword features to {csv_path}")

def is_keyword_present(text: str, keyword: str) -> int:
    """
    Checks if a keyword is present in a text.
    Args:
        text (str): The text to search for the keyword.
        keyword (str): The keyword to search for in the text.
    Returns:
        int: 1 if the keyword is present, 0 otherwise.
    """
    return int(keyword.lower() in text.lower())
