import os
import typing as t

from numpy import ndarray
import flask

from app.modules.common import interfaces


DATA_PATH = flask.current_app.config.get("recognition_data")
IMAGES_PATH = f'{DATA_PATH}/images'

class DataManager(interfaces.Manager):

    def __init__(self, face_detector: interfaces.Detector, path: str = IMAGES_PATH) -> None:
        self._path = path
        self.face_detector = face_detector

        self._image_names = os.listdir(path)
        self._data = []
        self._names = []
        self._encodings = []

        self.set_data()

    def get_image_names(self) -> t.List[str]:
        return self._image_names

    def get_names(self) -> t.List[str]:
        return self._names

    def get_encodings(self) -> t.List[ndarray]:
        return self._encodings

    def get_data(self) -> list:
        return self._data

    def set_data(self) -> None:
        for name, encoding in zip(self.set_names(), self.set_encodings()):
            self._data.append({
                "name": name,
                "encoding": encoding,
            })

    def set_encodings(self) -> t.List[ndarray]:
        for image_name in self.get_image_names():
            image = self.face_detector.load_image(os.path.join(self._path, image_name))
            self._encodings.append(self.face_detector.get_face_encodings(image)[0])
        return self._encodings

    def set_names(self) -> t.List[str]:
        self._names = [
            image_name.split('.')[0]
            for image_name in self.get_image_names()
        ]

        return self._names
