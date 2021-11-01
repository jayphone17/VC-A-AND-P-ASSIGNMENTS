# 特征匹配就像比较两个图像的特征，这两个图像可能在方向、视角、亮度上不同，甚至大小和颜色也不同。

import cv2
img1 = cv2.imread('./Pics/test2 .jpg', 0)
img2 = cv2.imread('./Pics/test3.jpg', 0)

orb = cv2.ORB_create(nfeatures=500)

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)


cv2.namedWindow("original image", 0)
cv2.resizeWindow("original image" , 320, 480)

cv2.namedWindow("test image", 0)
cv2.resizeWindow("test image",  320, 480)

cv2.namedWindow("Matches", 0)
cv2.resizeWindow("Matches", 640, 480)

cv2.imshow('original image', img1)
cv2.imshow('test image', img2)
cv2.imshow('Matches', match_img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

