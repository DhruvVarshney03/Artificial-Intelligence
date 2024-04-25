import nltk
import re
import numpy as np
import heapq

# Sample text
text = """
Python is a high-level programming language widely used for various purposes such as web development, data analysis, artificial intelligence, and scientific computing. It is known for its simplicity and readability, making it an excellent choice for beginners and experienced programmers alike. Python has a vast ecosystem of libraries and frameworks that facilitate different tasks, from web scraping to machine learning. With its clean syntax and powerful features, Python has become one of the most popular programming languages in the world.
"""

dataset = nltk.sent_tokenize(text)
for i in range(len(dataset)):
    dataset[i] = dataset[i].lower()
    dataset[i] = re.sub(r'\W', ' ', dataset[i])
    dataset[i] = re.sub(r'\s+', ' ', dataset[i])

word2count = {}
for data in dataset:
    words = nltk.word_tokenize(data)
    for word in words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1

freq_words = heapq.nlargest(100, word2count, key=word2count.get)
X = []
for data in dataset:
    vector = []
    for word in freq_words:
        if word in nltk.word_tokenize(data):
            vector.append(1)
        else:
            vector.append(0)
    X.append(vector)
X = np.asarray(X)
print("Dhruv Varshney \nA2305221157")
print(X)


from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Example text
text = "running cats"

# Tokenize the text into individual words
tokens = word_tokenize(text)

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

print("Stemmed words:", stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]

print("Lemmatized words:", lemmatized_words)
