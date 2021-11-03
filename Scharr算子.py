#coding:utf-8
import cv2 as cv
import numpy as np

img = cv.imread(r"./Pics/test.jpg")
#注意此处的ddepth不要设为-1，要设为cv.CV_32F或cv.CV_64F，否则会丢失太多信息
scharr_edge_x = cv.Scharr(img,ddepth=cv.CV_32F,dx=1,dy=0)
scharr_edge_x = cv.convertScaleAbs(scharr_edge_x) #convertScaleAbs等同于下面几句：

# scharr_edge_x = np.abs(scharr_edge_x)
# scharr_edge_x = scharr_edge_x/np.max(scharr_edge_x)
# scharr_edge_x = scharr_edge_x*255  #进行归一化处理
# scharr_edge_x = scharr_edge_x.astype(np.uint8)

scharr_edge_y = cv.Scharr(img,ddepth=cv.CV_32F,dx=0,dy=1)
scharr_edge_y = cv.convertScaleAbs(scharr_edge_y)

scharr_edge=cv.addWeighted(scharr_edge_x,0.5,scharr_edge_y,0.5,0) #两者等权叠加

cv.namedWindow("Original", 0)
cv.resizeWindow("Original", 360, 480)

cv.namedWindow("scharr_edge_x", 0)
cv.resizeWindow("scharr_edge_x", 360, 480)

cv.namedWindow("scharr_edge_y ", 0)
cv.resizeWindow("scharr_edge_y ", 360, 480)

cv.namedWindow("scharr_edge", 0)
cv.resizeWindow("scharr_edge", 360, 480)

cv.imshow("Original",img)
cv.imshow("scharr_edge_x",scharr_edge_x)
cv.imshow("scharr_edge_y ",scharr_edge_y )
cv.imshow("scharr_edge",scharr_edge)
cv.waitKey(0)
cv.destroyAllWindows()