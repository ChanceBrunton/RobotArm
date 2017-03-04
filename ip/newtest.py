
import cv2




img = cv2.imread('ip/input/test3.png')
cv2.imwrite('test3.jpg', img)

#array = np.asarray(img);

print (img)

### CONVERT TO CHROMATIC
#ip.rgbToChromatic(array)
#cv2.imwrite('ip/output/chromatic.jpg', array)

