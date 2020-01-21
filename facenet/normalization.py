# for normalizing the image .

import cv2 as cv
import numpy as np
path = r"/home/harish/Desktop/hh.jpg"
img = cv.imread(path)
normalizedImg = np.zeros((800, 800))
print("print the first normalization array :",normalizedImg)
normalizedImg = cv.normalize(img,  normalizedImg, 0, 255, cv.NORM_MINMAX)
print("print the normalization :", normalizedImg)
cv.imshow('dst_rt', normalizedImg)
cv.waitKey(0)
cv.destroyAllWindows()
