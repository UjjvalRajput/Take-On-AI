import json

import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

# Download necessary NLTK data files for sentiment analysis
nltk.download('vader_lexicon')

# Load preprocessed JSON corpus
with open('preprocessed_nyt_articles.json', 'r') as file:
    articles = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(articles)

# Ensure all entries in 'headline' and 'abstract' are strings
df['headline'] = df['headline'].astype(str)
df['abstract'] = df['abstract'].astype(str)

# Fill NaN values in 'abstract' with an empty string
df['abstract'].fillna('', inplace=True)

# Initialize Sentiment Intensity Analyzer
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis
df['headline_sentiment'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['abstract_sentiment'] = df['abstract'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Categorize sentiments
def categorize_sentiment(score):
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['headline_sentiment_category'] = df['headline_sentiment'].apply(categorize_sentiment)
df['abstract_sentiment_category'] = df['abstract_sentiment'].apply(categorize_sentiment)

# Save the processed data to a new file
df.to_csv('processed_nyt_articles.csv', index=False)

print("Sentiment analysis complete. Saved to processed_nyt_articles.csv")
# Load the processed data
df = pd.read_csv('processed_nyt_articles.csv')

# Plot sentiment distribution for headlines
plt.figure(figsize=(10, 6))
sns.countplot(x='headline_sentiment_category', data=df, palette='viridis', order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution in Headlines')
plt.xlabel('Sentiment Category')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Plot sentiment distribution for abstracts
plt.figure(figsize=(10, 6))
sns.countplot(x='abstract_sentiment_category', data=df, palette='viridis', order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution in Abstracts')
plt.xlabel('Sentiment Category')
plt.ylabel('Count')
plt.grid(True)
plt.show()
# Scatter plot to show correlation between headline and abstract sentiments
plt.figure(figsize=(10, 6))
sns.scatterplot(x='headline_sentiment', y='abstract_sentiment', data=df, hue='headline_sentiment_category', palette='viridis')
plt.title('Sentiment Comparison between Headlines and Abstracts')
plt.xlabel('Headline Sentiment')
plt.ylabel('Abstract Sentiment')
plt.legend(title='Headline Sentiment Category')
plt.grid(True)
plt.show()
# Calculate correlation between headline and abstract sentiments
correlation = df['headline_sentiment'].corr(df['abstract_sentiment'])

# Display correlation result
print(f'Correlation between headline and abstract sentiments: {correlation}')

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df[['headline_sentiment', 'abstract_sentiment']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation between Headline and Abstract Sentiments')
plt.show()
