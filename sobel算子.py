# python自己实现
# import cv2 as cv
# from scipy import signal
# import numpy as np
# import math
#
#
# # n阶的二项展开式系数,构建一维高斯平滑矩阵
# def getsmooth(n):
#     smooth = np.zeros([1, n], np.float32)
#     for i in range(n):
#         smooth[0][i] = math.factorial(n - 1) / (math.factorial(i) * math.factorial(n - i - 1))
#     return smooth
#
#
# def getdiff(n):
#     diff = np.zeros([1, n], np.float32)
#     smooth = getsmooth(n - 1)
#     for i in range(n):
#         if i == 0:
#             diff[0][i] = smooth[0][i]  # 恒等于1
#         elif i == n - 1:
#             diff[0][i] = -smooth[0][i - 1]  # 恒等于-1
#         else:
#             diff[0][i] = smooth[0][i] - smooth[0][i - 1]
#     return diff
#
#
# def sobel(img, size, boundary="symm", fillvalue=0):
#     smooth = getsmooth(size)
#     diff = getdiff(size)
#     print(smooth, diff)
#     print(np.dot(smooth.transpose(), diff))
#     print(np.dot(diff.transpose(), smooth))
#     rows, cols = img.shape[:2]
#     # 水平方向的sobel算子：先进行垂直方向的高斯平滑，再进行水平方向的差分
#     gaussian_y = signal.convolve2d(img, smooth.transpose(), mode="same", boundary=boundary, fillvalue=fillvalue)
#     sobel_x = signal.convolve2d(gaussian_y, diff, mode="same", boundary=boundary, fillvalue=fillvalue)
#
#     # 垂直方向的sobel算子：先进行水平方向的高斯平滑，再进行垂直方向的差分
#     gaussian_x = signal.convolve2d(img, smooth, mode="same", boundary=boundary, fillvalue=fillvalue)
#     sobel_y = signal.convolve2d(gaussian_x, diff.transpose(), mode="same", boundary=boundary, fillvalue=fillvalue)
#
#     return (sobel_x, sobel_y)
#
#
# if __name__ == "__main__":
#     img = cv.imread(r"./Pics/test.jpg", 0)
#     sobel_x, sobel_y = sobel(img, size=5)
#     sobel_x = np.abs(sobel_x)
#     sobel_edge_x = sobel_x.copy()
#     sobel_edge_x = sobel_edge_x / np.max(sobel_edge_x)
#     sobel_edge_x = sobel_edge_x * 255  # 进行归一化处理
#     sobel_edge_x = sobel_edge_x.astype(np.uint8)
#
#     sobel_y = np.abs(sobel_y)
#     sobel_edge_y = sobel_y.copy()
#     sobel_edge_y = sobel_edge_y / np.max(sobel_edge_y)
#     sobel_edge_y = sobel_edge_y * 255
#     sobel_edge_y = sobel_edge_y.astype(np.uint8)
#
#     sobel_edge = np.sqrt(np.power(sobel_x, 2.0), np.power(sobel_y, 2.0))
#     sobel_edge = sobel_edge / np.max(sobel_edge)
#     sobel_edge = sobel_edge * 255
#     sobel_edge = sobel_edge.astype(np.uint8)
#
#     cv.namedWindow("Original", 0)
#     cv.resizeWindow("Original", 360, 480)
#
#     cv.namedWindow("sobel_edge_x", 0)
#     cv.resizeWindow("sobel_edge_x", 360, 480)
#
#     cv.namedWindow("sobel_edge_y ", 0)
#     cv.resizeWindow("sobel_edge_y ", 360, 480)
#
#     cv.namedWindow("sobel_edge", 0)
#     cv.resizeWindow("sobel_edge", 360, 480)
#
#     cv.imshow("Original", img)
#     cv.imshow("sobel_edge_x", sobel_edge_x)
#     cv.imshow("sobel_edge_y ", sobel_edge_y)
#     cv.imshow("sobel_edge", sobel_edge)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# opencv自带sobel
import cv2 as cv
import numpy as np

img = cv.imread(r"./Pics/test.jpg")

#注意此处的ddepth不要设为-1，要设为cv.CV_32F或cv.CV_64F，否则会丢失太多信息
sobel_edge_x = cv.Sobel(img,ddepth=cv.CV_32F,dx=1,dy=0,ksize=5)
sobel_edge_x = np.abs(sobel_edge_x)
sobel_edge_x = sobel_edge_x/np.max(sobel_edge_x)
sobel_edge_x = sobel_edge_x*255  #进行归一化处理
sobel_edge_x = sobel_edge_x.astype(np.uint8)

sobel_edge_y = cv.Sobel(img,ddepth=cv.CV_32F,dx=0,dy=1,ksize=5)
sobel_edge_y = np.abs(sobel_edge_y)
sobel_edge_y = sobel_edge_y/np.max(sobel_edge_y)
sobel_edge_y = sobel_edge_y*255
sobel_edge_y = sobel_edge_y.astype(np.uint8)

sobel_edge1 = cv.addWeighted(sobel_edge_x,0.5,sobel_edge_y,0.5,0)

sobel_edge = cv.Sobel(img,ddepth=cv.CV_32F,dx=1,dy=1,ksize=5)
sobel_edge = np.abs(sobel_edge)
sobel_edge = sobel_edge/np.max(sobel_edge)
sobel_edge = sobel_edge*255
sobel_edge = sobel_edge.astype(np.uint8)

cv.namedWindow("Original", 0)
cv.resizeWindow("Original", 360, 480)

cv.namedWindow("sobel_edge_x", 0)
cv.resizeWindow("sobel_edge_x", 360, 480)

cv.namedWindow("sobel_edge_y ", 0)
cv.resizeWindow("sobel_edge_y ", 360, 480)

cv.namedWindow("sobel_edge", 0)
cv.resizeWindow("sobel_edge", 360, 480)

cv.namedWindow("sobel_edge1", 0)
cv.resizeWindow("sobel_edge1", 360, 480)

cv.imshow("Original",img)
cv.imshow("sobel_edge_x",sobel_edge_x)
cv.imshow("sobel_edge_y ",sobel_edge_y )
cv.imshow("sobel_edge",sobel_edge)
cv.imshow("sobel_edge1",sobel_edge1)
cv.waitKey(0)
cv.destroyAllWindows()
