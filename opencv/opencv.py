import cv2
image=cv2.imread("./image/rj.png")
rj_rgb = cv2.imread("./image/rj.png",1)
rj_gray = cv2.imread("./image/rj.png",0)
crop=image[10:170,120:240]
cv2.imshow("image",image)
cv2.imshow("crop",crop)
cv2.imshow("rj",rj_gray)
cv2.imshow("rj1",rj_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
