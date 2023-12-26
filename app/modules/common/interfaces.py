import abc
from flasgger import SwaggerView


class APIView(SwaggerView):
    pass


class Params(abc.ABC):
    pass


class UseCase(abc.ABC):
    @abc.abstractmethod
    def call(self, params: Params = None):
        pass


class UseCaseNoParams(abc.ABC):
    @abc.abstractmethod
    def call(self):
        pass
