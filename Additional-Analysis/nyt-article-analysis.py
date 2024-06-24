import json
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from PIL import ImageFont
import pandas as pd
import re
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Try to load the font
font = ImageFont.truetype("C:\\Users\\ujjva\\Downloads\\arial-font\\arial.ttf", size=12)


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

# Save the processed data to a new file
df.to_csv('processed_nyt_articles.csv', index=False)

print("Sentiment analysis complete. Saved to processed_nyt_articles.csv")

# Load the processed data
df = pd.read_csv('processed_nyt_articles.csv')

# Convert publication date to datetime, handle timezone info
df['pub_date'] = pd.to_datetime(df['pub_date']).dt.tz_localize(None)

# Extract year and month
df['year_month'] = df['pub_date'].dt.to_period('M')

# Plot sentiment distributions
plt.figure(figsize=(10, 6))
sns.histplot(df['headline_sentiment'], kde=True, bins=30, color='blue', label='Headline Sentiment')
sns.histplot(df['abstract_sentiment'], kde=True, bins=30, color='orange', label='Abstract Sentiment')
plt.title('Sentiment Distribution of Headlines and Abstracts')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()

# Plot sentiment comparison
plt.figure(figsize=(10, 6))
plt.scatter(df['headline_sentiment'], df['abstract_sentiment'], alpha=0.5)
plt.title('Sentiment Comparison between Headlines and Abstracts')
plt.xlabel('Headline Sentiment')
plt.ylabel('Abstract Sentiment')
plt.grid(True)
plt.show()

headline_text = ' '.join(df['headline'])
df['abstract'] = df['abstract'].fillna('')
abstract_text = ' '.join(df['abstract'])

# Define AI-related and sentimentally meaningful keywords
ai_keywords = {'machine learning', 'neural', 'algorithm', 'data', 'model', 'learning', 'intelligence', 'automated', 'technology'}

# Function to clean text data focused on AI keywords
def clean_text(text, additional_stopwords=set()):
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    # Remove single characters and extra spaces
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    stop_words = set(stopwords.words('english')).union(additional_stopwords)
    # Keep only AI relevant words or significant sentiment words
    text = ' '.join([word for word in text.split() if word in ai_keywords or len(word) > 4])  # length filter for potentially significant words
    return text

# Define domain-specific stop words
domain_stop_words = {'take', 'robotics', 'said', 'use', 'like', 'coming', 'china', 'report'}

# Clean the headlines and abstracts
df['headline_clean'] = df['headline'].apply(lambda x: clean_text(x, domain_stop_words))
df['abstract_clean'] = df['abstract'].apply(lambda x: clean_text(x, domain_stop_words))

# Most common words in cleaned headlines and abstracts
headline_words = ' '.join(df['headline_clean']).split()
abstract_words = ' '.join(df['abstract_clean']).split()

headline_common_words = Counter(headline_words).most_common(20)
abstract_common_words = Counter(abstract_words).most_common(20)

# Convert to DataFrame for plotting
headline_common_df = pd.DataFrame(headline_common_words, columns=['word', 'count'])
abstract_common_df = pd.DataFrame(abstract_common_words, columns=['word', 'count'])

# Plot common words
plt.figure(figsize=(14, 7))
sns.barplot(x='count', y='word', data=headline_common_df)
plt.title('Most Common AI-Related Words in Headlines After Cleaning')
plt.xlabel('Count')
plt.ylabel('Word')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 7))
sns.barplot(x='count', y='word', data=abstract_common_df)
plt.title('Most Common AI-Related Words in Abstracts After Cleaning')
plt.xlabel('Count')
plt.ylabel('Word')
plt.grid(True)
plt.show()
