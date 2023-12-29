import typing as t

import face_recognition
from numpy import ndarray, float64

from app.modules.user_recognition.utils import interfaces


class FaceDetector(interfaces.Detector):

    def load_image(self, frame) -> ndarray[t.Any]:
        return face_recognition.load_image_file(frame)

    def get_face_locations(self, frame) -> t.List[t.Tuple[int, t.Any, t.Any, int]]:
        return face_recognition.face_locations(frame)

    def get_face_encodings(self, frame, locations = None) -> t.List[ndarray]:
        return face_recognition.face_encodings(frame, locations)

    def compare_faces(self, know_encodings: list, unknow_encoding) -> t.List[t.Any]:
        return face_recognition.compare_faces(know_encodings, unknow_encoding)

    def get_face_distances(self, know_encodings: list, unknow_encoding) -> (ndarray[float64] | t.Any):
        return face_recognition.face_distance(know_encodings, unknow_encoding)