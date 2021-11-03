import cv2
import numpy as np

img = cv2.imread("./Pics/test.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst_img_gray = cv2.Laplacian(img_gray, cv2.CV_32F)

# 处理方式1
laplacian_edge = cv2.convertScaleAbs(dst_img_gray)  #取绝对值后，进行归一化
# convertScaleAbs等同于下面几句：
# laplacian_edge = np.abs(laplacian_edge)
# laplacian_edge = laplacian_edge/np.max(laplacian_edge)
# laplacian_edge = laplacian_edge*255  #进行归一化处理
# laplacian_edge = laplacian_edge.astype(np.uint8)

# 处理方式2
laplacian_edge2 = np.copy(laplacian_edge)
# laplacian_edge2[laplacian_edge > 0] = 255
laplacian_edge2[laplacian_edge > 255] = 255
laplacian_edge2[laplacian_edge <= 0] = 0
laplacian_edge2 = laplacian_edge2.astype(np.uint8)


#先进行平滑处理
gaussian_img_gray = cv2.GaussianBlur(dst_img_gray, (3, 3), 1)
laplacian_edge3 = cv2.convertScaleAbs(gaussian_img_gray)  #取绝对值后，进行归一化

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original", 360, 480)

cv2.namedWindow("laplacian_edge", 0)
cv2.resizeWindow("laplacian_edge", 360, 480)

cv2.namedWindow("laplacian_edge2", 0)
cv2.resizeWindow("laplacian_edge2" , 360, 480)

cv2.namedWindow("laplacian_edge3", 0)
cv2.resizeWindow("laplacian_edge3", 360, 480)

cv2.imshow("Original", img_gray)
cv2.imshow("laplacian_edge", laplacian_edge)
cv2.imshow("laplacian_edge2", laplacian_edge2)
cv2.imshow("laplacian_edge3", laplacian_edge3)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
