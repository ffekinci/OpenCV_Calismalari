import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow("image")

cv.createTrackbar("R:", "image", 0, 255, nothing)
cv.createTrackbar("G:", "image", 0, 255, nothing)
cv.createTrackbar("B:", "image", 0, 255, nothing)

while 1:
    cv.imshow("image", img)
    k = cv.waitKey(1)
    if k == 27:
        break

    r = cv.getTrackbarPos("R:", "image")
    g = cv.getTrackbarPos("G:", "image")
    b = cv.getTrackbarPos("B:", "image")

    img[:] = [b, g, r]

cv.destroyAllWindows()