import numpy as np
import cv2

def removeGray(img, lower, upper):
        size = img.shape
        nRows = size[0]
        nCols = size[1]
        for i in range(0,nRows):
                for j in range(0,nCols):
                        if (      ((img[i][j][0]-lower) < (upper-lower)) \
                                and ((img[i][j][1]-lower) < (upper-lower)) \
                                and ((img[i][j][2]-lower) < (upper-lower))):
                                        img[i][j][0] = 255;img[i][j][1] = 255;img[i][j][2] = 255;
        return img

def rgbToChromatic(array):
	size = array.shape
	nRows = size[0]
	nCols = size[1]
	nElem = size[2]
	array = array/(sum(array,2))
	#for i in range(0,nRows):
    	#	for j in range(0,nCols):
        #		RGB = 0
        #		for k in range(0,nElem):
         #   			RGB = RGB + array[i][j][k]
        #		for k in range(0,nElem):
         #   			array[i][j][k] = 255*array[i][j][k]/RGB

def findContours(img):
	# detect edges
	canny = cv2.Canny(img,40,180)
	
	# smooth and connect edges
	kernal = np.ones((3,3),np.uint8)
	canny = cv2.morphologyEx(canny,cv2.MORPH_CLOSE,kernal)
	cv2.imwrite('ip/output/cannyContours.png',canny)
	
	# find contours
	CV_RETR_EXTERNAL = 0     # workaround for missing constants issue
	CV_CHAIN_APPROX_NONE = 1 # workaround for missing constants issue
	contours, hierarchy, junk = cv2.findContours(canny,CV_RETR_EXTERNAL,method=CV_CHAIN_APPROX_NONE)
	print("\n\ncontours: \n")
	#print contours
	print("\n---------------------")
	print("hierarchy: \n")
	#print hierarchy
	print("\n---------------------")
	print("junk: \n")
	#print junk

	return np.asarray(hierarchy)

def fillContours(img,contours):
	CV_FILLED = -1 # workaround for missing constants issue
	color = (0,0,0) # black
	for contour in contours:
		cv2.drawContours(img,[contour],0,color,CV_FILLED)
	return img
