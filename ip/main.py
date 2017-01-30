import numpy as np
import time
import cv2
import ImageProcessing as ip
import PyFunc as pi


### TAKE A PICTURE
img = pi.takePicture('test.jpg');

#testImage = 'test3.png'
#img = cv2.imread('ip/input/'+testImage)

if img is None:
	raise Exception("Error while loading the image")

array = np.asarray(img);

### CONVERT TO CHROMATIC
ip.rgbToChromatic(array)
cv2.imwrite('ip/output/chromatic.jpg', array)

#print array

### CONVERT TO GRAY
img = ip.removeGray(array, 75, 100)
cv2.imwrite('ip/output/grayRemoved.jpg', img)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('ip/output/gray.jpg', img)

### THRESHOLD
#blur = cv2.GaussianBlur(img, (5,5), 0)
#th2 = cv2.threshold(blur, 0, 244, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thr = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('ip/output/thresh.jpg', thr)

### MORPHOLOGICAL TRANSFORMATION
kSize = 4; # size of kernal, horizontal and vertical
kernal = np.ones((kSize,kSize),np.uint8)
morph = cv2.morphologyEx(thr,cv2.MORPH_OPEN,kernal)
cv2.imwrite('ip/output/morph.jpg', morph)

### FIND CONTOURS
contours = ip.findContours(morph)

# fill contours
morph = ip.fillContours(morph,contours)
cv2.imwrite('ip/output/contours.jpg',morph)
