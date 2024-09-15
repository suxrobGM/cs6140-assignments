import pandas as  pd
import os

#pull down review data from insideairbnb

def get_data():
    # Check if data files exist if not download.
    if os.path.exists('assignments/dataset/assignment1/all_review_data.csv') != True:
        print("Downloading Reviews")
        get_city_reviews()
    if os.path.exists('assignments/dataset/assignment1/all_listing_data.csv') != True:
        print("Downloading Listings")
        get_city_listing()

def get_city_reviews():
    #https://chatgpt.com/share/66e75097-a694-8005-8e7c-437438a2ce85 --used to complete the function

    boston_reviews = pd.read_csv('https://data.insideairbnb.com/united-states/dc/washington-dc/2024-06-21/data/reviews.csv')
    new_york_reviews = pd.read_csv('https://data.insideairbnb.com/united-states/ny/new-york-city/2024-07-05/data/reviews.csv')
    montreal_reviews = pd.read_csv('https://data.insideairbnb.com/canada/qc/montreal/2024-06-18/data/reviews.csv')
    albany_reviews = pd.read_csv('https://data.insideairbnb.com/united-states/ny/albany/2024-06-07/data/reviews.csv')
    washington_dc_reviews = pd.read_csv('https://data.insideairbnb.com/united-states/dc/washington-dc/2024-06-21/data/reviews.csv')

    # Append 'city' column with respective city names
    boston_reviews['city'] = 'Boston'
    new_york_reviews['city'] = 'New York'
    montreal_reviews['city'] = 'Montreal'
    albany_reviews['city'] = 'Albany'
    washington_dc_reviews['city'] = 'Washington DC'

    # Concatenate all DataFrames together
    all_reviews = pd.concat([boston_reviews, new_york_reviews, montreal_reviews, albany_reviews, washington_dc_reviews], ignore_index=True)
    all_reviews.to_csv('assignments/dataset/assignment1/all_review_data.csv')



def get_city_listing():
    boston_listings = pd.read_csv('https://data.insideairbnb.com/united-states/ma/boston/2024-06-22/data/listings.csv')
    new_york_listings = pd.read_csv('https://data.insideairbnb.com/united-states/ny/new-york-city/2024-07-05/data/listings.csv')
    montreal_listings = pd.read_csv('https://data.insideairbnb.com/canada/qc/montreal/2024-06-18/data/listings.csv')
    albany_listings = pd.read_csv('https://data.insideairbnb.com/united-states/ny/albany/2024-06-07/data/listings.csv')
    washington_dc_listings = pd.read_csv('https://data.insideairbnb.com/united-states/dc/washington-dc/2024-06-21/data/listings.csv')

    boston_listings['city'] = 'Boston'
    new_york_listings['city'] = 'New York'
    montreal_listings['city'] = 'Montreal'
    albany_listings['city'] = 'Albany'
    washington_dc_listings['city'] = 'Washington DC'

    # Concatenate all DataFrames together
    all_listings = pd.concat([boston_listings, new_york_listings, montreal_listings, albany_listings, washington_dc_listings], ignore_index=True)
    
    all_listings.to_csv('assignments/dataset/assignment1/all_listing_data.csv')


def get_review_df():
    return pd.read_csv('all_review_data.csv')

def get_listing_df():
    return pd.read_csv('all_listing_data.csv')

get_data()
