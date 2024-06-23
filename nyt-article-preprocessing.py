import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load JSON corpus
with open('nyt_articles.json', 'r') as file:
    articles = json.load(file)

# Initialize stop words, lemmatizer, and punctuation translator
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
translator = str.maketrans('', '', string.punctuation)

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(translator)
    # Tokenize text
    words = nltk.word_tokenize(text)
    # Remove stop words and apply lemmatization
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Apply preprocessing to 'headline' and 'abstract'
for article in articles:
    if 'headline' in article:
        article['headline'] = preprocess_text(article['headline'])
    if 'abstract' in article:
        article['abstract'] = preprocess_text(article['abstract'])

# Save the preprocessed JSON corpus
with open('preprocessed_nyt_articles.json', 'w') as file:
    json.dump(articles, file, indent=4)

print("Preprocessing complete. Saved to preprocessed_nyt_articles.json")
