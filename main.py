import numpy as np
#from picamera import PiCamera
import time
import cv2



#with PiCamera() as camera:
#    camera.resolution = (256,256)
#    camera.start_preview()
#    time.sleep(2)
#    camera.capture('test.jpg')


img = cv2.imread('test.jpg')
array = np.asarray(img);

#print(array[1][1])

size = array.shape
#print(size)
nRows = size[0]
nCols = size[1]
nElem = size[2]


for i in range(0,nRows):
    for j in range(0,nCols):
        RGB = 0
        for k in range(0,nElem):
            RGB = RGB + array[i][j][k]
        #print("RGB: "),;print(RGB),;print("    "),
        #print(array[i][j]),;print(" => "),
        for k in range(0,nElem):
            array[i][j][k] = 255*array[i][j][k]/RGB
        #print(array[i][j]);
            
#print(array[1][1])

cv2.imwrite('output/array.jpg', array)
img2 = cv2.imread('array.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


cv2.imwrite('output/gray_image.jpg', img2)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('output/gray.jpg', img)


#blur = cv2.GaussianBlur(img2, (5,5), 0)
#th2 = cv2.threshold(blur, 0, 244, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th2 = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#print(th2)
cv2.imwrite('output/thresh.jpg', th2)


#contour = cv2.findContours(img,0)






