import pandas as  pd

#pull down review data from insideairbnb



def get_city_reviews():
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

    # Display the first few rows of the combined DataFrame
    return all_reviews