import cv2
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# 读取图片
cat = cv2.imread('image/cat.jpg')
dog = cv2.imread('image/dog.png')

dog_new = cv2.resize(dog, (cat.shape[1], cat.shape[0]))

res = cv2.addWeighted(cat, 0.9, dog_new, 0.4, 0)

plt.imshow(res)
plt.show()

cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()