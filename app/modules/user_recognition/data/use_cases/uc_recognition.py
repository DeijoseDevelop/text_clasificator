import io
import typing as t

from app.modules.common import interfaces
from app.modules.user_recognition.data import repositories
from app.modules.common import exceptions


class RecognitionUseCaseParams(interfaces.Params):

    def __init__(self, image_bytes: io.BytesIO) -> None:
        self.image_bytes = image_bytes


class RecognitionUseCase(interfaces.UseCase):

    def __init__(self, repository: repositories.RecognitionRepository):
        self.repository = repository

    def call(self, params: RecognitionUseCaseParams) -> t.List[t.Dict[str, str | bool | t.Tuple[int, t.Any, t.Any, int]]]:
        detection = self.repository.detect_face(image_bytes=params.image_bytes)

        if len(detection) == 0:
            raise exceptions.UseCaseException(message="Coincidencias no detectadas")

        return detection
