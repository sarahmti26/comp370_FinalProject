import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('annotated_kamala_harris_articles.csv')

#clean up data same as the other script 
df.columns = df.columns.str.strip()
df['Annotation'] = df['Annotation'].str.strip()

# Preprocessing: combining Title and Description to create the full text
df['text'] = df['Title'] + " " + df['Description']

# Create a TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer on all the articles (500 articles)
tfidf_matrix = vectorizer.fit_transform(df['text'])

# Get the feature names (words)
words = vectorizer.get_feature_names_out()

# Get the TF-IDF matrix as a DataFrame for easier manipulation
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=words)

# Iterate over each category and calculate the top 10 words for each
categories = df['Annotation'].unique()  # List of all unique categories
top_words = {}

for category in categories:
    # Get the articles for the current category
    category_text = df[df['Annotation'] == category]['text']
    
    # Vectorize the category-specific text
    tfidf_category_matrix = vectorizer.transform(category_text)
    
    # Sum the TF-IDF scores for each word across all articles in the category
    category_scores = tfidf_category_matrix.sum(axis=0).A1  # A1 converts it to a 1D array
    word_score_pairs = zip(words, category_scores)
    
    # Sort the words by score in descending order
    sorted_word_score_pairs = sorted(word_score_pairs, key=lambda x: x[1], reverse=True)
    
    # Store the top 10 words for the category
    top_words[category] = sorted_word_score_pairs[:10]

# Display the top 10 words for each category
for category, words_scores in top_words.items():
    print(f"Top 10 words for category '{category}':")
    for word, score in words_scores:
        print(f"{word}: {score:.4f}")
    print("\n")
