from typing import Dict

from app.modules.common import interfaces
from app.modules.category_clasificator.data import repositories
from app.modules.common import exceptions


class TrainModelUseCaseParams(interfaces.Params):

    def __init__(self, data: Dict[str]) -> None:
        self.data = data


class TrainModelUseCase(interfaces.UseCase):

    def __init__(self, repository: repositories.TrainModelRepository) -> None:
        self.repository = repository

    def call(self, params: TrainModelUseCaseParams) -> None:
        try:
            self.repository.train(data=params.data)
        except Exception as error:
            raise exceptions.UseCaseException(error)

