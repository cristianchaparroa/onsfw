from typing import List

from PIL import Image
from fastapi import Depends, FastAPI, File, UploadFile

from classifier import Classifier
from content import ImageContent

app = FastAPI()


def get_classifier():
    return Classifier()


@app.post("/moderations")
def moderations(
    file: List[UploadFile] = File(...), classifier: Classifier = Depends(get_classifier)
):
    images = []
    for f in file:
        try:
            image = ImageContent(f.file, f.filename)
            images.append(image)
        except Exception as e:
            return {"message": f"there was an error uploading the files: {str(e)}"}
        finally:
            f.file.close()
    return classifier.moderate_images(images)
