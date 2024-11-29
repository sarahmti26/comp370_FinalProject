import matplotlib.pyplot as plt

# Define the data for each category
categories = {
    "Kamala as a person": {
        "words": ["harris", "president", "vice", "kamala", "israel", "biden", "news", "trump", "supporters", "comments"],
        "scores": [1.9860, 1.7133, 1.2768, 1.0692, 0.9971, 0.9532, 0.9481, 0.9014, 0.8573, 0.8542]
    },
    "Election updates": {
        "words": ["trump", "president", "election", "harris", "news", "donald", "2024", "cbs", "win", "kamala"],
        "scores": [12.2773, 9.8527, 9.7411, 9.2947, 8.0226, 7.8037, 7.7475, 7.3686, 6.5624, 6.2399]
    },
    "Endorsement": {
        "words": ["harris", "obama", "president", "campaign", "kamala", "beyoncé", "endorsements", "trump", "barack", "vice"],
        "scores": [3.2700, 2.6414, 2.3423, 2.3084, 2.1550, 1.8039, 1.5082, 1.4643, 1.3761, 1.3758]
    },
    "Policies": {
        "words": ["trump", "harris", "president", "donald", "kamala", "election", "voters", "campaign", "vice", "stances"],
        "scores": [3.3258, 3.2730, 2.7692, 2.0589, 1.9276, 1.8036, 1.8033, 1.6645, 1.5207, 1.2758]
    },
    "Mentions of Kamala through other candidates": {
        "words": ["trump", "president", "harris", "donald", "kamala", "vice", "rally", "cbs", "women", "election"],
        "scores": [3.7148, 3.2503, 2.1515, 1.7655, 1.6022, 1.5653, 1.3709, 1.2615, 1.2589, 1.2162]
    },
    "Campaign": {
        "words": ["harris", "president", "trump", "campaign", "kamala", "vice", "news", "voters", "election", "donald"],
        "scores": [14.5758, 12.4981, 11.4359, 8.8944, 8.5423, 7.8230, 6.6398, 6.4146, 6.2161, 6.0365]
    },
    "General Facts about presidential elections": {
        "words": ["electoral", "college", "rural", "presidential", "democratic", "gap", "gender", "poll", "impact", "race"],
        "scores": [0.9726, 0.8662, 0.7276, 0.7159, 0.6734, 0.6020, 0.6020, 0.5872, 0.5840, 0.5621]
    }
}

# Function to create a bar graph for a given category
def plot_category(category_name, data):
    words = data["words"]
    scores = data["scores"]
    
    plt.figure(figsize=(10, 6))
    plt.bar(words, scores, color="skyblue")
    plt.title(f"Top 10 Words by TF-IDF for Category: {category_name}")
    plt.xlabel("Words")
    plt.ylabel("TF-IDF Scores")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{category_name}_tfidf.png")
    plt.show()

# Plot graphs for all categories
for category, data in categories.items():
    plot_category(category, data)
