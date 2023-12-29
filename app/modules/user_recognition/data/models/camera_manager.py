import typing as t

import cv2

from app.modules.user_recognition.data import models
from app.modules.common import interfaces


class CameraManager(interfaces.Manager):

    def __init__(self) -> None:
        # Get a reference to webcam #0 (the default one)
        self.video_capture = cv2.VideoCapture(0)
        self._frame = models.Frame()

    def get_frame(self) -> models.Frame:
        ret, frame = self.video_capture.read()
        self._frame.set_value(frame)
        return self._frame

    def draw_rectangle(self, positions: t.Tuple[int], thickness: int) -> None:
        (top, right, bottom, left) = positions
        cv2.rectangle(
            self._frame.get_value(),
            (left, top), (right, bottom),
            (0, 0, 255), thickness
        )

    def draw_text(self, name: str, positions: t.Tuple[int], thickness: int) -> None:
        (top, right, bottom, left) = positions
        cv2.putText(
            self._frame.get_value(), name,
            (left + 6, bottom - 6),
            cv2.FONT_HERSHEY_DUPLEX,
            1.0, (255, 255, 255), thickness
        )

    def show_image(self) -> None:
        cv2.imshow('Webcam', self._frame.get_value())

    def close_videoCapture(self) -> None:
        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()