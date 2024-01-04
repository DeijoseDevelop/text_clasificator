import typing as t

from app.modules.category_classificator.data import use_cases
from app.modules.common import exceptions, interfaces


class ClassifierController(interfaces.BaseController):

    def __init__(
        self,
        clean_data_use_case: use_cases.CleanDataUseCase,
        train_model_use_case: use_cases.TrainModelUseCase,
        predict_use_case: use_cases.PredictUseCase,
    ) -> None:
        self.data = {}
        self.clean_data_use_case = clean_data_use_case
        self.train_model_use_case = train_model_use_case
        self.predict_use_case = predict_use_case

    def predict(self, text: str) -> t.List[str]:
        try:
            return self.predict_use_case.call(
                params=use_cases.PredictUseCaseParams(text=text)
            )
        except exceptions.UseCaseException as error:
            # print(error.message)
            pass

    def train_model(self) -> None:
        self.train_model_use_case.call(
            params=use_cases.TrainModelUseCaseParams(self.get_data())
        )

    def get_data(self) -> t.Dict[str, t.Any]:
        (texts, labels) = self.clean_data_use_case.call()

        data = {"texts": texts, "labels": labels}
        self.data = data

        return data
