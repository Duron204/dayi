import cv2
import numpy as np

# 定义8位无符号整数（图像像素标准类型）
a = np.uint8([200])
b = np.uint8([70])

# 1. OpenCV 加法：饱和截断（最大值255）
cv2_result = cv2.add(a, b)

# 2. NumPy 加法：模256取余（溢出循环）
np_result = np.add(a, b)

# 3. 运算符加法：和np.add完全一致
operator_result = a + b

# 输出结果
print("cv2.add 结果：", cv2_result)   # [[255]]
print("np.add 结果：", np_result)     # [14]
print("+ 运算符 结果：", operator_result) # [14]