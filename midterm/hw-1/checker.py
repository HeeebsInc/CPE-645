import cv2
import numpy as np
from scipy import ndimage #import scipy

#check convole

#x = np.array([[1,1,1,1],[1,4,1,1],[1,1,1,-2],[1,1,1,1]])
x = np.array([[1,1,-2,1],[1,1,1,1],[1,4,1,1],[1,1,1,1]])
h = np.array([[0,1,0],[1,-4,1],[0,1,0]])
#h = np.array([[0,1,0],[],[]])
print(ndimage.convolve(x,h, mode = 'nearest', cval = 1.0, origin = -1))
#print(np.convolve(x, h))
