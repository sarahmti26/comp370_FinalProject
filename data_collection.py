import requests
import csv
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY") or ''

# Define the base URL and query parameters
base_url = 'https://newsapi.org/v2/everything'
query = '"Kamala Harris"'
language = 'en'
api_key = API_KEY
sources = 'abc-news,cnn,associated-press,bloomberg,business-insider,cbs-news,fortune,fox-news,google-news,msnbc,nbc-news,the-wall-street-journal,the-washington-post'
page = 1
# Path to the CSV file
csv_file = 'kamala_articles.csv'


def get_articles(params, page):
    params['page'] = page
    return requests.get(base_url, params=params)

# Fetch articles and save only new ones
def fetch_articles():
    articles = []
    params = {
        'q': query,
        'language': language,
        'apiKey': api_key,
        'sources' : sources,
        'page': page,
        'searchIn' : 'title,description'
    }

    for i in range(5):
        response = get_articles(params=params, page=i + 1)
        if response.status_code != 200:
            raise Exception(f"Error fetching news: {response.status_code}")
    
        # Get the articles
        cur_page_articles = response.json().get("articles", [])
        articles.extend(cur_page_articles)
    
    # Write articles to a CSV file
    with open(csv_file, mode='w`', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Title', 'Description', 'URL'])
        
        # Write article data
        for article in articles:
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            writer.writerow([title, description, url])

# Run the function
fetch_articles()
