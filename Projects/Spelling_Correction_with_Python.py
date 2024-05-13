# It provides some very useful features for Machine Learning projects like:
# Noun phrase extraction
# Part-of-speech tagging
# Sentiment analysis
# Classification
# Tokenization
# Word and phrase frequencies
# Parsing
# n-grams
# Word inflexion and lemmatization
# Spelling correction
# Add new models or languages through extensions
# WordNet integration


from textblob import TextBlob

words = ["Machne", "Learnin"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")