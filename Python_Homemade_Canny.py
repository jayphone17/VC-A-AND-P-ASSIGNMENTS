#coding:utf-8
# 自己实现Canny边缘提取算法
import cv2
import numpy as np
import math

def no_maximum_suppression_default(dx, dy):
    edge = np.sqrt(np.power(dx, 2) + np.power(dy, 2))  # 梯度大小
    rows, cols = dx.shape
    gradientDirection = np.zeros(dx.shape)
    edge_nonMaxSup = np.zeros(dx.shape)
    # 最外层一圈为填充0，不进行处理
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            angle = math.atan2(dy[r][c], dx[r][c])*180/math.pi  # 梯度方向
            gradientDirection[r][c] = angle
            # 左右方向
            if abs(angle) < 22.5 or abs(angle) > 157.5:
                if edge[r][c] > edge[r][c-1] and edge[r][c] > edge[r][c+1]:
                    edge_nonMaxSup[r][c] = edge[r][c]
            # 左上角，右下角方向
            if 22.5 <= angle < 67.5 or -157.5 <= angle < -112.5:
                if edge[r][c] > edge[r-1][c-1] and edge[r][c] > edge[r+1][c+1]:
                    edge_nonMaxSup[r][c] = edge[r][c]
            # 上下方向
            if 67.5 <= abs(angle) <= 112.5:
                if edge[r][c] > edge[r-1][c] and edge[r][c] > edge[r+1][c]:
                    edge_nonMaxSup[r][c] = edge[r][c]
            # 左下角，右上角方向
            if 112.5 < angle <= 157.5 or -67.5 < angle <= -22.5:
                if edge[r][c] > edge[r-1][c+1] and edge[r][c] > edge[r+1][c-1]:
                    edge_nonMaxSup[r][c] = edge[r][c]
    return edge_nonMaxSup


def checkInRange(r, c, rows, cols):
    if 0 <= r < rows and 0 <= c < cols:
        return True
    else:
        return False


def trace(edge_nonMaxSup, edge, lowerThresh, r, c, rows, cols):
    if edge[r][c] == 0:
        edge[r][c] = 255
        for i in range(-1, 2):
            for j in range(-1, 2):
                if checkInRange(r+i, c+j, rows, cols) and edge_nonMaxSup[r+i][c+j] >= lowerThresh:
                    trace(edge_nonMaxSup, edge, lowerThresh, r+i, c+j, rows, cols)

def hysteresisThreshold(edge_nonMaxSup, lowerThresh, upperThresh):
    rows, cols = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape, np.uint8)
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            # 大于高阈值的点确定为边缘点，并以该点为起点进行深度优先搜索
            if edge_nonMaxSup[r][c] >= upperThresh:
                trace(edge_nonMaxSup, edge, lowerThresh, r, c, rows, cols)
            # 小于低阈值的点剔除掉
            if edge_nonMaxSup[r][c] < lowerThresh:
                edge[r][c] = 0
    return edge

if __name__ == "__main__":
    img_path = r"./Pics/test.jpg"
    img = cv2.imread(img_path, 0)

    sobel_edge_x = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
    sobel_edge_y = cv2.Sobel(img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

    # 梯度方向非极大值抑制
    edge_nonMaxSup = no_maximum_suppression_default(sobel_edge_x, sobel_edge_y)
    edge_nonMaxSup[edge_nonMaxSup>255] = 255

    # 双阈值后阈值处理
    edge_nonMaxSup = edge_nonMaxSup.astype(np.uint8)
    canny_edge = hysteresisThreshold(edge_nonMaxSup, 60, 180)

    cv2.namedWindow("Original", 0)
    cv2.resizeWindow("Original", 360, 480)

    cv2.namedWindow("canny_edge", 0)
    cv2.resizeWindow("canny_edge", 360, 480)

    cv2.imshow("Original", img)
    cv2.imshow("canny_edge", canny_edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
#   if edge[r][c] == 0:
# Fatal Python error: Cannot recover from stack overflow.
# Python runtime state: initialized


# import cv2
#
# img_path= r"./Pics/test.jpg"
# img = cv2.imread(img_path)
#
# canny_edge1 = cv2.Canny(img, threshold1=60, threshold2=180)
# canny_edge2 = cv2.Canny(img, threshold1=180, threshold2=230)
# canny_edge3 = cv2.Canny(img, threshold1=180, threshold2=230, apertureSize=5, L2gradient=True)
#
# cv2.namedWindow("Original", 0)
# cv2.resizeWindow("Original", 360, 480)
#
# cv2.namedWindow("canny_edge1", 0)
# cv2.resizeWindow("canny_edge1", 360, 480)
#
# cv2.namedWindow("canny_edge2", 0)
# cv2.resizeWindow("canny_edge2", 360, 480)
#
# cv2.namedWindow("canny_edge3", 0)
# cv2.resizeWindow("canny_edge3", 360, 480)
#
# cv2.imshow("Original", img)
# cv2.imshow("canny_edge1", canny_edge1)
# cv2.imshow("canny_edge2", canny_edge2)
# cv2.imshow("canny_edge3", canny_edge3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()