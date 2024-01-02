import abc
import typing

import flask
import flasgger


class APIView(abc.ABC, flasgger.SwaggerView):
    pass


class BaseController(abc.ABC):
    pass


class Params(abc.ABC):
    pass


class UseCase(abc.ABC):
    @abc.abstractmethod
    def call(self, params: Params):
        pass


class UseCaseNoParams(abc.ABC):
    @abc.abstractmethod
    def call(self):
        pass


class Manager(abc.ABC):
    pass