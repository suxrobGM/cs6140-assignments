import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from utils import download_dataset

def run() -> None:
    print("Distribution Analysis\n")
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


        #columns to keep
        numerical_cats = numerical_cats[['price', 'minimum_nights', 'review_scores_rating']]

        
    
        for cat in numerical_cats:
            mean = numerical_cats[cat].mean()
            std_dev = numerical_cats[cat].std()
            filtered_data = numerical_cats[(numerical_cats[cat] >= mean - 3 * std_dev) & (numerical_cats[cat] <= mean + 3 * std_dev)]
            sns.kdeplot(data=filtered_data, x=cat, fill=True, color='blue', alpha=0.5)
            plt.xlim(left=0, right=filtered_data[cat].max())
            plt.title(f"Density Plot of {cat} in {city}")
            plt.xlabel(cat)
            plt.ylabel("Density")


            ### THIS CODE WAS COPIED FROM CHAT GPT
            # Get current ticks and set them to be twice as frequent
            current_ticks = plt.xticks()[0]
            new_ticks = []
            for tick in current_ticks:
                new_ticks.extend([tick - (tick - current_ticks[0]) / 2, tick])
            plt.xticks(sorted(set(new_ticks)))  # Ensure ticks are unique and sorted

            plt.show()