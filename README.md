# Media Coverage Analysis of Kamala Harris's 2024 Presidential Campaign

## Introduction

This project analyzes the media coverage of Kamala Harris during her 107-day campaign as the Democratic Party’s nominee for the 2024 U.S. presidential election. We examined 500 articles from English-language, North American online news outlets over a one-month period surrounding the election.

## Key Findings

- Coverage primarily focused on Harris's role as the Democratic candidate rather than her role as Vice President.
- Donald Trump was a significant presence in the coverage, often as a critic.
- Positive endorsements of Harris provided a counterbalance to negative remarks from Trump.
- Media coverage favored personal narratives over policy discussions.

## Data Collection

We used Newsapi.org to gather 500 relevant articles, ensuring they mentioned "Kamala Harris" in the title or description. The dataset includes:
1. **Title**: The article's title.
2. **Description**: A snippet from the article.
3. **URL**: The link to the article.
4. **Annotation**: The topic of the article, selected from a predefined typology.
5. **Sentiment**: The article's overall sentiment towards Harris.

## Methods

### Data Filtering and Annotation
Articles were filtered for relevance, language (English), and source credibility. They were categorized into seven topics: election, campaign, policies, endorsements, mentions by other political figures, Harris outside her campaign, and general facts about presidential elections. Sentiment was annotated as positive, negative, or neutral.

### Data Analytics and Visualization
Using Python scripting, we performed data analytics and visualization, turning raw data into actionable insights. Tf-idf scores were calculated to identify key terms in each category, and sentiment analysis was conducted to determine the overall tone of the articles.

## Results

- **Category Composition**: Most articles focused on Harris's campaign and election updates.
- **Tf-idf Analysis**: Key terms included endorsements by prominent figures like Obama and Beyoncé, and international relations topics like "Israel".
- **Sentiment Analysis**: Majority of articles were neutral, with endorsements being mostly positive and mentions by other political figures being more negative.

## Conclusion

Media coverage of Kamala Harris during the election period was predominantly neutral, with a focus on campaign updates and personal narratives over policy discussions. Positive endorsements and negative remarks from Trump significantly influenced the sentiment of the articles.

## Contributors

Charlotte Marchal, Ilana Martins, and Sarah Matmati.