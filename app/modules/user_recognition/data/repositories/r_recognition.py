import io
import typing as t

import numpy as np

from app.modules.user_recognition.data import repositories
from app.modules.user_recognition.data import models


class RecognitionRepository(repositories.BaseRepository):

    def __init__(self) -> None:
        self.data_manager = models.DataManager()
        self.face_detector = models.FaceDetector()
        self.image_manager = models.ImageManager()

        self.known_face_encodings = self.data_manager.get_encodings()
        self.known_face_names = self.data_manager.get_names()

    def detect_face(self, image_bytes: io.BytesIO) -> t.Dict[str, bool | t.Tuple[int, t.Any, t.Any, int]]:
        cv2_image = self.image_manager.convert_bytes_to_cv2_image(data=image_bytes)
        self.image_manager.set_frame(cv2_image)

        rgb_image = self.image_manager\
                .get_frame()\
                .convert_to_rgb()\
                .get_rgb_value()

        face_locations = self.face_detector.compare_faces(rgb_image)
        face_encodings = self.face_detector.get_face_encodings(rgb_image, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = self.face_detector.compare_faces(self.known_face_encodings, face_encoding)

            face_distances = self.face_detector.get_face_distances(
                    self.known_face_encodings,
                    face_encoding
                )

            best_match_index = np.argmin(face_distances)

            return {"matched": matches[best_match_index], "face_locations": (top, right, bottom, left)}
