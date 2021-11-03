# 拉普拉斯算子没有对图像做平滑处理，会对噪声产生明显的响应，
# 所以一般先对图片进行高斯平滑处理，再采用拉普拉斯算子进行处理，
# 但这样要进行两次卷积处理。高斯拉普拉斯(LoG)边缘检测，
# 是将两者结合成一个卷积核，只进行一次卷积运算。

import numpy as np
from scipy import signal
import cv2


def createLoGKernel(sigma, size):
    H, W = size
    r, c = np.mgrid[0:H:1.0, 0:W:1.0]
    r -= (H-1)/2
    c -= (W-1)/2
    sigma2 = np.power(sigma, 2.0)
    norm2 = np.power(r, 2.0) + np.power(c, 2.0)
    LoGKernel = (norm2/sigma2 -2)*np.exp(-norm2/(2*sigma2))  # 省略掉了常数系数 1\2πσ4

    print(LoGKernel)
    return LoGKernel

def LoG(image, sigma, size, _boundary='symm'):
    LoGKernel = createLoGKernel(sigma, size)
    edge = signal.convolve2d(image, LoGKernel, 'same', boundary=_boundary)
    return edge


if __name__ == "__main__":
    img = cv2.imread("./Pics/test.jpg", 0)
    LoG_edge = LoG(img, 1, (11, 11))
    LoG_edge[LoG_edge>255] = 255
    # LoG_edge[LoG_edge>255] = 0
    LoG_edge[LoG_edge<0] = 0
    LoG_edge = LoG_edge.astype(np.uint8)

    LoG_edge1 = LoG(img, 1, (37, 37))
    LoG_edge1[LoG_edge1 > 255] = 255
    LoG_edge1[LoG_edge1 < 0] = 0
    LoG_edge1 = LoG_edge1.astype(np.uint8)

    LoG_edge2 = LoG(img, 2, (11, 11))
    LoG_edge2[LoG_edge2 > 255] = 255
    LoG_edge2[LoG_edge2 < 0] = 0
    LoG_edge2 = LoG_edge2.astype(np.uint8)

    cv2.namedWindow("Original", 0)
    cv2.resizeWindow("Original", 360, 480)
    cv2.namedWindow("LoG_edge", 0)
    cv2.resizeWindow("LoG_edge", 360, 480)
    cv2.namedWindow("LoG_edge1", 0)
    cv2.resizeWindow("LoG_edge1", 360, 480)
    cv2.namedWindow("LoG_edge2", 0)
    cv2.resizeWindow("LoG_edge2", 360, 480)

    cv2.imshow("Original", img)
    cv2.imshow("LoG_edge", LoG_edge)
    cv2.imshow("LoG_edge1", LoG_edge1)
    cv2.imshow("LoG_edge2", LoG_edge2)

    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


