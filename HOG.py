from skimage.feature import hog
import cv2

# 在深度学习出现之前，HoG 是对象检测应用中最突出的特征描述符之一。
# HoG 是一种用于计算图像局部中梯度方向出现的技术。

ori = cv2.imread('./Pics/test.jpg')
img = cv2.imread("./Pics/test.jpg")
_, hog_image = hog(img, orientations=32, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("HoG", 0)
cv2.resizeWindow("HoG", 480, 640)

cv2.imshow('Original', ori)
cv2.imshow('HoG', hog_image)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()