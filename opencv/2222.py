import cv2
import numpy as np

img = cv2.imread("image/cat.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
cv2.imshow("img", img)
cv2.imshow("img_hsv", img_hsv)
cv2.imshow("img_yuv", img_yuv)
cv2.imshow("img_bgra", img_bgra)

cv2.waitKey(0)
cv2.destroyAllWindows()