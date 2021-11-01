import numpy as np
import cv2 as cv

ori = cv.imread('./Pics/test.jpg')
img = cv.imread('./Pics/test.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()

kp, des = sift.detectAndCompute(gray,None)

img = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, color = (0, 255, 255))

# DRAW_MATCHES_FLAGS_DEFAULT：只绘制特征点的坐标点，显示在图像上就是一个个小圆点，每个小圆点的圆心坐标都是特征点的坐标。
# DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG：函数不创建输出的图像，而是直接在输出图像变量空间绘制，要求本身输出图像变量就是一个初始化好了的，size与type都是已经初始化好的变量。
# DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS ：单点的特征点不被绘制。
# DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS：绘制特征点的时候绘制的是一个个带有方向的圆，这种方法同时显示图像的坐标，size和方向，是最能显示特征的一种绘制方式。


cv.namedWindow("Original", 0)
cv.resizeWindow("Original" , 480, 640)

cv.namedWindow("SIFT", 0)
cv.resizeWindow("SIFT", 480, 640)

cv.imshow('Original',ori)
cv.imshow('SIFT',img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()