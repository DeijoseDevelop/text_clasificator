import io
import typing as t

import cv2
import cv2.typing

from app.modules.common import exceptions, interfaces
from app.modules.user_recognition.data import use_cases
from app.modules.user_recognition.data import models


class RecognitionController(interfaces.BaseController):

    def __init__(
        self,
        recognition_use_case: use_cases.RecognitionUseCase,
        image_manager: models.ImageManager
    ) -> None:
        self.recognition_use_case = recognition_use_case
        self.image_manager = image_manager

    def detect_face(
        self,
        image_bytes: io.BytesIO
    ) -> t.Dict[str, t.List[t.Dict[str, str | bool | t.Tuple[int, t.Any, t.Any, int]]] | io.BytesIO]:
        try:
            detection = self.recognition_use_case.call(
                params=use_cases.RecognitionUseCaseParams(image_bytes=image_bytes)
            )
            # if not detection["matched"]:
            #     raise Exception("Coincidencias no detectadas.")

            # TODO: test resize image with front

            io_image = self.image_manager.convert_cv2_image_to_bytes_io(self.image_manager.get_frame().get_value())

            if io_image is None:
                raise Exception("Imagen no se pudo codificar.")

            return {"data": detection, "image": io_image}

        except exceptions.UseCaseException as error:
            print(error.message)
        except Exception as error:
            print("error:", error)

    def convert_bytes_to_cv2_image(self, data: io.BytesIO) -> cv2.typing.MatLike:
        self.image_manager.convert_bytes_to_cv2_image(data=data)

    def convert_cv2_image_to_bytes(self, image: cv2.typing.MatLike) -> bytes:
        self.image_manager.convert_cv2_image_to_bytes(image=image)

