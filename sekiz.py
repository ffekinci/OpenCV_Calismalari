import cv2 as cv
import numpy as np

##### Basic paint app :)

drawing = False #True is mouse pressed
mode = True #True sraw rectangle, False draw circle

def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix ,iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)
            else:
                cv.circle(img, (x,y), 10, (0,0,255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((512,512,3),np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image",draw)

while 1:
    cv.imshow("image",img)
    k = cv.waitKey(1)
    if k == ord('m'):
        mode = not mode

    elif k == 27:
        break

cv.destroyAllWindows()
