import pandas as pd
import matplotlib.pyplot as plt
import json

# Function to safely read a JSON file
def safe_read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data)
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Load the datasets
discussions = safe_read_json('discussions.json')
nyt_articles = safe_read_json('nyt_articles.json')

# Check if data was loaded successfully
if discussions is not None and nyt_articles is not None:
    # Convert date columns to datetime
    discussions['createdAt'] = pd.to_datetime(discussions['createdAt'], errors='coerce')
    nyt_articles['pub_date'] = pd.to_datetime(nyt_articles['pub_date'], errors='coerce')

    # Drop rows with invalid dates
    discussions.dropna(subset=['createdAt'], inplace=True)
    nyt_articles.dropna(subset=['pub_date'], inplace=True)

    # Save the total counts before filtering
    total_discussions = discussions.shape[0]
    total_nyt_articles = nyt_articles.shape[0]

    # Filter data to only include entries between March 2023 and May 2024
    start_date = '2023-03-01'
    end_date = '2024-05-01'
    discussions = discussions[(discussions['createdAt'] >= start_date) & (discussions['createdAt'] <= end_date)]
    nyt_articles = nyt_articles[(nyt_articles['pub_date'] >= start_date) & (nyt_articles['pub_date'] <= end_date)]

    # Set the date columns as index
    discussions.set_index('createdAt', inplace=True)
    nyt_articles.set_index('pub_date', inplace=True)

    # Resample to monthly frequency
    monthly_discussions = discussions.resample('M').size()
    monthly_nyt_articles = nyt_articles.resample('M').size()

    # Calculate proportions based on original totals
    monthly_discussions_prop = monthly_discussions / total_discussions
    monthly_nyt_articles_prop = monthly_nyt_articles / total_nyt_articles

    # Calculate moving averages
    discussions_moving_avg = monthly_discussions_prop.rolling(window=3).mean()
    nyt_articles_moving_avg = monthly_nyt_articles_prop.rolling(window=3).mean()

    # Calculate monthly growth rates
    discussions_growth_rate = monthly_discussions_prop.pct_change()
    nyt_articles_growth_rate = monthly_nyt_articles_prop.pct_change()

    # Plot Temporal Analysis
    plt.figure(figsize=(14, 8))

    # Plot proportions
    plt.subplot(2, 1, 1)
    monthly_discussions_prop.plot(kind='line', label='Discussions Proportion', color='blue')
    monthly_nyt_articles_prop.plot(kind='line', label='NYT Articles Proportion', color='orange')
    discussions_moving_avg.plot(kind='line', label='Discussions Moving Avg (3 months)', linestyle='--', color='blue')
    nyt_articles_moving_avg.plot(kind='line', label='NYT Articles Moving Avg (3 months)', linestyle='--', color='orange')
    plt.title('Trend of AI and Automation Mentions Over Time (Proportions) from March 2023 to May 2024')
    plt.xlabel('Date')
    plt.ylabel('Proportion of Discussions/Articles')
    plt.legend()
    plt.grid(True)
    plt.xlim(pd.Timestamp(start_date), pd.Timestamp(end_date))
    plt.ylim(0, max(monthly_discussions_prop.max(), monthly_nyt_articles_prop.max()) * 1.1)

    # Plot growth rates
    plt.subplot(2, 1, 2)
    discussions_growth_rate.plot(kind='line', label='Discussions Growth Rate', color='blue')
    nyt_articles_growth_rate.plot(kind='line', label='NYT Articles Growth Rate', color='orange')
    plt.title('Monthly Growth Rate of AI and Automation Mentions')
    plt.xlabel('Date')
    plt.ylabel('Growth Rate')
    plt.legend()
    plt.grid(True)
    plt.xlim(pd.Timestamp(start_date), pd.Timestamp(end_date))

    # Highlight significant points
    max_discussions_prop_date = monthly_discussions_prop.idxmax()
    max_nyt_articles_prop_date = monthly_nyt_articles_prop.idxmax()

    plt.subplot(2, 1, 1)
    plt.axvline(x=max_discussions_prop_date, color='blue', linestyle='--', alpha=0.7)
    plt.axvline(x=max_nyt_articles_prop_date, color='orange', linestyle='--', alpha=0.7)
    plt.text(max_discussions_prop_date, monthly_discussions_prop.max(), 'Max Discussions', rotation=45, color='blue')
    plt.text(max_nyt_articles_prop_date, monthly_nyt_articles_prop.max(), 'Max NYT Articles', rotation=45, color='orange')

    plt.tight_layout()
    plt.show()
else:
    print("Failed to load one or both datasets.")
