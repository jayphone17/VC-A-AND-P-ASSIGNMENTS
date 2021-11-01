import cv2
import numpy as np

input_img = './Pics/test.jpg'

ori = cv2.imread(input_img)
image = cv2.imread(input_img)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
dst = cv2.dilate(dst,None)
image[dst>0.01*dst.max()]=[0,0,255]

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("Harris", 0)
cv2.resizeWindow("Harris", 480, 640)

cv2.imshow('Original',ori)
cv2.imshow('Harris',image)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

