import cv2
import numpy as np

# read input image
img = cv2.imread('newtest.png')

# convert to HSV spectrum to remove shadows
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
cv2.imwrite('hsv.jpg',hsv)

# convert to gray scale
gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

# blur image
gray = cv2.medianBlur(gray, 5)
cv2.imwrite('gray.jpg',gray)

# detect edges using Canny algorithm
can = cv2.Canny(gray, 50, 100)
cv2.imwrite('canny.jpg',can)

# find contours
f, contours, hierarchy = cv2.findContours(can, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# draw bounding boxes and midpoints
width = []
midpoint = []
angle = []
area = []
for c in contours:
    if cv2.contourArea(c) > 100:
        
        # find bounding box points
        rect = cv2.minAreaRect(c)
       
    
        x = cv2.boxPoints(rect)
        x1,y1 = x[0]
        x2,y2 = x[1]
        x3,y3 = x[2]
        x4,y4 = x[3]

        # save info to object lists

        angle.append(rect[2])
        area.append(cv2.contourArea(c))
        
      
        
        # draw bounding box
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)
        cv2.line(img, (x2,y2), (x3,y3), (0,255,0), 1)
        cv2.line(img, (x3,y3), (x4,y4), (0,255,0), 1)
        cv2.line(img, (x4,y4), (x1,y1), (0,255,0), 1)

        # calculate and draw midpoints
        mp1 = ((x1+x2)*0.5,(y1+y2)*0.5)
        mp2 = ((x3+x4)*0.5,(y3+y4)*0.5)
        mp = ((mp1[0]+mp2[0])*0.5,(mp1[1]+mp2[1])*0.5)
      
        xx = int(mp[0])
        yy = int(mp[1])
        
        cv2.circle(img, (xx,yy), 3 ,(0,0,255), -1)



      
        

# write input image with bounding boxes
cv2.imwrite('boxes.jpg',img)

print('Angles')
print(angle)
print('Areas')
print(area)





