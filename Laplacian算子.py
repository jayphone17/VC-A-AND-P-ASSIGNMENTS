# opencv中提供Laplacian()函数计算拉普拉斯运算，其对应参数如下：

# dst = cv2.Laplacian(src, ddepth, ksize, scale, delta, borderType)
#     src: 输入图像对象矩阵,单通道或多通道
#     ddepth:输出图片的数据深度,注意此处最好设置为cv.CV_32F或cv.CV_64F
#     ksize: Laplacian核的尺寸，默认为1，采用上面3*3的卷积核
#     scale: 放大比例系数
#     delta: 平移系数
#     borderType: 边界填充类型

import cv2

img = cv2.imread("./Pics/test.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst_img = cv2.Laplacian(img, cv2.CV_32F)
laplacian_edge = cv2.convertScaleAbs(dst_img)  #取绝对值后，进行归一化

dst_img_gray = cv2.Laplacian(img_gray, cv2.CV_32F)
laplacian_edge_gray = cv2.convertScaleAbs(dst_img_gray)  #取绝对值后，进行归一化

cv2.namedWindow("Original", 0)
cv2.resizeWindow("Original", 360, 480)

cv2.namedWindow("laplacian_edge", 0)
cv2.resizeWindow("laplacian_edge", 360, 480)

cv2.namedWindow("img_gray", 0)
cv2.resizeWindow("img_gray" , 360, 480)

cv2.namedWindow("laplacian_edge_gray ", 0)
cv2.resizeWindow("laplacian_edge_gray ", 360, 480)

cv2.imshow("Original", img)
cv2.imshow("laplacian_edge", laplacian_edge)
cv2.imshow("img_gray", img_gray)
cv2.imshow("laplacian_edge_gray ", laplacian_edge_gray)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()