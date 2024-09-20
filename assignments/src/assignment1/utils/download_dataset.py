import os
import requests
import gzip
import shutil

class AirbnbData:
    def __init__(self, city: str, listings_csv: str, reviews_csv: str):
        self.city = city
        self.listings_csv = listings_csv
        self.reviews_csv = reviews_csv

def download_dataset() -> list[AirbnbData]:
    """
    Download the Airbnb dataset for five cities and save them as CSV files in the dataset/assignment1 directory.
    If the files already exist, they will not be downloaded again and the existing files will be used.
    Cities: Boston, New York, Montreal, Albany, Washington DC
    Returns:
        A list of AirbnbData objects containing the city name, listings CSV file path, and reviews CSV file path.
    """
    extracted_files: list[AirbnbData] = []
    dest_dir = os.path.abspath("../../../dataset/assignment1")
    base_url = "https://data.insideairbnb.com"
    files_to_download: list[dict[str, str]] = [
        {
            "city": "boston",
            "listings_url": f"{base_url}/united-states/ma/boston/2024-06-22/data/listings.csv.gz",
            "reviews_url": f"{base_url}/united-states/ma/boston/2024-06-22/data/reviews.csv.gz", 
        },
        {
            "city": "new-york-city",
            "listings_url": f"{base_url}/united-states/ny/new-york-city/2024-09-04/data/listings.csv.gz",
            "reviews_url": f"{base_url}/united-states/ny/new-york-city/2024-09-04/data/reviews.csv.gz",
        },
        {
            "city": "montreal",
            "listings_url": f"{base_url}/canada/qc/montreal/2024-09-13/data/listings.csv.gz",
            "reviews_url": f"{base_url}/canada/qc/montreal/2024-09-13/data/reviews.csv.gz",
        },
        {
            "city": "albany",
            "listings_url": f"{base_url}/united-states/ny/albany/2024-09-05/data/listings.csv.gz",
            "reviews_url": f"{base_url}/united-states/ny/albany/2024-09-05/data/reviews.csv.gz",
        },
        {
            "city": "washington-dc",
            "listings_url": f"{base_url}/united-states/dc/washington-dc/2024-06-21/data/listings.csv.gz",
            "reviews_url": f"{base_url}/united-states/dc/washington-dc/2024-06-21/data/reviews.csv.gz",
        },
    ]

    # Check if the destination directory exists, if not create it
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for file_data in files_to_download:
        city = file_data["city"]
        listings_url = file_data["listings_url"]
        reviews_url = file_data["reviews_url"]

        # Check if the file already exists
        listings_file_path = os.path.join(dest_dir, f"{city}_listings.csv")
        reviews_file_path = os.path.join(dest_dir, f"{city}_reviews.csv")

        if not os.path.exists(listings_file_path):
            download_and_extract(listings_url, listings_file_path)

        if not os.path.exists(reviews_file_path):
            download_and_extract(reviews_url, reviews_file_path)
    
        extracted_files.append(AirbnbData(city, listings_file_path, reviews_file_path))
        
    return extracted_files

def download_and_extract(url: str, dest_path: str):
    """
    Download and extract a gzip file from the given URL to the destination path.
    Args:
        url: The URL of the gzip file to download.
        dest_path: The destination path to save the extracted file.
    """
    # Download the gzip file
    response = requests.get(url)
    with open("temp.gz", "wb") as f:
        f.write(response.content)
        print(f"Downloaded {url})")

    # Extract the gzip file
    with gzip.open("temp.gz", "rb") as gzip_file:
        with open(dest_path, "wb") as extracted_file:
            shutil.copyfileobj(gzip_file, extracted_file)
            print(f"Extracted to {dest_path}")

    # Remove the temporary gzip file
    os.remove("temp.gz")

