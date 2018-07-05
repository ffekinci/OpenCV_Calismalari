import numpy as np
import cv2 as cv

cap = cv.VideoCapture("mov_bbb.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("deneme", gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()