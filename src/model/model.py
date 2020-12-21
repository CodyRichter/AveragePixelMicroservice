from PIL import Image
from PIL.ImageStat import Stat
import time


def init():
    """
    This method will be run once on startup. You should check if the supporting files your
    model needs have been created, and if not then you should create/fetch them.
    """

    # Placeholder init code. Replace the sleep with check for model files required etc...
    time.sleep(1)


def predict(image_file):
    """
    Interface method between model and server. This signature must not be
    changed and your model must be able to predict given a file-like object
    with the image as an input.
    """

    image = Image.open(image_file.name, mode='r')
    stat = Stat(image)
    av_r, av_g, av_b = stat.mean  # Get average pixel
    image.close()
    return {
        'classes': ['average_red', 'average_green', 'average_blue'],  # List every class in the classifier
        'result': {  # For results, use the class names above with the result value
            'average_red': av_r,
            'average_green': av_g,
            'average_blue': av_b
        }
    }
