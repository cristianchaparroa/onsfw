import io
from typing import BinaryIO

from PIL import Image


class ImageContent:
    _filename: str
    _pimage: Image

    def __init__(self, image: BinaryIO, filename: str):
        self._pimage = Image.open(io.BytesIO(image.read()))
        self._filename = filename

    def to_pillow(self) -> Image:
        return self._pimage

    @property
    def filename(self):
        return self._filename
