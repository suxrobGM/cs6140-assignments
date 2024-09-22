import pandas as pd
from utils import download_dataset
import seaborn as sns
import matplotlib.pyplot as plt

def run() -> None:
    print("Correlation Analysis\n")
    dataset = download_dataset()

    
    for data in dataset:
        city = data.city
        
        listings = pd.read_csv(data.listings_csv)

        # Clean the 'price' column
        listings['price'] = listings['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

        # Clean percent columns 
        listings['host_response_rate'] = listings['host_response_rate'].replace({'%': ''}, regex=True).astype(float) / 100
        listings['host_acceptance_rate'] = listings['host_acceptance_rate'].replace({'%': ''}, regex=True).astype(float) / 100
            

        #Select umerical columns
        numerical_cats = listings.select_dtypes(include=['number'])
        
        #drop ids
        numerical_cats = numerical_cats.drop(columns=['id', 'scrape_id', 'host_id'])
        #Dropping redundant cats to reduce reading
        numerical_cats = numerical_cats.drop(columns= ['minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights', 'minimum_nights_avg_ntm', 'host_total_listings_count', "latitude", "longitude"])

        correllations = numerical_cats.corr()

        variablePairs = set()
        correllationDict = {}
        for i in correllations:
            for j in correllations:
                if i != j and set([i,j]) not in variablePairs:
                     correllationDict[i + ', ' + j] = correllations.loc[i,j]
                     variablePairs.add(frozenset([i, j]))

        correllationsDf= pd.DataFrame(correllationDict.items(), columns=['variables', 'correlation'])
        correllationsDf['abs_correlation'] = correllationsDf['correlation'].abs()

        positiveC = correllationsDf.nlargest(5, 'correlation')
        negativeC = correllationsDf.nsmallest(5, 'correlation')
        closest_to_zero = correllationsDf.nsmallest(5, 'abs_correlation')

        print(f"{city} Largest Positive Correlations")
        print(positiveC[['variables', 'correlation']])
        print()

        print(f"{city} Largest Negative Correlations")
        print( negativeC[['variables', 'correlation']])
        print()

        print(f"{city} Top 5 Correlations Closeest to 0")
        print(closest_to_zero[['variables', 'correlation']])

        plt.figure(figsize=(16, 16))
        sns.heatmap(correllations, cmap='coolwarm', center=0)
        plt.title(f"{city} Correlation Heatmap")
        plt.show()