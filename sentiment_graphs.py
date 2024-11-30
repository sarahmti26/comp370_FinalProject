import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "/Users/ilanamartin/Documents/fall 2024/comp 370/project/comp370_FinalProject/complete_sentiment_analysis-2.csv"  # Replace with your CSV file path
data = pd.read_csv(file_path, delimiter=";")

# Strip trailing spaces from all string columns
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Calculate overall sentiment percentages
sentiment_counts = data['Sentiment'].value_counts(normalize=True) * 100

# General sentiment pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Overall Sentiment Distribution")
plt.show()

# Calculate sentiment percentages per annotation
annotations = data['Annotation'].unique()

for annotation in annotations:
    filtered_data = data[data['Annotation'] == annotation]
    sentiment_counts = filtered_data['Sentiment'].value_counts(normalize=True) * 100
    
    # Pie chart for each annotation
    plt.figure(figsize=(6, 6))
    plt.pie(
        sentiment_counts,
        labels=sentiment_counts.index,
        autopct='%1.1f%%',
        startangle=90
    )
    plt.title(f"Sentiment Distribution for Annotation: {annotation}")
    plt.show()
