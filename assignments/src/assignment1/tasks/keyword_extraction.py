import pandas as pd
from matplotlib import pyplot as plt
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
            reviews[keyword] = reviews["comments"].apply(lambda text: is_keyword_present(text, keyword))

        # Display the first few rows with the new keyword features
        print(f"Keyword features for {city}:")
        print(reviews[["comments"] + [keyword for keyword in KEYWORDS]].head())
        plot_histogram(reviews, city)

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

def plot_histogram(data: pd.DataFrame, city: str) -> None:
    """
    Plots a histogram of the keyword features.
    Args:
        data (DataFrame): The DataFrame containing the keyword features.
        city (str): The name of the city.
    """

    # Create a DataFrame with the sum of each keyword feature
    keyword_counts = data[[keyword for keyword in KEYWORDS]].sum()

    # Plot a histogram of the keyword counts
    keyword_counts.plot(kind="bar", figsize=(10, 6))
    plt.title(f"Keyword Counts in Reviews for {city}")
    plt.xlabel("Keyword")
    plt.ylabel("Count")
    plt.show()
