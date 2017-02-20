import cv2
import numpy as np
import ImageProcessing as ip
img = cv2.imread('newtest.png')


hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

cv2.imwrite('hsv.jpg',hsv)


gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

copy = np.array(gray)

gray = cv2.medianBlur(gray, 5)

cv2.imwrite('gray.jpg',gray)



#thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#cv2.imwrite('thresh.jpg',thresh)
can = cv2.Canny(gray, 50, 100)

cv2.imwrite('canny.jpg', can)

f, contours, hierarchy = cv2.findContours(can, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    cv2.drawContours(copy,[c],0,(0,255,0),1)

cv2.imwrite('contours.jpg', copy)
    


for c in contours:
    if cv2.contourArea(c) > 100:
        rect = cv2.minAreaRect(c)
        x = cv2.boxPoints(rect)
        x1,y1 = x[0]
        x2,y2 = x[1]
        x3,y3 = x[2]
        x4,y4 = x[3]

        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)
        cv2.line(img, (x2,y2), (x3,y3), (0,255,0), 1)
        cv2.line(img, (x3,y3), (x4,y4), (0,255,0), 1)
        cv2.line(img, (x4,y4), (x1,y1), (0,255,0), 1)

        


cv2.imwrite('boxes.jpg', img)







