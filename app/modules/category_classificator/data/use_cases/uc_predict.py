import typing as t

from app.modules.common import interfaces
from app.modules.category_classificator.data import repositories
from app.modules.common import exceptions


class PredictUseCaseParams(interfaces.Params):

    def __init__(self, text: str) -> None:
        self.text = text


class PredictUseCase(interfaces.UseCase):

    def __init__(self, repository: repositories.PredictRepository) -> None:
        self.repository = repository

    def call(self, params: PredictUseCaseParams) -> t.List[str]:
        try:
            prediction = self.repository.predict(params.text)
            return list(prediction)
        except Exception as error:
            raise exceptions.UseCaseException(error)
