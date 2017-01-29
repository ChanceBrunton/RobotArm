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