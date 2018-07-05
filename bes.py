import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

#define 123
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv.flip(frame, 0)

        out.write(frame)

        cv.imshow("frame", frame)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()