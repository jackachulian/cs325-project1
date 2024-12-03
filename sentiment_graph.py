import os
import matplotlib.pyplot as plt
from collections import Counter

sentiment_words = {"positive", "neutral", "negative"}
sentiment_colors = {
    "positive": "#44e",
    "neutral": "#ee4",
    "negative": "#e44",
}

# Extracts the sentiment from an AI's sentiment response and ignore any of the extra words it may have outputted.
def find_first_sentiment(text: str):
    words = text.split()  # Split the text into words
    for word in words:
        if word.lower() in sentiment_words:
            return word.lower()  # Return the first matching word
    return None  # Return None if no keywords are found

# Directory containing text files
directory_path = './sentiments'

# Initialize data storage
file_sentiment_counts = {}

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        counter = Counter()
        with open(file_path, 'r') as file:
            for line in file:
                print("finding sentiment of: ",line[:20]+"...")
                sentiment = find_first_sentiment(line)
                print("sentiment: "+sentiment)
                counter[sentiment] += 1
        file_sentiment_counts[filename[:-4]] = counter

# Prepare data for grouped bar chart
files = list(file_sentiment_counts.keys())
sentiments = list(sentiment_words)
data = {sentiment: [file_sentiment_counts[file].get(sentiment, 0) for file in files] for sentiment in sentiments}

# Plot grouped bar chart
x = range(len(files))  # Number of files
bar_width = 0.15
bar_separation = 0.05
offsets = [-bar_width - bar_separation, 0, bar_width + bar_separation]  # Adjust positions for each sentiment

print(data)

plt.figure(figsize=(10, 6))
for i, sentiment in enumerate(sentiments):
    plt.bar(
        [pos + offsets[i] for pos in x],  # Offset bars for grouping
        data[sentiment],
        width=bar_width,
        label=sentiment,
        edgecolor='black',
        color=sentiment_colors[sentiment]
    )

# Customize the plot
plt.xticks(range(len(files)), files, rotation=45, ha='right')  # File names as x-axis labels
plt.title('Sentiment by Game')
plt.xlabel('Games')
plt.ylabel('Reviews')
plt.legend(title='Sentiments')
plt.tight_layout()

# Show the plot
plt.show()
