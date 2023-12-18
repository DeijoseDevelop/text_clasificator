from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib as model_saver
from db import texts, labels


# Preprocessing and splitting the data
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2)

# Vectorization
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

model_saver.dump(model, 'model.joblib')
model_saver.dump(vectorizer, 'vectorizer.joblib')
