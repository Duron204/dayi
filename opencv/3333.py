import cv2
import numpy as np

color = cv2.imread("image/opencv_logo.png")

color_hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask_red1 = cv2.inRange(color_hsv, lower_red1, upper_red1)
mask_red2 = cv2.inRange(color_hsv, lower_red2, upper_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

result = cv2.bitwise_and(color, color, mask=mask_red)

cv2.imshow("color", color)
cv2.imshow("mask_red", mask_red)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()