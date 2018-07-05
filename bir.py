import cv2

img = cv2.imread("ilk.png")
cv2.imshow("resim",img)

gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
"""""
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)


"""
cv2.imwrite("gray.png",gray)

img_crop = img[0:200,150:300]
cv2.imshow("kesilmis",img_crop)

r,c = img_crop.shape[:2]
new_img = cv2.resize(img_crop,(2*r,2*c))
cv2.imshow("resize",new_img)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()