import pandas as pd
from utils import download_dataset
import seaborn as sns
import matplotlib.pyplot as plt

def run() -> None:
    print("Correlation Analysis\n")
    dataset = download_dataset()

    dataset = download_dataset()
    
    for data in dataset:
        city = data.city

        #Get all numeric categories
        numerical_cats = pd.read_csv(data.listings_csv).select_dtypes(include=['number'])
        
        #drop ids
        numerical_cats = numerical_cats.drop(columns=['id', 'scrape_id', 'host_id'])

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