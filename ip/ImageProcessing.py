import numpy as np
import cv2

def rgbToChromatic(array):
	size = array.shape
	nRows = size[0]
	nCols = size[1]
	nElem = size[2]
	for i in range(0,nRows):
    		for j in range(0,nCols):
        		RGB = 0
        		for k in range(0,nElem):
            			RGB = RGB + array[i][j][k]
        		for k in range(0,nElem):
            			array[i][j][k] = 255*array[i][j][k]/RGB

def findContours(img):
	# detect edges
	canny = cv2.Canny(img,40,180)
	
	# smooth and connect edges
	kernal = np.ones((3,3),np.uint8)
	canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernal)
	
	# find contours
	contours, hierarchy = cv2.findContours(canny,cv2.cv.CV_RETR_EXTERNAL,method=cv2.cv.CV_CHAIN_APPROX_NONE)

	return contours

def fillContours(img,contours):
	color = (0,0,0) # black
	for contour in contours:
		cv2.drawContours(img,[contour],0,color,cv2.cv.CV_FILLED)
	return img
