import cv2
import numpy as np

img = cv2.imread("image/cat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(gray)
mask[0:200, 0:200] = 255
img_or = cv2.bitwise_or(gray, mask)
img_not = cv2.bitwise_not(gray)
bit_xor = cv2.bitwise_xor(gray, mask)
img_and = cv2.bitwise_and(gray, mask)
cv2.imshow("gray", gray)
cv2.imshow("Mask", mask)
cv2.imshow("img_or",img_or)
cv2.imshow("img_not", img_not)
cv2.imshow("img_and", img_and)
cv2.imshow("bit_xor", bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()