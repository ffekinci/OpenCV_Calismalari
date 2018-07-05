import cv2 as cv
import numpy as np

cv.waitKey(0)
cv.destroyAllWindows()

img = cv.imread("roi.jpg")

BLUE = [255,0,0]




cv.imshow("deneme", img)

