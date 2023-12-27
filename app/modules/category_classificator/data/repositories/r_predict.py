from typing import Dict, Any

import flask
import joblib as model_saver

from app.modules.category_classificator.data import repositories


class PredictRepository(repositories.BaseRepository):

    def __init__(self):
        self.model = model_saver.load(flask.current_app.config.get("model"))
        self.vectorizer = model_saver.load(flask.current_app.config.get("vectorizer"))

    def predict(self, data: str) -> Any:
        vectorized_data = self.vectorization_data(data=data)

        return self.model.predict(vectorized_data)

    def vectorization_data(self, data) -> Any:
        return self.vectorizer.transform([data.lower()])
