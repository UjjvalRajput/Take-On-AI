import json
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from textblob import TextBlob

# Load data
with open('discussions.json') as f:
    discussions = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(discussions)

# Data Cleaning
df['bodyText'] = df['bodyText'].str.replace(r'\s+', ' ', regex=True)  # Replace multiple spaces with a single space
df.dropna(subset=['bodyText', 'createdAt'], inplace=True)  # Drop rows with missing bodyText or createdAt

# Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

df['sentiment'] = df['bodyText'].apply(get_sentiment)
df['sentiment_category'] = pd.cut(df['sentiment'], bins=[-1, -0.05, 0.05, 1], labels=['Negative', 'Neutral', 'Positive'])

# Plot Sentiment Distribution
sentiment_counts = df['sentiment_category'].value_counts()

plt.figure(figsize=(10, 6))
sentiment_counts.plot(kind='bar', color=['red', 'grey', 'green'])
plt.title('Sentiment Distribution of AI and Automation Discussions from GitHub')
plt.xlabel('Sentiment')
plt.ylabel('Number of Discussions')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('sentiment-Github.png')
plt.show()


# Topic Modeling
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['bodyText'])

lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)

# Display topics
for index, topic in enumerate(lda.components_):
    print(f'Topic #{index}')
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])

# Example Engagement Metrics (Placeholder logic)
df['comments'] = df['bodyText'].apply(lambda x: len(x.split()))  # Placeholder for actual comments count
df['likes'] = df['bodyText'].apply(lambda x: len(x.split()) // 2)  # Placeholder for actual likes count

# Plot Engagement Metrics
engagement_metrics = df[['comments', 'likes']].sum()

plt.figure(figsize=(10, 6))
engagement_metrics.plot(kind='bar', color=['blue', 'orange'])
plt.title('Engagement Metrics for AI and Automation Discussions from GitHub')
plt.xlabel('Metric')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Temporal Analysis
df['createdAt'] = pd.to_datetime(df['createdAt'])
df.set_index('createdAt', inplace=True)

# Resample to monthly frequency
monthly_mentions = df.resample('M').size()

# Plot Temporal Analysis
plt.figure(figsize=(12, 6))
monthly_mentions.plot(kind='line', marker='o')
plt.title('Trend of AI and Automation Mentions Over Time on GitHub')
plt.xlabel('Date')
plt.ylabel('Number of Discussions')
plt.grid(True)
plt.tight_layout()
plt.show()

