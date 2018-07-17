import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('pics/cat1.jpg',0)
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', img)
k = cv.waitKey(0) & 0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    print ("Saving image")
    cv.imwrite('pics/cat_imwrite.png', img)
    cv.destroyAllWindows()

