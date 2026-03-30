import cv2

# 读取图片
cat = cv2.imread('image/cat.jpg')
dog = cv2.imread('image/dog.png')

print(cat.shape, dog.shape)

cat_new = cv2.resize(cat, (dog.shape[1], dog.shape[0]))

print(cat_new.shape)
print(dog.shape)

img_add = cv2.add(cat_new, dog)

# 显示结果
cv2.imshow('img_add', img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()
