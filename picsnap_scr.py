from picamera2 import Picamera2
from PIL import Image
import io

def pic_capture():
    camera = Picamera2()
    camera.configure(camera.create_still_configuration())
    camera.start()

    img_array = camera.capture_array()

    image = Image.fromarray(img_array)

    img_mem = io.BytesIO()
    image.save(img_mem, format = "JPEG")

    img_mem.seek(0)

    camera.stop()

    return img_mem