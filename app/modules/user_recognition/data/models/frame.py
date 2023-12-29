import typing as t

import cv2

class Frame(object):

    def __init__(self) -> None:
        self._value = None
        self._rgb_value = None

    def get_value(self) -> t.Any | None:
        return self._value

    def get_rgb_value(self) -> t.Any | None:
        return self._rgb_value

    def set_value(self, frame) -> "Frame":
        self._value = frame
        return self

    def convert_to_rgb(self) -> "Frame":
        self._rgb_value = cv2.cvtColor(self._value, cv2.COLOR_BGR2RGB)
        return self