import joblib as model_saver


# Model
model = model_saver.load("model.joblib")
vectorizer = model_saver.load("vectorizer.joblib")

text2 = input("Enter your preference: ")

# Vectorization of the new text
new_text_tfidf = vectorizer.transform([text2.lower()])

# Evaluation
predicted_category = model.predict(new_text_tfidf)
print(f"The predicted category is: {predicted_category}")
