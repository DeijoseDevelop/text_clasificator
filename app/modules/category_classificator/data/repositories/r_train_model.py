import typing as t

import flask
from scipy.sparse import spmatrix
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib as model_saver


class TrainModelRepository(object):

    def __init__(self) -> None:
        self.preprocessed_data = {}
        self.vectorized_data = {}
        self.model = MultinomialNB()
        self.vectorizer = TfidfVectorizer()

    def train(self, data: t.Dict[str, str]) -> None:
        self._preprocess_data(data=data)
        vectorized_data = self.vectorization_data()

        self.model.fit(vectorized_data["x_train_tfidf"], self.preprocessed_data["y_train"])

    def vectorization_data(self) -> t.Dict[str, spmatrix]:
        preprocessed_data = self.preprocessed_data
        x_train_tfidf = self.vectorizer.fit_transform(preprocessed_data["x_train"])
        x_test_tfidf = self.vectorizer.transform(preprocessed_data["x_test"])

        vectorized_data = {
            "x_train_tfidf": x_train_tfidf,
            "x_test_tfidf": x_test_tfidf,
        }
        self.vectorization_data = vectorized_data
        return vectorized_data

    def _preprocess_data(self, data: t.Dict[str, str]) -> None:
        (x_train, x_test, y_train, y_test) = train_test_split(data["texts"], data["labels"], test_size=0.2)

        self.preprocessed_data = {
            "x_train": x_train,
            "x_test": x_test,
            "y_train": y_train,
            "y_test": y_test,
        }

    def save_model(self) -> None:
        model_saver.dump(self.model, flask.current_app.config.get("model"))

    def save_vectorizer(self) -> None:
        model_saver.dump(self.vectorizer, flask.current_app.config.get("vectorizer"))
