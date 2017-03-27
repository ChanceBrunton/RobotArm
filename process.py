import cv2
import numpy as np
import create_object


# return attributes of one object in frame

def processFrame():

    # read input image
    img = cv2.imread('newtest.png')


    # convert to HSV spectrum to remove shadows
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


    # convert to gray scale
    gray = cv2.cvtColor(hsv, cv2.COLOR_RGB2GRAY)

    # blur image
    gray = cv2.medianBlur(gray, 7)


    # detect edges using Canny algorithm
    can = cv2.Canny(gray, 50, 100)


    # find contours
    f, contours, hierarchy = cv2.findContours(can, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    width = 0
    xx = 0
    yy = 0
    angle = 0
    name = ''
    objects = []
    area = []
    area1 = []

    for c in contours:
        if cv2.contourArea(c) > 100:
        
            # find bounding box points
            rect = cv2.minAreaRect(c)  
            x = cv2.boxPoints(rect)
        
            x1,y1 = x[0]
            x2,y2 = x[1]
            x3,y3 = x[2]
            x4,y4 = x[3]

            # calculate object width
            width1 = ((x2-x1)**2 + (y2-y1)**2)**0.5
            width2 = ((x3-x2)**2 + (y3-y2)**2)**0.5

            areacalc = width1 * width2
            area1.append(areacalc)
        
            width = width1
            if width1 > width2:
                width = width2


            # classify object from area calculation
     
            if (areacalc >= 300 and areacalc <= 375):
                name = 'die'
            
            elif (areacalc >= 1450 and areacalc <= 1600):
                name = 'pencil'

            elif (areacalc >= 2000 and areacalc <= 2400):
                name = 'eraser'
                    
            elif (areacalc >= 3400 and areacalc <= 4000):
                name = 'pvc'

        
            

            # calculate and draw midpoints
            mp1 = ((x1+x2)*0.5,(y1+y2)*0.5)
            mp2 = ((x3+x4)*0.5,(y3+y4)*0.5)
            mp = ((mp1[0]+mp2[0])*0.5,(mp1[1]+mp2[1])*0.5)
      
            xx = int(mp[0])
            yy = int(mp[1])
        
            cv2.circle(img, (xx,yy), 3, (0,0,255), -1)

            # save object orientation angle     
            angle = rect[2]

            # create object from attributes
            obj = create_object.Piece(name, angle, width, xx, yy)

            break


    return (obj)
