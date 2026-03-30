import cv2
import numpy as np
# 创建一个大小为800x800像素的空白图像，3个通道（BGR格式），np.uint8:像素值的范围是0~255
image = np.zeros([800, 800, 3], dtype=np.uint8)

# 添加顶部白色文本，坐标(100,50)，字体，缩放，白色，线宽
cv2.putText(image, "AI Drawing_zhangsan", (100, 50), 0, 1, (255, 255, 255), 2)

# 绘制蓝色正方形，左上角坐标，右下角坐标，蓝色，线宽
cv2.rectangle(image, (100, 350), (350, 600), (255, 0, 0), 3)

# 绘制紫色菱形，定义顶点坐标，闭合多边形，紫色，线宽
diamond_points = np.array([[200, 150], [250, 200], [200, 250], [150, 200]], np.int32).reshape((-1, 1, 2))
cv2.polylines(image, [diamond_points], True, (255, 0, 255), 3)

# 绘制绿色圆形，圆心坐标，半径，绿色，线宽
cv2.circle(image, (400, 250), 80, (0, 255, 0), 3)

# 绘制黄色倾斜椭圆，圆心，长短轴，旋转角-30度，黄色，线宽
cv2.ellipse(image, (400, 400), (180, 80), -30, 0, 360, (0, 255, 255), 3)

# 绘制红色直线，起点坐标，终点坐标，红色，线宽
cv2.line(image, (200, 250), (550, 550), (0, 0, 255), 3)

# 显示图像
cv2.imshow("Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()