import io
import typing as t

import flask
import numpy as np
import cv2.typing

from app.modules.user_recognition.data import repositories
from app.modules.user_recognition.data import models


class RecognitionRepository(repositories.BaseRepository):

    def __init__(self, image_manager: models.ImageManager) -> None:
        self.face_detector = models.FaceDetector()
        self.data_manager = models.DataManager(
            path=flask.current_app.config.get("recognition_data"),
            face_detector=self.face_detector
        )
        self.image_manager = image_manager

        self.known_face_encodings = self.data_manager.get_encodings()
        self.known_face_names = self.data_manager.get_names()

    def detect_face(self, image_bytes: io.BytesIO) -> t.List[t.Dict[str, str | bool | t.Tuple[int, t.Any, t.Any, int]]]:
        cv2_image = self._convert_bytes_to_cv2_image(image_bytes)

        self._set_frame(cv2_image)
        rgb_image = self._convert_to_rgb_and_get_value(self.image_manager.get_frame())
        face_locations, face_encodings = self._detect_faces(rgb_image)
        return self._find_best_match(face_encodings, face_locations)

    def _convert_bytes_to_cv2_image(self, image_bytes: io.BytesIO) -> cv2.typing.MatLike:
        return self.image_manager.convert_bytes_to_cv2_image(data=image_bytes)

    def _set_frame(self, cv2_image: cv2.typing.MatLike) -> None:
        self.image_manager.set_frame(cv2_image)

    def _convert_to_rgb_and_get_value(self, frame: models.Frame) -> cv2.typing.MatLike:
        rgb_image = frame.convert_to_rgb().get_rgb_value()
        return rgb_image

    def _detect_faces(self, rgb_image: cv2.typing.MatLike) -> t.Tuple[t.List[t.Any], t.List[np.ndarray]]:
        face_locations = self.face_detector.get_face_locations(rgb_image)
        face_encodings = self.face_detector.get_face_encodings(rgb_image, face_locations)
        return face_locations, face_encodings

    def _find_best_match(
        self,
        face_encodings: t.List[t.Any],
        face_locations: t.List[np.ndarray]
    ) -> t.List[t.Dict[str, str | bool | t.Tuple[int, t.Any, t.Any, int]]]:

        data = []

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = self.face_detector.compare_faces(self.known_face_encodings, face_encoding)
            face_distances = self.face_detector.get_face_distances(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            name = self.known_face_names[best_match_index]

            if matches[best_match_index]:
                self.image_manager.draw_rectangle(positions=(top, right, bottom, left), thickness=2)
                self.image_manager.draw_rectangle(positions=(bottom, right, bottom - 35, left), thickness=cv2.FILLED)
                self.image_manager.draw_text(name=name, positions=(top, right, bottom, left), thickness=2)

                detection = {
                    "name": self.known_face_names[best_match_index] ,
                    "matched": True,
                    "face_locations": (top, right, bottom, left)
                }

                data.append(detection)

        return data
