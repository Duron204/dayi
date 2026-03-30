import cv2
# 打开本地视频文件
cap = cv2.VideoCapture("image/保护校花.mp4")
if cap.isOpened():
    print("成功打开视频")
    open = True
    # 读取第一帧（可选，不影响循环逻辑）
    open, frame = cap.read()
else:
    open = False
# 循环读取视频帧
while open:
    ret, frame = cap.read()
    # 若帧为空（视频结束），退出循环
    if frame is None:
        break
    # 若成功读取帧，显示画面
    if ret == True:
        cv2.imshow("video", frame)
        # 按ESC键（键值27）退出播放
        if cv2.waitKey(25) & 0xff == 27:
            break
# 释放视频资源
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
