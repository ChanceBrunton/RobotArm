from picamera import PiCamera

def takePicture(name):
	with PiCamera() as camera:
		camera.resolution = (256,256)
		camera.start_preview()
		time.sleep(2)
		camera.capture(name)