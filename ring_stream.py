import io
import random
import time
import picamera
import pyzbar.pyzbar as pyzbar
from PIL import Image

# return as number 0 means not found
def read_barcode(camera):
    stream = io.BytesIO()
    camera.start_preview()
    time.sleep(1)
    camera.capture(stream, format='jpeg', use_video_port=True)
    stream.seek(0)
    current_image = Image.open(stream)
    barcodes = pyzbar.decode(current_image)

    if len(barcodes) > 0:
        return int(barcodes[0].data.decode('UTF-8'))
    else:
        return 0

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    stream = picamera.PiCameraCircularIO(camera, seconds=10)
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            barcode_id=read_barcode(camera)
            if barcode_id:
                print("ID found: {}".format(barcode_id))
            else:
                print("Nothing found, trying again")
    finally:
        camera.stop_recording()
