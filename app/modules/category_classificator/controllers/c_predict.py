import typing

from app.modules.category_classificator.data import use_cases
from app.modules.common import exceptions, interfaces


class PredictController(interfaces.BaseController):

    def __init__(
        self,
        predict_use_case: use_cases.PredictUseCase = None,
    ):
        self.data = {}
        self.predict_use_case = predict_use_case

    def predict(self, text) -> typing.List[str]:
        try:
            return self.predict_use_case.call(
                params=use_cases.PredictUseCaseParams(text=text)
            )
        except exceptions.UseCaseException as error:
            print(error.message)
