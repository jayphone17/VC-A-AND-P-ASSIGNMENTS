# ORB 是一种一次性面部识别算法。
#
# 它目前正在你的手机和应用程序中使用，
#
# 例如 Google 照片，你可以在其中对人进行分组，你看到的图像是根据人分组的。
#
# 这个算法不需要任何主要的计算。
#
# 它不需要GPU。快速而简短。
#
# 它适用于关键点匹配。图像中不同区域的关键点匹配，如强度变化。

import numpy as np
import cv2
ori = cv2.imread('./Pics/test.jpg')
img = cv2.imread('./Pics/test.jpg', 0)

orb = cv2.ORB_create(nfeatures=200)
kp = orb.detect(img, None)
kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("ORB", 0)
cv2.resizeWindow("ORB", 480, 640)

cv2.imshow('Original', ori)
cv2.imshow('ORB', img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()