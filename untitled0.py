import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

# Download the stopwords from NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Read the contents of the file
with open('random_paragraphs.txt', 'r') as file:
    text = file.read().lower()

# Tokenize the text
tokens = word_tokenize(text)

# Remove the stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_tokens)

# Display the word frequency count to the console
for word, count in word_freq.items():
    print(f'Word: {word}, Frequency: {count}')
