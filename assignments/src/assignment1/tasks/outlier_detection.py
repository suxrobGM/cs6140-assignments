import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import download_dataset

def run() -> None:
    print("Outlier Detection\n")
    dataset = download_dataset()

    # Columns for outlier detection
    columns = ["price", "minimum_nights", "review_scores_rating"]

    for data in dataset:
        city = data.city.replace("-", " ").capitalize()
        listings = pd.read_csv(data.listings_csv)

        # Display outliers for each city
        display_outliers(listings, city, columns)
        
        # Plot the outliers using box plots
        plot_outliers_boxplot(listings, city, columns)

def clean_numeric_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Cleans a column by removing non-numeric characters and converting it to numeric.
    Args:
        df (DataFrame): The DataFrame containing the data.
        column (str): The column to clean and convert to numeric.
    Returns:
        DataFrame: The cleaned DataFrame with the column converted to numeric.
    """
    # Remove non-numeric characters (e.g., $ or commas in price columns)
    df[column] = df[column].replace("[\\$,]", "", regex=True)

    # Convert the column to numeric, forcing errors to NaN
    df[column] = pd.to_numeric(df[column], errors="coerce")
    
    # Drop rows with NaN in the numeric column
    df = df.dropna(subset=[column])
    
    return df

def detect_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Detects outliers using the IQR method.
    Args:
        df (DataFrame): The DataFrame containing the data.
        column (str): The column for which to detect outliers.
    Returns:
        DataFrame: A DataFrame containing only the outlier rows.
    """
    # Clean and convert the column to numeric
    df = clean_numeric_column(df, column)

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers

def plot_outliers_boxplot(df: pd.DataFrame, city: str, columns: list[str]) -> None:
    """
    Plots box plots to visualize outliers for specific columns for a city using matplotlib and seaborn.
    Also plots the histogram for comparison.
    Args:
        df (DataFrame): The DataFrame containing the city listings data.
        city (str): Name of the city.
        columns (list[str]): List of numerical columns to analyze.
    """
    for column in columns:
        # Create a box plot to visualize outliers
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[column])
        plt.title(f"Outliers in {column} for {city}")
        plt.xlabel(column)
        plt.show()

        # Plot the histogram for comparison
        plt.figure(figsize=(10, 6))
        df[column].hist()
        plt.title(f"{column} distribution for {city}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

def display_outliers(df: pd.DataFrame, city: str, columns: list[str]) -> None:
    """
    Displays outliers for specific columns for a given city.
    Args:
        df (DataFrame): The DataFrame containing the city listings data.
        city (str): Name of the city.
        columns (list[str]): List of numerical columns to analyze.
    """
    print(f"\nOutliers in {city}:\n")

    for column in columns:
        outliers = detect_outliers(df, column)

        if not outliers.empty:
            print(f"Outliers in {column} for {city}:")
            print(outliers[[column]])
        else:
            print(f"No significant outliers in {column} for {city}")
