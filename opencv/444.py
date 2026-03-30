import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("成功打开摄像头")
else:
    print("未打开摄像头")
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        continue
    cv2.imshow("frame",frame)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()