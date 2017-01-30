from __future__ import division # default floating point division

import numpy as np
import cv2
import ImageProcessing as ip
import math
import matplotlib.pyplot as plt

# print full arrays
#np.set_printoptions(threshold='nan')

# load an image
img = cv2.imread('input/test3.png')
img = np.asarray(img)

# convert to chromatic 3D
ip.rgbToChromatic(img)

# convert to log-chromatic 2D
array = np.zeros((256,256,2))
size = img.shape
nRows = size[0]
nCols = size[1]

x = []
y = []

for i in range(0,nRows):
	for j in range(0,nCols):
		r = img[i][j][0]
		g = img[i][j][1]
		b = img[i][j][2]
		array[i][j] = (math.log(r/b),math.log(g/b))
		x.append(math.log(r/b))
		y.append(math.log(g/b))

plt.scatter(x,y)
plt.show()
