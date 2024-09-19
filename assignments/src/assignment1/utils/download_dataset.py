import os
import requests
import gzip
import shutil

def download_dataset() -> list[str]:
    """
    Download the Airbnb dataset for five cities and save them as CSV files in the dataset/assignment1 directory.
    Cities: Boston, New York, Montreal, Albany, Washington DC
    Returns:
        A list of the file paths of the downloaded datasets.
    """
    extracted_files_path: list[str] = []
    dest_dir = os.path.abspath(os.path.join(os.getcwd(), "../dataset/assignment1"))
    base_url = "https://data.insideairbnb.com"
    files_to_download: list[dict] = [
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
        city: str = file_data["city"]
        listings_url: str = file_data["listings_url"]
        reviews_url: str = file_data["reviews_url"]

        # Check if the file already exists
        listings_file_path = os.path.join(dest_dir, f"{city}_listings.csv")
        reviews_file_path = os.path.join(dest_dir, f"{city}_reviews.csv")

        if os.path.exists(listings_file_path):
            print(f"{city.capitalize()} listings file already exists.")
        else:
            download_and_extract(listings_url, listings_file_path)

        if os.path.exists(reviews_file_path):
            print(f"{city.capitalize()} reviews file already exists.")
        else:
            download_and_extract(reviews_url, reviews_file_path)
    
        extracted_files_path.append(reviews_file_path)
        extracted_files_path.append(listings_file_path)
        

    return extracted_files_path

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
    with gzip.open("temp.gz", "rb") as f_in:
        with open(dest_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
            print(f"Extracted to {dest_path}")

    # Remove the temporary gzip file
    os.remove("temp.gz")

