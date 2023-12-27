from app.modules.common import interfaces
from app.modules.category_classificator.data import repositories
from app.modules.common import exceptions


class CleanDataUseCase(interfaces.UseCaseNoParams):

    def __init__(self, repository: repositories.CleanDataRepository = None):
        self.repository = repository

    def call(self) -> tuple:
        try:
            (texts, labels) = self.repository.clean()
            return (texts, labels)
        except Exception as error:
            raise exceptions.UseCaseException(error)
