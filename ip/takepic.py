import time
from picamera import PiCamera
import cv2

with PiCamera() as camera:
    camera.resolution = (256,256)
    camera.start_preview()
    time.sleep(2)
    camera.capture('newtest.png')
