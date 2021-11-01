import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('./Pics/test.jpg')
ori = cv2.imread('./Pics/test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,300,0.01,5)
corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),10,250,-1)

# cv2.circle(image, center_coordinates, radius, color, thickness)
# 参数：
# image:它是要在其上绘制圆的图像。
# center_coordinates：它是圆的中心坐标。坐标表示为两个值的元组，即(X坐标值，Y坐标值)。
# radius:它是圆的半径。
# color:它是要绘制的圆的边界线的颜色。对于BGR，我们通过一个元组。例如：(255，0，0)为蓝色。
# thickness:它是圆边界线的粗细像素。厚度-1像素将以指定的颜色填充矩形形状。


cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("Shi-Tomasi", 0)
cv2.resizeWindow("Shi-Tomasi", 480, 640)

cv2.imshow('Original', ori)
cv2.imshow('Shi-Tomasi', img)

cv2.waitKey(0)
cv2.destroyAllWindows()