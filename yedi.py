import cv2 as cv
import numpy as np

# Draw circle doubleclick left

'''
#Show events
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )
'''

#mouse callback
def draw_circle(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("image")
cv.setMouseCallback("image", draw_circle)

while 1:
    cv.imshow("image", img)
    if cv.waitKey(20) == 27:
        break


cv.destroyAllWindows()