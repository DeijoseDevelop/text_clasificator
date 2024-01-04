import typing as t

from app.modules.category_classificator.data import use_cases
from app.modules.common import exceptions, interfaces


class PredictController(interfaces.BaseController):

    def __init__(
        self,
        predict_use_case: use_cases.PredictUseCase,
    ):
        self.data = {}
        self.predict_use_case = predict_use_case

    def predict(self, text) -> t.List[str]:
        try:
            return self.predict_use_case.call(
                params=use_cases.PredictUseCaseParams(text=text)
            )
        except exceptions.UseCaseException as error:
            # print(error.message)
            pass
