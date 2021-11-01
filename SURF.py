import numpy as np
import cv2 as cv

ori =cv.imread('./Pics/test.jpg')
img = cv.imread('./Pics/test.jpg')

surf = cv.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
img2 = cv.drawKeypoints(img, kp, None, (0, 255, 255), 4)

cv.namedWindow("Original", 0)
cv.resizeWindow("Original" , 480, 640)

cv.namedWindow("SURF", 0)
cv.resizeWindow("SURF", 480, 640)

cv.imshow('Original', ori)
cv.imshow('SURF', img2)