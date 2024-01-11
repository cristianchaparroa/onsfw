from typing import List

from PIL.Image import Image
import opennsfw2 as n2
import numpy as np
import tensorflow as tf  # type: ignore
from content import ImageContent


class Classifier:
    _model: tf.keras.Model

    def __init__(self):
        self._model = n2.make_open_nsfw_model()

    def moderate_image(self, image: ImageContent) -> float:
        image = n2.preprocess_image(image.to_pillow())
        inputs = np.expand_dims(image, axis=0)  # Add batch axis (for single image).
        predictions = self._model.predict(inputs)
        sfw_probability, nsfw_probability = predictions[0]
        return nsfw_probability.tolist()

    def moderate_images(self, images: List[ImageContent]) -> dict:
        predictions = {}
        for image in images:
            predictions[image.filename] = self.moderate_image(image)
        return predictions
