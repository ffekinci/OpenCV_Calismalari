import cv2 as cv

capture = cv.VideoCapture(0)

if(capture.isOpened()):
    print("success")

while(1):
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("video",gray)
    if cv.waitKey(1) == ord('q'):
        break





















































capture.release()
cv.destroyAllWindows()
