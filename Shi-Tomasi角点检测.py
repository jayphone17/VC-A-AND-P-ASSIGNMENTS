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

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("Shi-Tomasi", 0)
cv2.resizeWindow("Shi-Tomasi", 480, 640)

cv2.imshow('Original', ori)
cv2.imshow('Shi-Tomasi', img)

cv2.waitKey(0)
cv2.destroyAllWindows()