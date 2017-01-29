import numpy as np
import time
import cv2
import ImageProcessing as ip
#import PyFunc as pi

testImage = 'test3.png'

### TAKE A PICTURE
#pi.takePicture('test.jpg');
img = cv2.imread('input/'+testImage)
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
#contour = cv2.findContours(img,0)
#cv2.imwrite('output/contour.jpg',contour)
