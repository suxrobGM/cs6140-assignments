import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import download_dataset

def run() -> None:
    dataset = download_dataset()
    
    for data in dataset:
        city = data.city.replace("-", " ").capitalize()
        listings = pd.read_csv(data.listings_csv)
        reviews = pd.read_csv(data.reviews_csv)
        
        # Calculate word and character count for each review
        reviews["word_count"] = reviews["comments"].apply(calc_word_count)
        reviews["char_count"] = reviews["comments"].apply(calc_char_count)

        # Merge reviews with listings based on "listing_id" to bring in review scores
        merged_df = reviews.merge(listings[["id", "name", "review_scores_rating"]], left_on="listing_id", right_on="id", how="left")

        # Drop any rows where review_scores_rating is missing (if applicable)
        merged_df = merged_df.dropna(subset=["review_scores_rating"])

        # Correlation analysis
        correlation_word_count = merged_df["word_count"].corr(merged_df["review_scores_rating"])
        correlation_char_count = merged_df["char_count"].corr(merged_df["review_scores_rating"])

        print(f"\nCity: {city}")
        print(f"Correlation between word count and review scores: {correlation_word_count}")
        print(f"Correlation between character count and review scores: {correlation_char_count}")

        # Display the first few rows of the new dataframe
        print(merged_df[["listing_id", "name", "comments", "word_count", "char_count", "review_scores_rating"]])

        # Draw correlation heatmap
        plot_correlation_heatmap(city, merged_df)

        # Draw scatter plots
        plot_scatter(city, merged_df)


def calc_word_count(text: str) -> int:
    return len(text.split()) if pd.notnull(text) else 0

def calc_char_count(text: str) -> int:
    return len(text) if pd.notnull(text) else 0

def plot_correlation_heatmap(city: str, merged_df: pd.DataFrame) -> None:
    # Columns for correlation analysis
    corr_matrix = merged_df[["word_count", "char_count", "review_scores_rating"]].corr()

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(f"Correlation Heatmap for {city}")
    plt.show()

def plot_scatter(city: str, merged_df: pd.DataFrame) -> None:
    # Scatter plot for word count vs. review scores
    plt.figure(figsize=(8, 6))
    sns.regplot(x="word_count", y="review_scores_rating", data=merged_df, scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
    plt.title(f"Word Count vs Review Scores for {city}")
    plt.xlabel("Word Count")
    plt.ylabel("Review Scores")
    plt.show()

    # Scatter plot for character count vs. review scores
    plt.figure(figsize=(8, 6))
    sns.regplot(x="char_count", y="review_scores_rating", data=merged_df, scatter_kws={"alpha":0.5}, line_kws={"color":"red"})
    plt.title(f"Character Count vs Review Scores for {city}")
    plt.xlabel("Character Count")
    plt.ylabel("Review Scores")
    plt.show()
