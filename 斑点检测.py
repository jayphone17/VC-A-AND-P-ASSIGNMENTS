import cv2
import numpy as np;

# BLOB 代表二进制大对象。它指的是特定二值图像中具有共同属性的一组连接像素或区域。
# 这些区域是 OpenCV 中的轮廓，具有一些额外的特征，
# 如质心、颜色、面积、均值和覆盖区域中像素值的标准差。

ori = cv2.imread('./Pics/test.jpg')
im = cv2.imread("./Pics/test.jpg", cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector_create()

keypoints = detector.detect(im)
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original" , 480, 640)

cv2.namedWindow("BLOB", 0)
cv2.resizeWindow("BLOB", 480, 640)

cv2.imshow('Original',ori)
cv2.imshow('BLOB',im_with_keypoints)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()