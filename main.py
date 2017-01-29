import numpy as np
import time
import cv2
import ImageProcessing as ip
#import PyFunc as pi


### TAKE A PICTURE
#pi.takePicture('test.jpg');

testImage = 'test3.png'
img = cv2.imread('input/'+testImage)

if img is None:
	raise Exception("Error while loading the image")

array = np.asarray(img);

### CONVERT TO CHROMATIC
ip.rgbToChromatic(array)
cv2.imwrite('output/chromatic.jpg', array)

### CONVERT TO GRAY
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('output/gray.jpg', img)

### THRESHOLD
#blur = cv2.GaussianBlur(img, (5,5), 0)
#th2 = cv2.threshold(blur, 0, 244, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thr = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('output/thresh.jpg', thr)

### MORPHOLOGICAL TRANSFORMATION
kernal = np.ones((4,4),np.uint8)
morph = cv2.morphologyEx(thr,cv2.MORPH_OPEN,kernal)
cv2.imwrite('output/morph.jpg', morph)

### FIND CONTOURS
canny = cv2.Canny(morph,40,180)
cv2.imwrite('output/canny.jpg',canny)
kernal = np.ones((3,3),np.uint8)
canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernal)
cv2.imwrite('output/canny_filled.jpg', canny)
contours, hierarchy = cv2.findContours(canny,cv2.cv.CV_RETR_EXTERNAL,method=cv2.cv.CV_CHAIN_APPROX_NONE)

# fill contours
color = (0,0,0) # black
for contour in contours:
	cv2.drawContours(morph,[contour],0,color,cv2.cv.CV_FILLED)
cv2.imwrite('output/contours.jpg',morph)
