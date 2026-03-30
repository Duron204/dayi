import cv2
cat = cv2.imread("./image/cat.jpg")
new_cat = cat.copy()
b = cat[:, :, 0]
g = cat[:, :, 1]
r = cat[:, :, 2]
cv2.imshow("cat", cat)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.waitKey()
cv2.destroyAllWindows()