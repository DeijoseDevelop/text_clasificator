import typing

from app.modules.category_classificator.data import use_cases
from app.modules.common import exceptions, interfaces


class TrainModelController(interfaces.BaseController):

    def __init__(
        self,
        clean_data_use_case: use_cases.CleanDataUseCase = None,
        train_model_use_case: use_cases.TrainModelUseCase = None,
    ):
        self.data = {}
        self.clean_data_use_case = clean_data_use_case
        self.train_model_use_case = train_model_use_case

    def train(self) -> str:
        try:
            self.train_model_use_case.call(
                params=use_cases.TrainModelUseCaseParams(self.get_data())
            )
            return "Successfully trained"
        except exceptions.UseCaseException as error:
            print(error.message)

    def get_data(self):
        (texts, labels) = self.clean_data_use_case.call()

        data = {"texts": texts, "labels": labels}
        self.data = data

        return data
