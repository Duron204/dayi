import cv2
import numpy as np
# 创建一个大小为300x300像素的空白图像，3个通道（BGR格式），np.uint8:像素值的范围是0~255
image = np.zeros([300, 300, 3], dtype=np.uint8)
# 绘制一条直线，起始点坐标，结束点坐标，颜色（蓝色），线宽
cv2.line(image, (100, 180), (180, 180), (255, 0, 0), 4)
# 绘制一个矩形，起始点坐标，结束点坐标，颜色（绿色），线宽
cv2.rectangle(image, (80, 80), (130, 130), (0, 255, 0), 2)
# 绘制一个圆，圆心坐标，半径，颜色（红色），线宽
cv2.circle(image, (180, 100), 20, (0, 0, 255), 3)
cv2.circle(image, (140, 110), 100, (0, 255, 255), 3)
# 在图像上添加文本，文本内容，左下角坐标，字体类型
# （cv2.FONT_HERSHEY_SIMPLEX），线宽，缩放因子，白色，线宽，线的类型
# （cv2.LINE_AA，抗锯齿线）
# 图像→文字→坐标→字体→大小→颜色→粗细→线条类型
cv2.putText(image, "shuai", (100, 50), 0, 1, (255, 255, 255), 2, 1)
cv2.imshow("image", image)
cv2.waitKey()